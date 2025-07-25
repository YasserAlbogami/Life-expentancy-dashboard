import streamlit as st
from data import fillters

from tabs import (
    general_insights,
    overall_insights,
    region_based_analytics,
    saudi_arabia,

)
from utils import apply_custom_style, add_logo_to_sidebar

# Apply global style and logo amnd 
apply_custom_style()
add_logo_to_sidebar()

#  Page title
st.set_page_config(page_title="🌐 Life Expectancy Dashboard", layout="wide")
st.title("🌐 Life Expectancy Dashboard")
st.markdown("Use the sidebar to filter data by country, region, and year.")

# Get filtered dataframe
df_filtered = fillters.get_filtered_df()

# Create tabs
tab0, tab1, tab2, tab3 = st.tabs([
    "📊 General Insights",
    "🗺️ Region-Based Analytics",
    "🌍 Numerical Analysis & comparison",
    "🇸🇦 Saudi Arabia",
])

# Render each tab content


with tab0:
    general_insights.render(df_filtered)

with tab1:
    region_based_analytics.render(df_filtered)


with tab2:
    overall_insights.render(df_filtered)

with tab3:
        # Force Saudi-only data, ignoring sidebar filters
    saudi_df = df_filtered.copy()
    saudi_df = saudi_df[saudi_df["Country"] == "Saudi Arabia"]
    saudi_arabia.render(saudi_df)