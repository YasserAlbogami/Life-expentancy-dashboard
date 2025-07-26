# tabs/project_info.py
import streamlit as st
import plotly.express as px
import pandas as pd

def render(df_filtered):
    
    st.header("🗺️ Region-Based Analytics")

    
    # Show metrics for the last year using df_filtered
    latest_year = df_filtered["Year"].max()
    latest_df = df_filtered[df_filtered["Year"] == latest_year]

    total_population = latest_df["Population_mln"].sum()
    avg_gdp_per_capita = latest_df["GDP_per_capita"].mean()

    col1, col2 = st.columns(2)
    col1.metric("🌍 Total Population (mln, last year)", f"{total_population:,.2f}")
    col2.metric("💰 Average GDP per Capita (USD, last year)", f"{avg_gdp_per_capita:,.2f}")
    
    st.markdown("---")
    
    st.subheader("1:    📦 Life Expectancy Distribution by Region")

    # 1: Boxplot
    fig = px.box(
        df_filtered,
        x='Region',
        y='Life_expectancy',
        color='Region',
        title="Life Expectancy Distribution by Region",
        labels={'Life_expectancy': 'Life Expectancy (Years)'},
        points='outliers',  # Show only outliers (also can use 'all' or 'suspectedoutliers')
        template='plotly_white'
    )

    fig.update_layout(
        xaxis_title="Region",
        yaxis_title="Life Expectancy",
        showlegend=False,
        margin=dict(t=50, b=50)
    )

    st.plotly_chart(fig, use_container_width=True)
   

    # 2:

    fig = px.line(
    df_filtered.groupby(['Year', 'Region'])['BMI'].mean().reset_index().assign(Year=lambda d: d['Year'].astype(str)),
    x='Year',
    y='BMI',
    color='Region',
    title="📉 Average BMI Over Time by Region"
)
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="BMI",
        xaxis_type='category',
        legend_title="Region"
    )
    
    st.subheader("2:    🧬 Regional Trends in Average BMI Over Time")
    st.plotly_chart(fig, use_container_width=True)

    #  3:

    st.subheader("3:    🧬 Heatmap of Average 0-5 Years Deaths by Region and Status")

    heatmap_data = df_filtered.copy()

    heatmap_data['Status'] = heatmap_data.apply(
    lambda row: "Developed" if row['Developed'] == 1 else "Developing", axis=1
)    

    # Prepare the data
    heatmap_data = heatmap_data.groupby(['Region', 'Status'])['0-5yrs_deaths'].mean().reset_index()

    # Create density heatmap
    fig = px.density_heatmap(
        heatmap_data,
        x="Region",
        y="Status",
        z="0-5yrs_deaths",
        color_continuous_scale="YlGnBu",
        title="🧬 Heatmap of Average 0-5 Years Deaths by Region and Status",
        nbinsx=len(heatmap_data['Region'].unique())
    )

    st.plotly_chart(fig, use_container_width=True)

  
    
    
    
    # Insight 4: Life Expectancy Differences by Region and Economic Status

    st.subheader("4: 🌐 Life Expectancy Differences by Region and Economic Status")

    # Map 'Developed' column to readable status if not already present
    df_le = df_filtered.copy()
    df_le['Economy_status'] = df_le['Developed'].map({0: 'Developing', 1: 'Developed'})

    # Calculate mean life expectancy grouped by Region and Economy status
    mean_life_by_region_status = (
        df_le.groupby(['Region', 'Economy_status'])['Life_expectancy']
        .mean()
        .reset_index()
    )

    # Sort regions by mean life expectancy of Developing countries (for consistent order)
    developing_order = (
        mean_life_by_region_status[mean_life_by_region_status['Economy_status'] == 'Developing']
        .sort_values('Life_expectancy', ascending=False)['Region']
        .tolist()
    )

    # Plot grouped bar chart
    fig = px.bar(
        mean_life_by_region_status,
        x="Region",
        y="Life_expectancy",
        color="Economy_status",
        barmode="group",
        category_orders={"Region": developing_order, "Economy_status": ["Developing", "Developed"]},
        color_discrete_map={"Developing": "#6A9FB5", "Developed": "#4CB5AE"},
        text=mean_life_by_region_status["Life_expectancy"].round(1),
        title="Average Life Expectancy by Region and Economic Status",
        labels={"Life_expectancy": "Life Expectancy (Years)"}
    )

    fig.update_traces(textposition='outside')
    fig.update_layout(
        xaxis_title="Region",
        yaxis_title="Life Expectancy (Years)",
        legend_title="Economic Status",
        margin=dict(t=50, b=50),
        xaxis_tickangle=45
    )

    st.plotly_chart(fig, use_container_width=True)  


    # 5: Relationship Between Immunization Rates and Infant Deaths


    # Filter and average by region
    bubble_df = (
        df_filtered.groupby("Region")[["Polio", "Diphtheria", "Hepatitis_B", "Infant_deaths"]]
        .mean()
        .reset_index()
    )

    fig = px.scatter(
        bubble_df,
        x="Polio",
        y="Diphtheria",
        size="Infant_deaths",
        color="Region",
        hover_name="Region",
        size_max=60,
        text=bubble_df["Infant_deaths"].round(1),
        title="🧬 Bubble Chart: Infant Deaths vs Polio and Diphtheria Coverage by Region",
        labels={
            "Polio": "Polio Coverage (%)",
            "Diphtheria": "Diphtheria Coverage (%)",
            "Infant_deaths": "Infant Deaths"
        }
    )

    fig.update_traces(textposition="top center")

    fig.update_layout(
        xaxis=dict(range=[50, 100]),
        yaxis=dict(range=[50, 100]),
        margin=dict(t=50, b=50),
    )
    
    st.subheader("5: 🧬 Immunization Coverage and Its Impact on Infant Deaths")
    st.plotly_chart(fig, use_container_width=True)


