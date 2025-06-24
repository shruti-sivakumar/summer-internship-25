import streamlit as st

# Configure the page
st.set_page_config(
    page_title="Bid Processing Suite", 
    layout="wide",
    page_icon="📊"
)

# Create pages
data_extraction_page = st.Page("pages/data_extraction.py", title="Data Extraction From Memos", icon="📄")
keyword_tagging_page = st.Page("pages/keyword_tagging.py", title="Keywords Tagging", icon="🏷️")

# Navigation
pg = st.navigation([data_extraction_page, keyword_tagging_page])

# Sidebar info
st.sidebar.info("Built by Shruti Sivakumar as part of her internship at Visual Infomedia (2025).")

# Run the selected page
pg.run()