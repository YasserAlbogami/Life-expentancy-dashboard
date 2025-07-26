import streamlit as st
from data import fillters
import pandas as pd
from tabs import (
    Linear_Model,
    general_insights,
    numrecial_analysis,
    region_based_analytics,
)
import streamlit as st
import plotly.express as px



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

# 2:  Correlation with Life Expectancy for saudi arabia (Plotly Heatmap)
corr_matrix = df_filtered[df_filtered['Country']=='Saudi Arabia'].corr(numeric_only=True)
life_corr = corr_matrix['Life_expectancy'].drop(index=['Developing','Developed','Incidents_HIV'], errors='ignore')
life_corr = life_corr.drop(labels=["Life_expectancy"])

life_corr = life_corr.reset_index()
life_corr.columns = ["Variable", "Correlation_with_Life_expectancy"]
life_corr = life_corr.sort_values(by="Correlation_with_Life_expectancy")
fig = px.imshow([life_corr["Correlation_with_Life_expectancy"]],
                labels=dict(x='Variable',color="Correlation"),
                x=life_corr['Variable'],
                y=['Life_expectancy'],
                color_continuous_scale="RdBu",
                text_auto=".2f",
                zmax=1,
                zmin=-1)
fig.update_layout(height=300, title="Correlation of Each Variable with Life Expectancy: Saudi Arabia ")
st.subheader("2:  🇸🇦 Correlation with Life Expectancy for Saudi Arabia")
st.plotly_chart(fig, use_container_width=True)


# 2: Mortality Trends in Saudi Arabia

df_saudi = df_filtered[df_filtered['Country']=='Saudi Arabia'].sort_values(by="Year")

fig1 = px.line(df_saudi,
              x='Year',
              y=['Adult_mortality','Infant_deaths','0-5yrs_deaths'],
              markers=True,
              title='Mortality Rates: Saudi Arabia')
fig1.update_layout(xaxis_title="Year",
                  yaxis_title="Mortality Rate (per 1,000)")
st.subheader("3:  🇸🇦 Mortality Trends in Saudi Arabia")
st.plotly_chart(fig1, use_container_width=True)


# 2: Life Expectancy vs. Schooling in Saudi Arabia
df_saudi = df_filtered[df_filtered['Country']=='Saudi Arabia'].sort_values(by="Life_expectancy")

fig2 = px.line(df_saudi,
              x='Life_expectancy',
              y='Schooling',
              markers=True,
              title='Life Expectancy vs. Schooling in Saudi Arabia')
fig2.update_layout(xaxis_title="Life Expectancy",
                  yaxis_title="Avg Schooling Years")
st.subheader("4:  🇸🇦 Life Expectancy vs. Schooling: Saudi Arabia")
st.plotly_chart(fig2, use_container_width=True)

# 5: BMI vs Adult Mortality (Separate Charts)
df_saudi_bmi = df_filtered[df_filtered['Country'] == 'Saudi Arabia'][['Year','BMI','Adult_mortality']].sort_values(by="Year")

fig_bmi = px.line(df_saudi_bmi, x='Year', y='BMI', markers=True,
                  title='Saudi Arabia: Average BMI (2000–2015)')
fig_bmi.update_layout(yaxis_title="BMI", xaxis_title="Year")

fig_mort = px.line(df_saudi_bmi, x='Year', y='Adult_mortality', markers=True,
                   title='Saudi Arabia: Adult Mortality (Ages 15–60) (2000–2015)')
fig_mort.update_layout(yaxis_title="Adult Mortality (per 1,000)", xaxis_title="Year")

st.subheader("5:  🇸🇦 Rising BMI vs Adult Mortality in Saudi Arabia")
st.plotly_chart(fig_bmi, use_container_width=True)
