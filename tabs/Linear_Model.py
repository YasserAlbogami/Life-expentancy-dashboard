# tabs/saudi_arabia.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

def render(df_filtered: pd.DataFrame):
    st.header("Linear Regression Model: Predicting Life Expectancy")

    # Aggregate data to get average life expectancy per year
    global_trend = df_filtered.groupby("Year")["Life_expectancy"].mean().reset_index()

    year_min, year_max = int(global_trend["Year"].min()), int(global_trend["Year"].max())

    # Select a single year for prediction (you can change to a range if needed)
    selected_year = st.slider(
        "Select a year to predict life expectancy",
        min_value=year_min,
        max_value=year_max + 10,  # Allow predicting future years beyond available data
        value=year_max,
        step=1
    )

    # Build regression model using available historical data
    X = global_trend["Year"].values.reshape(-1, 1)
    y = global_trend["Life_expectancy"].values

    model = LinearRegression()
    model.fit(X, y)

    # Predict life expectancy for the selected year (including future years)
    predicted_life_exp = model.predict(np.array([[selected_year]]))[0]

    # Calculate training error metrics
    y_pred_train = model.predict(X)
    mse = mean_squared_error(y, y_pred_train)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y, y_pred_train)
    r2 = model.score(X, y)

    # Prepare data for plotting regression line from earliest year to selected year
    years_extended = np.arange(year_min, selected_year + 1).reshape(-1, 1)
    life_pred_extended = model.predict(years_extended)

    # Plot actual data points, regression line, and prediction point
    fig = go.Figure()

    # Actual life expectancy data points
    fig.add_trace(go.Scatter(
        x=global_trend["Year"],
        y=global_trend["Life_expectancy"],
        mode='markers',
        name="Actual Data",
        marker=dict(color="blue")
    ))

    # Regression line
    fig.add_trace(go.Scatter(
        x=years_extended.flatten(),
        y=life_pred_extended,
        mode='lines',
        name="Regression Line",
        line=dict(color='red')
    ))

    # Prediction point for the selected year
    fig.add_trace(go.Scatter(
        x=[selected_year],
        y=[predicted_life_exp],
        mode='markers+text',
        name="Prediction",
        marker=dict(color='green', size=12, symbol='star'),
        text=[f"{predicted_life_exp:.2f}"],
        textposition="top center"
    ))

    fig.update_layout(
        title=f"Life Expectancy Regression and Prediction for Year {selected_year}",
        xaxis_title="Year",
        yaxis_title="Life Expectancy (Years)",
        template="plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)

    # Show regression summary and error metrics
    st.markdown(f"""
    ### Regression Summary
    - Slope: **{model.coef_[0]:.3f}** (Increase in life expectancy per year)
    - Intercept: **{model.intercept_:.2f}**
    - Predicted Life Expectancy for **{selected_year}**: **{predicted_life_exp:.2f}** years

    ### Model Evaluation on Training Data
    - Mean Squared Error (MSE): **{mse:.3f}**
    - Root Mean Squared Error (RMSE): **{rmse:.3f}**
    - Mean Absolute Error (MAE): **{mae:.3f}**
    - R² Score: **{r2:.3f}**
    """)
