# tabs/saudi_arabia.py

import streamlit as st
import plotly.express as px

def render(df_filtered):
    st.header("🇸🇦 Saudi Arabia: Focused Analysis")

    saudi_df = df_filtered[df_filtered["Country"] == "Saudi Arabia"]

    if saudi_df.empty:
        st.warning("⚠️ No data for Saudi Arabia with current filters.")
        return

    st.subheader("📄 Saudi Arabia Data Preview")
    st.dataframe(saudi_df)

    st.subheader("📊 Life Expectancy Over Time")
    if "Year" in saudi_df.columns and "Life expectancy" in saudi_df.columns:
        fig = px.line(
            saudi_df,
            x="Year", y="Life expectancy",
            title="Life Expectancy in Saudi Arabia Over Time"
        )
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("📈 Descriptive Statistics")
    
    describe_df = df_filtered.drop(columns=["Year"])
    
    st.write(describe_df.describe())
