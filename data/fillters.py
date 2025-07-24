# filters.py

import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv("data/Life-Expectancy-Data-Updated.csv")
    return df

def get_filtered_df():
    df = load_data()

    # Sidebar filters
    countries = df["Country"].unique()
    regions = df["Region"].unique()
    years = df["Year"].unique()

    selected_countries = st.sidebar.multiselect("Select Country", countries, default=countries)
    selected_regions = st.sidebar.multiselect("Select Region", regions, default=regions)
    selected_years = st.sidebar.slider("Select Year Range", int(df["Year"].min()), int(df["Year"].max()), (2000, 2015))

    # Apply filters
    filtered_df = df[
        (df["Country"].isin(selected_countries)) &
        (df["Region"].isin(selected_regions)) &
        (df["Year"] >= selected_years[0]) &
        (df["Year"] <= selected_years[1])
    ]
    return filtered_df