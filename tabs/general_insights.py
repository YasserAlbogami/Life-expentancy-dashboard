import streamlit as st
import plotly.express as px

def render(df_filtered):
    """Render stacked histogram of Life Expectancy by Development Status."""    
    
    avg_alcohol = df_filtered["Alcohol"].mean()
    avg_schooling = df_filtered["Schooling"].mean()

    # 
    latest_year = df_filtered["Year"].max()
    latest_df = df_filtered[df_filtered["Year"] == latest_year]

    
    developed_count = latest_df["Developed"].sum()
    developing_count = latest_df["Developing"].sum()

    #
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("🍺 Avg Alcohol Consumption", f"{avg_alcohol:.2f} L/year")
    col2.metric("🟢 Developed Countries (Last Year)", f"{int(developed_count)}")
    col3.metric("🟠 Developing Countries (Last Year)", f"{int(developing_count)}")
    col4.metric("🎓 Avg Schooling Years", f"{avg_schooling:.2f} years")



    # <-🔹 1: 📊 Life Expectancy Distribution by Development Status->


    # Map labels
    df_filtered['Developed_label'] = df_filtered['Developed'].map({0: 'Developing', 1: 'Developed'})

    # Custom colors (Developed = dark blue, Developing = light blue)

    color_map = {
    "Developed": "#2171b5",    # dark blue
    "Developing": "#9ecae1"    # light blue
}


    # Overlap the two distributions using barmode='overlay'
    fig = px.histogram(
        df_filtered,
        x="Life_expectancy",
        color="Developed_label",
        nbins=30,
        barmode="overlay",
        color_discrete_map=color_map,
        title="📊 Stacked Histogram of Life Expectancy by Developed Status"
    )

    # Calculate means
    mean_developed = df_filtered[df_filtered['Developed_label'] == 'Developed']['Life_expectancy'].mean()
    mean_developing = df_filtered[df_filtered['Developed_label'] == 'Developing']['Life_expectancy'].mean()

    fig.add_vline(
    x=mean_developed,
    line_dash="dash",
    line_color='rgb(0,32,96)',
    annotation_text=f"\t\t\tDeveloped Mean: {mean_developed:.2f}",
    annotation_position="top left"
)

    fig.add_vline(
        x=mean_developing,
        line_dash="dash",
        line_color='rgb(135,206,250)',
        annotation_text=f"Developing Mean: {mean_developing:.2f}",
        annotation_position="top right"
    )

    # Subheader and chart
    st.subheader("1:  📊 Life Expectancy Distribution by Development Status")
    st.plotly_chart(fig, use_container_width=True)


   # <-🔹 2: Life Expectancy Growth in the Middle East->

    # Filter for Middle East region (case-insensitive, robust to preprocessing)
    me_df = df_filtered[df_filtered['Region'].str.contains("Mid East", case=False, na=False)].copy()

    # Ensure sorting for correct pct_change calculation
    me_df = me_df.sort_values(['Country', 'Year'])

    # Calculate annual % change in life expectancy per country
    me_df['LE_pct_change'] = me_df.groupby('Country')['Life_expectancy'].pct_change() * 100

    # Compute average % change per country (ignoring NaNs from pct_change)
    avg_pct_change = (
        me_df.groupby('Country', as_index=False)['LE_pct_change']
        .mean()
        .sort_values('LE_pct_change', ascending=True)
    )

    # Plot: vertical bar chart of average annual % increase
    fig = px.bar(
        avg_pct_change,
        x="Country",
        y="LE_pct_change",
        text=avg_pct_change["LE_pct_change"].apply(lambda x: f"{x:.2f}%"),
        title="Average Annual % Change in Life Expectancy (Middle East)"
    )

    fig.update_traces(textposition='outside')
    fig.update_layout(
        xaxis_title="Country",
        yaxis_title="Avg Annual % Increase",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color="white"),
        margin=dict(t=30, b=40)
    )

    # Show header and chart
    st.subheader("📈 2: Life Expectancy Growth in the Middle East")
    st.plotly_chart(fig, use_container_width=True)


    # Insight 3: Average Life Expectancy Increases with Higher Levels of Schooling

    st.subheader("3: 📚 Average Life Expectancy by Years of Schooling")

    # Calculate the average Life Expectancy for each level of Schooling (in years)
    avg_life_exp = df_filtered.groupby('Schooling')['Life_expectancy'].mean().reset_index()

    # Plot the average Life Expectancy against years of Schooling
    fig = px.line(
        avg_life_exp,
        x='Schooling',
        y='Life_expectancy',
        markers=True,
        title="Average Life Expectancy vs. Years of Schooling",
        labels={'Schooling': 'Years of Schooling', 'Life_expectancy': 'Average Life Expectancy (Years)'},
        line_shape='linear'
    )

    fig.update_traces(line=dict(color='#4CB5AE'), marker=dict(color='#4CB5AE', size=8))
    fig.update_layout(
        xaxis_title="Years of Schooling",
        yaxis_title="Average Life Expectancy (Years)",
        margin=dict(t=40, b=40)
    )

    st.plotly_chart(fig, use_container_width=True)

    # Insight 4: Impact of New HIV Infections on Life Expectancy

    st.subheader("4:    🦠 Impact of New HIV Infections on Life Expectancy")

    fig = px.scatter(
        df_filtered,
        x="Incidents_HIV",
        y="Life_expectancy",
        color="Region",
        hover_name="Country",
        title="Life Expectancy vs. New HIV Infections (per 1,000 uninfected, ages 15–49)",
        labels={
            "Incidents_HIV": "New HIV Infections per 1,000 (ages 15–49)",
            "Life_expectancy": "Life Expectancy (Years)"
        }
    )
    fig.update_layout(margin=dict(t=40, b=40))
    st.plotly_chart(fig, use_container_width=True)

    # Insight 5: Impact of New HIV Infections on Life Expectancy


    fig = px.sunburst(
        df_filtered,
        path=["Region", "Country"],
        values="Adult_mortality",
        color="Adult_mortality",
        color_continuous_scale="Reds",
        hover_data=["Alcohol"],
        title="Adult Mortality Rate Across Regions and Countries"
    )

    st.subheader("5: 🌞 Adult Mortality Breakdown by Region and Country")

    st.plotly_chart(fig, use_container_width=True)
