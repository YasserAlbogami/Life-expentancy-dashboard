# filters.py

import streamlit as st
import pandas as pd
from main_tabs import preprocessing


@st.cache_data
def load_data():
    df = preprocessing.process()
    return df


def get_filtered_df():

    # 📥 Load dataset
    df = load_data()

    # Sidebar navigation
    st.sidebar.title("🔗 Navigation")

    st.sidebar.subheader("🔧 Filters")

    # Reset filters button
    if st.sidebar.button("🔄 Reset Filters"):
        st.session_state["selected_regions"] = list(df["Region"].unique())
        st.session_state["selected_countries"] = list(df["Country"].unique())
        st.session_state["selected_years"] = (
            int(df["Year"].min()), int(df["Year"].max())
        )
    
    # Prepare options
    # 🔹 Get all unique regions and year range from the dataset
    all_regions = df["Region"].unique()
    all_years = (int(df["Year"].min()), int(df["Year"].max()))

    # 🔹 Get previously selected values from session state (if any)
    default_regions = st.session_state.get(
        "selected_regions", list(all_regions))
    default_years = st.session_state.get("selected_years", all_years)

    # 🔸 REGION SELECTION (always first)
    selected_regions = st.sidebar.multiselect(
        "Select Region", all_regions, default=default_regions, key="selected_regions"
    )

    # 🔸 Filter the list of countries based on selected regions
    filtered_country_list = df[df["Region"].isin(
        selected_regions)]["Country"].unique()

    # ✅ ONLY THIS PART IS CHANGED: auto-fill selected countries based on selected regions

    # 🔸 Keep only previously selected countries that still belong to current regions
    previous_countries = st.session_state.get(
        "selected_countries", list(filtered_country_list))
    default_countries = [
        c for c in previous_countries if c in filtered_country_list]

    # 🔸 Country "Select All" toggle
    select_all_countries = st.sidebar.checkbox(
        "✅ Select All Countries in Region")

    # 🔸 COUNTRY SELECTION (auto-filled, editable)

    # If checkbox is checked, override session state with full filtered list

    if select_all_countries:
        st.session_state.selected_countries = list(filtered_country_list)

    selected_countries = st.sidebar.multiselect(
        "Select Country",
        filtered_country_list,
        default=[c for c in st.session_state.get(
            "selected_countries", []) if c in filtered_country_list],
        key="selected_countries"
    )

    # 🔸 Optional: Update selected_regions dynamically from selected countries
    if selected_countries:
        selected_regions = df[df["Country"].isin(
            selected_countries)]["Region"].unique().tolist()

    # 🔸 YEAR RANGE SELECTION
    selected_years = st.sidebar.slider(
        "Select Year Range",
        all_years[0],
        all_years[1],
        value=default_years,
        key="selected_years"
    )

    # 🔸 FINAL FILTERING based on selected region, country, and year
    filtered_df = df[
        (df["Region"].isin(selected_regions)) &
        (df["Country"].isin(selected_countries)) &
        (df["Year"] >= selected_years[0]) &
        (df["Year"] <= selected_years[1])
    ]

    return filtered_df
