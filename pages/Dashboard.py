import streamlit as st
from data import fillters
import pandas as pd
from tabs import (
    Linear_Model,
    general_insights,
    numrecial_analysis,
    region_based_analytics,

)


#  Page title
st.set_page_config(page_title="🌐 Life Expectancy Dashboard", layout="wide")
st.title("🌐 Life Expectancy Dashboard")
st.markdown("Use the sidebar to filter data by country, region, and year.")

# Get filtered dataframe
df_filtered = fillters.get_filtered_df()

# Create tabs
tab0, tab1, tab2, tab3 = st.tabs([
    "📊 General Insights",
    "🌍 Numerical Analysis",
    "🗺️ Region-Based Analytics",
    "🤖 Linear Regression Model",
])

# Render each tab content
with tab0:
    general_insights.render(df_filtered)

with tab1:
    numrecial_analysis.render(df_filtered)

with tab2:
    region_based_analytics.render(df_filtered)

with tab3:
    Linear_Model.render(pd.read_csv("data/Life-Expectancy-Data-Updated.csv"))
