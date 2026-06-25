from src.data_cleaner import *


import streamlit as st
import pandas as pd

# Title
st.title("📊 DataSense AI")
st.subheader("Intelligent Data Analytics Assistant")

# File uploader
uploaded_file = st.file_uploader(
    "Upload a CSV or Excel file",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    # Read file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # Display data
    st.write("## Dataset Preview")
    st.dataframe(df)

    # Dataset information
    st.write("## Dataset Information")
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")

    # Column names
    st.write("## Column Names")
    st.write(df.columns.tolist())

    # Summary statistics
    st.write("## Summary Statistics")
    st.write(df.describe())

    st.write("## Data Quality Report")

missing = get_missing_values(df)
duplicates = get_duplicate_count(df)

st.write("Missing Values Per Column")
st.write(missing)

st.write(f"Duplicate Rows: {duplicates}")

if st.button("Remove Duplicates"):
    df = remove_duplicates(df)
    st.success("Duplicates Removed")

if st.button("Fill Missing Values"):
    df = fill_missing_values(df)
    st.success("Missing Values Filled")