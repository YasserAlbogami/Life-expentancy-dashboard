import streamlit as st
import pandas as pd


def render(df):
    st.header("🧹 Data Cleaning & Preprocessing")

    # Phase 1: Rename Features
    st.subheader("🔧 Phase 1: Rename Selected Features")
    rename_map = {
        'Under_five_deaths': '0-5yrs_deaths',
        'Alcohol_consumption': 'Alcohol',
        'Thinness_ten_nineteen_years': 'Thinness_10-19',
        'Thinness_five_nine_years': 'Thinness_5-9',
        'Economy_status_Developed': 'Developed',
        'Economy_status_Developing': 'Developing'
    }
    st.write("✅ Renamed columns:")
    st.write(pd.DataFrame(rename_map.items(), columns=["Original", "Renamed"]))

    # Apply the renaming
    df.rename(columns=rename_map, inplace=True)

    # Phase 2: Value Ranges
    st.subheader("📊 Phase 2: Value Ranges of Numeric Features")
    numeric_features = df.select_dtypes(include=['number'])
    min_values = numeric_features.min()
    max_values = numeric_features.max()
    min_max_df = pd.DataFrame({'Min Value': min_values, 'Max Value': max_values})
    st.dataframe(min_max_df.style.format(precision=2), use_container_width=True)

    # Phase 3: Unique Values
    st.subheader("🔣 Phase 3: Unique Values in Categorical Features")
    categorical_features = df.select_dtypes(include=['object', 'category'])
    for col in categorical_features.columns:
        st.markdown(f"**📝 {col}**: {df[col].nunique()} unique value(s)")
        st.write(sorted(df[col].dropna().unique()))

    # Phase 4: Missing Values
    st.subheader("🧪 Phase 4: Missing Values Check")
    null_counts = df.isnull().sum()
    total_nulls = null_counts.sum()
    if total_nulls == 0:
        st.success("✅ No missing values detected in the dataset!")
    else:
        st.warning("⚠️ Missing values detected:")
        st.dataframe(null_counts[null_counts > 0], use_container_width=True)

    # Phase 5: Shorten Region Names
    st.subheader("✂️ Phase 5: Shorten Region Names")
    region_replacements = {
        'Middle East': 'Mid East',
        'European Union': 'EU',
        'South America': 'South Am',
        'Central America and Caribbean': 'Central Am',
        'Rest of Europe': 'Non EU',
        'North America': 'North Am'
    }
    df['Region'] = df['Region'].replace(region_replacements)
    st.write("✅ Replaced region names:")
    st.write(pd.DataFrame(region_replacements.items(), columns=["Original", "Shortened"]))

# ✅ Preprocessing logic only (used by both process() and render())
def _preprocess_logic(df):
    # Rename columns
    rename_map = {
        'Under_five_deaths': '0-5yrs_deaths',
        'Alcohol_consumption': 'Alcohol',
        'Thinness_ten_nineteen_years': 'Thinness_10-19',
        'Thinness_five_nine_years': 'Thinness_5-9',
        'Economy_status_Developed': 'Developed',
        'Economy_status_Developing': 'Developing'
    }
    df.rename(columns=rename_map, inplace=True)

    # Shorten region names
    region_replacements = {
        'Middle East': 'Mid East',
        'European Union': 'EU',
        'South America': 'South Am',
        'Central America and Caribbean': 'Central Am',
        'Rest of Europe': 'Non EU',
        'North America': 'North Am'
    }
    df['Region'] = df['Region'].replace(region_replacements)

    return df

# ✅ To use in all pages for loading + preprocessing
@st.cache_data
def process():
    df = pd.read_csv("data/Life-Expectancy-Data-Updated.csv")
    df = _preprocess_logic(df)
    return df
