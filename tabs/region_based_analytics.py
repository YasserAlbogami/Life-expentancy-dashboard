# tabs/project_info.py
import streamlit as st
import plotly.express as px
import pandas as pd

def render(df_filtered):
    
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

    st.subheader("2:    🧬 Regional Trends in Average BMI Over Time")



    fig = px.line(
        df_filtered.groupby(['Year', 'Region'])['BMI'].mean().reset_index(),
        x='Year',
        y='BMI',
        color='Region',
        title="📉 Average BMI Over Time by Region"
    )
    st.plotly_chart(fig, use_container_width=True)

    #  3:

    st.subheader("3:    🌍 Average BMI by Region and Development Status")


    heatmap_data = df_filtered.copy()

    heatmap_data['Status'] = heatmap_data.apply(
    lambda row: "Developed" if row['Developed'] == 1 else "Developing", axis=1
)    

    # Prepare the data
    heatmap_data = heatmap_data.groupby(['Region', 'Status'])['BMI'].mean().reset_index()

    # Create density heatmap
    fig = px.density_heatmap(
        heatmap_data,
        x="Region",
        y="Status",
        z="BMI",
        color_continuous_scale="YlGnBu",
        title="🧬 Heatmap of Average BMI by Region and Status",
        nbinsx=len(heatmap_data['Region'].unique())
    )

    st.plotly_chart(fig, use_container_width=True)

    # BMI category explanation table
    st.markdown("#### 🧾 BMI Classification Table")
    st.dataframe({
        "BMI Category": ["Underweight", "Normal", "Overweight", "Obese"],
        "BMI Range": ["< 18.5", "18.5 – 24.9", "25 – 29.9", "30+"]
    })

    # Insight 4: Life Expectancy Differences by Region and Economic Status

    st.header("4: 🌐 Life Expectancy Differences by Region and Economic Status")

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