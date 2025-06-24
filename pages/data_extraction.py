import streamlit as st
import pandas as pd
from memo_parser import process_excel_streaming
from io import BytesIO

st.title("📄 Data Extraction From Memos")
st.divider()

with st.expander("❗️ Instructions", expanded=False):
    st.markdown("""  
    ### 🔹 **What This Tool Does**

    This tool uses a fine-tuned **gpt-4o-mini** model to extract structured information from unstructured bid memos. It identifies the following fields:

    - **Bid Sponsor** (`K12`, `HE`, `GOV`)  
    - **Bid Type** (`AFB`, `ATB`, `IFB`, `ITB`, `NTB`, `RFB`, `RFI`, `RFP`, `RFQ`)  
    - **Bid Title**  
    - **Institution**  
    - **Publish Date**, **Pre-Bid Date**, **Due Date**

    ---

    ### 📁 **Input Format**

    Upload an Excel (`.xlsx`) file with the following **required columns**:

    | Column Name        | Description                                |
    |--------------------|--------------------------------------------|
    | `UID`              | Unique ID for each memo                    |
    | `State`            | State name or abbreviation                 |
    | `Bid Document Url` | Link to bid document                       |
    | `Bid Url`          | Link to original bid page                  |
    | `Memo`             | Full unstructured text of the memo         |

    ---

    ### ⚙️ **Steps to Use the Tool**

    1. **Choose Model Version**  
    Select which version of the fine-tuned gpt-4o-mini model you want to use:
    - `Version 1`: Initial fine-tuned model  
    - `Version 2`: Improved model trained on mismatches  

    ⚠️ **Note:** There may be trade-offs between the two models. **Version 2** offers more detailed bid titles, but may occasionally miss edge cases previously handled by **Version 1**.

    2. **Upload Your Excel File**  
    Use the file uploader to submit your `.xlsx` file. Make sure it has the correct columns.

    3. **Processing**  
    Once uploaded, the tool will:
    - Process each memo  
    - Extract structured fields using the selected model  
    - Validate the data using built-in rules

    4. **Download Output**  
    After processing, you can:
    - Preview the extracted results  
    - Download the structured Excel file containing the extracted fields

    ---

    ### 📁 **Output File Format**

    The output `.xlsx` file will contain the following columns:

    - `UID` (from input)  
    - `Bid Keywords` (left empty for now)  
    - `Bid Sponsor` (extracted)  
    - `Bid Type` (extracted)  
    - `Zip Code` (left empty)  
    - `State` (from input)  
    - `Bid Title` (extracted)  
    - `Bid Document Url` (from input)  
    - `Institution` (extracted)  
    - `Bid Url` (from input)  
    - `Publish Date` (extracted)  
    - `Pre Bid` (extracted, if available)  
    - `Due Date` (extracted)  
    - `Memo` (original input)

    ---

    ### ⚠️ **Notes**

    - All date fields will be formatted as `DD/MM/YYYY`.  
    - If a memo fails validation or the model cannot extract fields, it will still be included in the output with respective fields left blank.  
    - Processing time depends on the number of memos and API latency.
    """)

st.subheader("Choose Version")
version = st.selectbox("Select Model Version", ["Version 1", "Version 2"])

st.subheader("Upload Your Excel File")
uploaded_file = st.file_uploader("Format Given In Instructions", type=["xlsx"])

if uploaded_file:
    st.success("File uploaded. Click 'Upload' to start processing.")

    if st.button("Upload"):
        df = pd.read_excel(uploaded_file)

        if not {"UID", "State", "Bid Document Url", "Bid Url", "Memo"}.issubset(df.columns):
            st.error("Required columns missing. Please check your file.")
        else:
            progress = st.progress(0, text="Starting extraction...")
            status = st.empty()

            # Stream memo processing
            structured_data = None

            for i, total, structured_data in process_excel_streaming(df, version):
                percent = int((i / total) * 100)
                progress.progress(percent, text=f"Processing memo {i} of {total}...")
                status.info(f"📄 Processed UID {df.iloc[i-1]['UID']}")
            
            progress.progress(100, "Extraction complete!")
            status.success("All memos processed.")
            
            # Final DataFrame
            output_df = pd.DataFrame(structured_data, columns=[
                "UID", "Bid Keywords", "Bid Sponsor", "Bid Type", "Zip Code", "State",
                "Bid Title", "Bid Document Url", "Institution", "Bid Url",
                "Publish Date", "Pre Bid", "Due Date", "Memo"
            ])

            st.dataframe(output_df, use_container_width=True)

            # Download
            buffer = BytesIO()
            output_df.to_excel(buffer, index=False)
            buffer.seek(0)

            st.download_button(
                label="Download Extracted Excel",
                data=buffer,
                file_name="structured_output.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )