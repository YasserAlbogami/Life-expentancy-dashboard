# tabs/numerical_analysis.py
import streamlit as st
import plotly.express as px
import pandas as pd



def render(df_filtered):
    st.header("🌍 Numerical Analysis")

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


# 1   📊 Correlation with Life Expectancy


# Compute correlation matrix
    corr_matrix = df_filtered.corr(numeric_only=True)

    # Get correlations with Life_expectancy only
    life_corr = corr_matrix["Life_expectancy"].drop("Life_expectancy", errors="ignore")

    # Convert to DataFrame and sort ascending
    life_corr_df = life_corr.reset_index()
    life_corr_df.columns = ["Variable", "Correlation_with_Life_expectancy"]
    life_corr_df = life_corr_df.sort_values(by="Correlation_with_Life_expectancy", ascending=True)

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
        height=300,
        title="Correlation of Each Variable with Life Expectancy (Sorted)"
    )

    st.subheader("# 1   📊 Correlation with Life Expectancy (Sorted)")
    st.plotly_chart(fig, use_container_width=True)


    # --------------------------------

    st.subheader("2:    🔍 Top Correlated Features")

# Sort correlations
    # top positive and negative indices start from 1
    top_positive = life_corr_df.sort_values(
        "Correlation_with_Life_expectancy", ascending=False).head(3).reset_index(drop=True)
    top_negative = life_corr_df.sort_values(
        "Correlation_with_Life_expectancy").head(3).reset_index(drop=True)

    top_positive.index += 1
    top_negative.index += 1

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**🔼 Top Positive Correlations**")
        st.table(top_positive)

    with col2:
        st.markdown("**🔽 Top Negative Correlations**")
        st.table(top_negative)

    # --------------------------------
    
    st.subheader("3:    📉 Impact of Youth Thinness on Life Expectancy")

    st.markdown("""
    Investigating the relation between thinness among youth (ages 5–9 and 10–19) and life expectancy.
    """)
    
    fig = px.scatter_3d(
        df_filtered,
        x="Thinness_5-9",
        y="Thinness_10-19",
        z="Life_expectancy",
        color="Region" if "Region" in df_filtered.columns else None,
        title="3D Relationship: Thinness (5-9, 10-19) vs Life Expectancy",
        labels={
            "Thinness_5-9": "Thinness (Age 5-9)",
            "Thinness_10-19": "Thinness (Age 10-19)",
            "Life_expectancy": "Life Expectancy"
        },
        height=600
    )
    st.plotly_chart(fig, use_container_width=True)

    # --------------------------------

    st.subheader("4: 🍷 Alcohol Consumption vs Life Expectancy")

    st.markdown("""
    A simple scatter plot showing the relationship between **life expectancy** and **alcohol consumption** across all countries.
    """)

    # Filter necessary columns and drop missing values
    df_scatter = df_filtered[["Life_expectancy", "Alcohol"]].dropna()

    fig = px.scatter(
        df_scatter,
        x="Life_expectancy",
        y="Alcohol",
        color_discrete_sequence=["#1f77b4"],  # Simple blue color
        title="Alcohol Consumption vs Life Expectancy",
        labels={
            "Life_expectancy": "Life Expectancy (years)",
            "Alcohol": "Alcohol Consumption (liters per capita)"
        },
        height=500,
        opacity=0.7
    )

    st.plotly_chart(fig, use_container_width=True)

# --------------------------------

    st.subheader("5:    📦 BMI and Life Expectancy")

    st.markdown("""
    This box plot visualizes the distribution of **Life Expectancy** across different ranges of **BMI**.
    """)

    # Optionally: Create BMI categories (bins)
    df_filtered["BMI_Category"] = pd.cut(
        df_filtered["BMI"],
        bins=[0, 18.5, 25, 30, 35, 100],
        labels=["Underweight", "Normal", "Overweight", "Obese I", "Obese II+"]
    )

    # Create box plot
    fig = px.box(
        df_filtered,
        x="BMI_Category",
        y="Life_expectancy",
        color="BMI_Category",
        category_orders={"BMI_Category": ["Underweight", "Normal", "Overweight", "Obese I", "Obese II+"]},
        title="Life Expectancy Distribution by BMI Category",
        labels={"Life_expectancy": "Life Expectancy (years)", "BMI_Category": "BMI Category"},
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)
