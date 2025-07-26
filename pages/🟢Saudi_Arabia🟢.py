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

import streamlit as st
import plotly.express as px

# Apply global style and add logo to sidebar
apply_custom_style()
add_logo_to_sidebar()

# Page configuration
st.set_page_config(page_title="🇸🇦 Saudi Arabia Life Expectancy", layout="wide")

# Page title with flag
st.title("🇸🇦 Saudi Arabia Life Expectancy Dashboard")
st.markdown(
    "This tab focuses on life expectancy trends in **Saudi Arabia**, "
    "with comparison to global averages. Use the sidebar filters to adjust data."
)

# Get filtered dataframe
df_filtered = fillters.get_filtered_df()





st.markdown("---")

# Global average per year
global_trend = df_filtered.groupby('Year')['Life_expectancy'].mean().reset_index()
global_trend['Country'] = 'Global Average'

# Saudi Arabia data
saudi_trend = df_filtered[df_filtered['Country'] == 'Saudi Arabia'][['Year', 'Life_expectancy']].copy()
saudi_trend['Country'] = 'Saudi Arabia'
saudi_trend.sort_values(by="Year", ascending=True, inplace=True)

# Combine both dataframes
compare = pd.concat([global_trend, saudi_trend], ignore_index=True)

# 1:  line chart comparing Saudi Arabia with global average

fig_saudi = px.line(
    compare,
    x='Year',
    y='Life_expectancy',
    color='Country',
    markers=True,
    title="Life Expectancy: Saudi Arabia vs Global Average",
)
fig_saudi.update_layout(
    yaxis_title="Life Expectancy (Years)",
    xaxis_title="Year",
    xaxis_type='category',
    legend_title="Country"
)
st.subheader("1:  🇸🇦 Saudi Arabia vs Global Life Expectancy")

st.plotly_chart(fig_saudi, use_container_width=True)
