# tabs/overall_insights.py

import streamlit as st
import plotly.express as px
import pandas as pd


def render(df_filtered):
    st.header("🌍 Overall Insights")

    if df_filtered.empty:
        st.warning("No data available for the selected filters.")
        return

    # ✅ Add 3 summary columns based on filtered data
    col1, col2, col3 = st.columns(3)

    # Column 1: Average Life Expectancy
    avg_life = df_filtered["Life_expectancy"].mean()
    col1.metric("📈 Avg. Life Expectancy", f"{avg_life:.2f} years")

    # Column 2: Number of Countries
    num_countries = df_filtered["Country"].nunique()
    col2.metric("🌎 Number of Countries", num_countries)

    # Column 3: Are we gaining or losing?
    yearly_avg = df_filtered.groupby("Year")["Life_expectancy"].mean()
    if len(yearly_avg) >= 2:
        trend_direction = yearly_avg.diff().dropna()
        net_change = trend_direction.sum()
        status = "⬆️ Increasing" if net_change > 0 else "⬇️ Decreasing"
        col3.metric("📉 Trend Direction of Life Expectancy",
                    status, f"{net_change:.2f} years")
    else:
        col3.metric("📉 Trend Direction of Life Expectancy ",
                    "Not enough data", "-")

    st.markdown("This section shows insights based on the current filters.")

    st.markdown(
        "## 📊 Insight 1: Correlation with Life Expectancy (Plotly Heatmap)")

# Compute correlation matrix
    corr_matrix = df_filtered.corr(numeric_only=True)

    # Get correlations with Life_expectancy only
    life_corr = corr_matrix["Life_expectancy"].drop(
        "Life_expectancy", errors="ignore")

    # Convert to DataFrame for Plotly
    life_corr_df = life_corr.reset_index()
    life_corr_df.columns = ["Variable", "Correlation_with_Life_expectancy"]

    st.table(life_corr_df)

    # Create heatmap
    fig = px.imshow(
        [life_corr_df["Correlation_with_Life_expectancy"]],
        labels=dict(x="Variable", y="", color="Correlation"),
        x=life_corr_df["Variable"],
        y=["Life_expectancy"],
        color_continuous_scale="RdBu",
        zmin=-1, zmax=1,
        text_auto=".2f"
    )

    fig.update_layout(
        height=300, title="Correlation of Each Variable with Life Expectancy")

    st.plotly_chart(fig, use_container_width=True)

    # --------------------------------

    st.markdown("## 🌍 Insight 2: Global Trend in Life Expectancy")

# Calculate the average Life Expectancy per year from the filtered data

    trend = df_filtered.groupby("Year")["Life_expectancy"].mean().reset_index()

    # Create interactive line chart
    fig = px.line(
        trend,
        x="Year",
        y="Life_expectancy",
        markers=True,
        title="Average Global Life Expectancy Over Time",
        labels={"Life_expectancy": "Avg. Life Expectancy", "Year": "Year"},
    )

    fig.update_traces(line=dict(color="lightblue"))
    fig.update_layout(xaxis_title="Year",
                      yaxis_title="Life Expectancy (Years)")

    # Show chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # --------------------------------

    # --------------------------------

    st.markdown("## 🇸🇦 Insight 3: Saudi Arabia vs. Global Life Expectancy")

# Global average per year
    global_trend = df_filtered.groupby(
        'Year')['Life_expectancy'].mean().reset_index()
    global_trend['Country'] = 'Global Average'

    # Saudi Arabia data
    saudi_trend = df_filtered[df_filtered['Country'] ==
                              'Saudi Arabia'][['Year', 'Life_expectancy']].copy()

    saudi_trend['Country'] = 'Saudi Arabia'

    saudi_trend.sort_values(by="Year", ascending=True, inplace=True)

    # Combine both dataframes
    compare = pd.concat([global_trend, saudi_trend], ignore_index=True)

    # Plot
    fig = px.line(
        compare,
        x='Year',
        y='Life_expectancy',
        color='Country',
        title="Life Expectancy: Saudi Arabia vs Global Average )",
        markers=True
    )

    fig.update_layout(
        yaxis_title="Life Expectancy (Years)",
        xaxis_title="Year",
        xaxis_type='category',
        legend_title="Country"
    )

    st.plotly_chart(fig, use_container_width=True)