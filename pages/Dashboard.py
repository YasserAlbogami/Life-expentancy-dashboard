import streamlit as st
from data import fillters
import pandas as pd
from tabs import (
    Linear_Model,
    general_insights,
    numrecial_analysis,
    region_based_analytics,

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
    "🤖 Linear Regression Model",
])

# Render each tab content


with tab0:
    general_insights.render(df_filtered)

with tab1:
    region_based_analytics.render(df_filtered)


with tab2:
    numrecial_analysis.render(df_filtered)

with tab3:
    
    Linear_Model.render(pd.read_csv("data/Life-Expectancy-Data-Updated.csv"))  # Assuming the data is in this CSV file