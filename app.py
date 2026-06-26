from src.visualizer import *
from src.data_cleaner import *

import streamlit as st
import pandas as pd

# -------------------------------
# Page Title
# -------------------------------
st.title("📊 DataSense AI")
st.subheader("Intelligent Data Analytics Assistant")

# -------------------------------
# File Upload
# -------------------------------
uploaded_file = st.file_uploader(
    "Upload a CSV or Excel file",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    # Read Dataset
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # -------------------------------
    # Dataset Preview
    # -------------------------------
    st.write("## Dataset Preview")
    st.dataframe(df)

    # -------------------------------
    # Dataset Information
    # -------------------------------
    st.write("## Dataset Information")
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")

    # -------------------------------
    # Column Names
    # -------------------------------
    st.write("## Column Names")
    st.write(df.columns.tolist())

    # -------------------------------
    # Summary Statistics
    # -------------------------------
    st.write("## Summary Statistics")
    st.write(df.describe())

    # -------------------------------
    # Data Quality Report
    # -------------------------------
    st.write("## Data Quality Report")

    missing = get_missing_values(df)
    duplicates = get_duplicate_count(df)

    st.write("### Missing Values Per Column")
    st.write(missing)

    st.write(f"### Duplicate Rows: {duplicates}")

    if st.button("Remove Duplicates", key="remove_duplicates"):
        df = remove_duplicates(df)
        st.success("Duplicates Removed")

    if st.button("Fill Missing Values", key="fill_missing"):
        df = fill_missing_values(df)
        st.success("Missing Values Filled")

    # -------------------------------
    # Data Visualization
    # -------------------------------
    st.write("## Data Visualization")

    numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()
    all_columns = df.columns.tolist()

    # Histogram
    if len(numeric_columns) > 0:

        st.write("### Histogram")

        hist_column = st.selectbox(
            "Select Numeric Column",
            numeric_columns
        )

        fig = create_histogram(df, hist_column)
        st.plotly_chart(fig, use_container_width=True)

    # Bar Chart
    st.write("### Bar Chart")

    bar_column = st.selectbox(
        "Select Column",
        all_columns
    )

    fig = create_bar_chart(df, bar_column)
    st.plotly_chart(fig, use_container_width=True)

    # Scatter Plot
    if len(numeric_columns) >= 2:

        st.write("### Scatter Plot")

        x_col = st.selectbox(
            "X Axis",
            numeric_columns,
            key="x_axis"
        )

        y_col = st.selectbox(
            "Y Axis",
            numeric_columns,
            index=1,
            key="y_axis"
        )

        fig = create_scatter_plot(df, x_col, y_col)
        st.plotly_chart(fig, use_container_width=True)