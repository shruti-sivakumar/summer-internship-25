import os
import pandas as pd
import json
from pydantic import BaseModel, Field, ValidationError, field_validator
from typing import Optional
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ------------------ Pydantic Model ------------------

class MemoInfo(BaseModel):
    Bid_Sponsor: str = Field(...)
    Bid_Type: str = Field(...)
    Bid_Title: str = Field(...)
    Institution: str = Field(...)
    Publish_Date: Optional[str] = Field(...)
    Pre_Bid_Date: Optional[str] = Field(None)
    Due_Date: str = Field(...)

    @field_validator("Bid_Sponsor")
    def validate_bid_sponsor(cls, value):
        allowed = ["K12", "HE", "GOV"]
        return value if value in allowed else ""

    @field_validator("Bid_Type")
    def validate_bid_type(cls, value):
        allowed = ["AFB", "ATB", "IFB", "ITB", "NTB", "RFB", "RFI", "RFP", "RFQ"]
        return value if value in allowed else "RFP"


# ------------------ Helpers ------------------

def format_date(date_str):
    """Convert YYYY-MM-DD to DD/MM/YYYY."""
    if date_str and date_str != "null":
        try:
            return pd.to_datetime(date_str).strftime("%d/%m/%Y")
        except:
            return date_str
    return ""


# ------------------ Core Processing ------------------

def process_memo(uid, memo_text, model_version):
    # Select model based on version
    model_id = {
        "Version 1": "ft:gpt-4o-mini-2024-07-18:visual-infomedia::B01jGrca",
        "Version 2": "ft:gpt-4o-mini-2024-07-18:visual-infomedia::BidgnWIU"
    }[model_version]

    prompt = f"""
    Extract the following information from the memo:
    - Bid Sponsor (one of: HE (Higher Education), K12 (K-12 institutions), GOV (Government institutions))
    - Bid Type (one of: AFB, ATB, IFB, ITB, NTB, RFB, RFI, RFP, RFQ)
    - Bid Title
    - Institution
    - Publish Date (if given, YYYY-MM-DD)
    - Pre-Bid Date (if any, YYYY-MM-DD)
    - Due Date (YYYY-MM-DD)

    Memo:
    {memo_text}
    """

    try:
        response = client.beta.chat.completions.parse(
            model=model_id,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert at structured data extraction. You will be given an unstructured memo and should extract structured values in the defined format."
                },
                {"role": "user", "content": prompt},
            ],
            response_format=MemoInfo,
        )
        parsed_data = json.loads(response.choices[0].message.content)
        memo_info = MemoInfo(**parsed_data)
        return uid, memo_info

    except Exception as e:
        print(f"Error processing UID {uid}: {e}")
        return uid, None


def process_excel_streaming(df, model_version):
    total = len(df)
    structured_data = []

    for i, row in enumerate(df.itertuples(), 1):
        uid, state, bid_doc_url, bid_url, memo = row.UID, row.State, row._3, row._4, row.Memo

        uid, memo_info = process_memo(uid, memo, model_version)

        if memo_info:
            structured_data.append([
                uid,
                "",  # Bid Keywords
                memo_info.Bid_Sponsor,
                memo_info.Bid_Type,
                "",  # Zip Code
                state,
                memo_info.Bid_Title,
                bid_doc_url,
                memo_info.Institution,
                bid_url,
                format_date(memo_info.Publish_Date),
                format_date(memo_info.Pre_Bid_Date),
                format_date(memo_info.Due_Date),
                memo
            ])
        else:
            # If error, insert blank values
            structured_data.append([
                uid,
                "",
                "", "", "",
                state,
                "", bid_doc_url, "", bid_url,
                "", "", "",
                memo
            ])

        yield i, total, structured_data