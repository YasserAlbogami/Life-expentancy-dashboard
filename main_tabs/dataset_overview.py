import streamlit as st
import pandas as pd

def render(df_filtered: pd.DataFrame):
    st.header("📌 Dataset Overview")

    # 🔹 Add 4 summary columns
    col1, col2, col3, col4 = st.columns([1, 1, 1, 2])  # Give col4 extra space for chart


    # Column 1: Number of Countries
    num_countries = df_filtered["Country"].nunique()
    col1.metric("🌍 Number of Countries", f"{num_countries}")

    # Column 2: Average Adult Mortality
    avg_mortality = df_filtered["Adult_mortality"].mean()
    col2.metric("⚰️ Avg. Adult Mortality", f"{avg_mortality:.0f}")

    # Column 3: Average Life Expectancy
    avg_life = df_filtered["BMI"].mean()
    col3.metric("📈 Avg. BMI", f"{avg_life:.2f}")

    # Column 4: Progress View as mini table
    with col4:
        st.markdown("📌 **Progress View** (Average by Country)")

        # Calculate average life expectancy per country across all years
        df_avg = df_filtered.groupby("Country", as_index=False)["Life_expectancy"].mean()

        if not df_avg.empty:
            # Sort by life expectancy
            df_bar = df_avg.sort_values(by="Life_expectancy", ascending=False).reset_index(drop=True)

            # Normalize to max
            max_life = df_bar["Life_expectancy"].max()
            df_bar["Progress"] = df_bar["Life_expectancy"] / max_life

            # Show as compact progress table
            st.dataframe(
                df_bar[["Country", "Life_expectancy", "Progress"]],
                column_config={
                    "Life_expectancy": st.column_config.NumberColumn("Life Expectancy (yrs)", format="%.1f"),
                    "Progress": st.column_config.ProgressColumn("Relative to Max", format="%.0f%%"),
                },
                use_container_width=True,
                height=300
            )
        else:
            st.info("No data available.")

    st.markdown("---")

    st.markdown("""
    This dataset, sourced from the **World Health Organization (WHO)** and the **United Nations**, provides an in-depth view of global **life expectancy** trends from **2000 to 2015**.

    It contains a diverse range of features related to:
    - 🌍 **Country demographics**
    - 💰 **Economic indicators**
    - 🏥 **Health status**
    - 💉 **Vaccination coverage**
    - 🧬 **Lifestyle and nutrition**

    **Objective**: To explore how various social, economic, and health factors correlate with **life expectancy** around the world.
    """)

    st.subheader("📂 Filtered Dataset Preview")

    preview_df = df_filtered.head().reset_index(drop=True)
    preview_df.index = preview_df.index + 1
    preview_df.index.name = "Index"
    st.dataframe(preview_df)

    st.subheader("📈 Dataset Shape & Data Types")
    st.markdown(f"""
    - 🔢 **Rows**: `{df_filtered.shape[0]:,}`
    - 📊 **Columns**: `{df_filtered.shape[1]}`
    """)
    st.write(df_filtered.dtypes)

    describe_df = df_filtered.drop(columns=["Year"])
    st.subheader("📊 Descriptive Statistics")
    st.dataframe(describe_df.describe().style.format(precision=2))

    
    st.markdown("---")

    st.markdown("""

## 🧾 Dataset Column Descriptions

Each row represents a **country-year** pair and includes multiple indicators grouped by category:

---

### 🌍 General Information

| **Column**               | **Description**                                                  |
|--------------------------|------------------------------------------------------------------|
| `Country`                | Name of the country (e.g., Japan, Saudi Arabia).                 |
| `Region`                 | Geographic region of the country (e.g., Eastern Mediterranean).  |
| `Year`                   | Year of the observation.                                         |
| `Population_mln`         | Population size in millions.                                     |
| `GDP_per_capita`         | Gross Domestic Product per person in USD.                        |
| `Schooling`              | Average number of years of schooling.                            |
| `Economy_status_Developed`   | `1` if country is developed, else `0`.                     |
| `Economy_status_Developing` | `1` if country is developing, else `0`.                   |

---

### ❤️ Health Outcomes

| **Column**         | **Description**                                                  |
|--------------------|------------------------------------------------------------------|
| `Life_expectancy`  | Average number of years a person is expected to live.           |
| `Infant_deaths`    | Number of deaths of infants under 1 year per 1,000 live births. |
| `Under_five_deaths`| Number of deaths of children under 5 years per 1,000 births.    |
| `Adult_mortality`  | Probability of dying between ages 15–60 (per 1,000 adults).     |

---

### 🦠 Disease & Immunization

| **Column**     | **Description**                                                      |
|----------------|----------------------------------------------------------------------|
| `Hepatitis_B`  | % of children vaccinated against Hepatitis B.                        |
| `Measles`      | Number of measles cases reported annually.                           |
| `Polio`        | % of children vaccinated against Polio.                              |
| `Diphtheria`   | % of children vaccinated against Diphtheria.                         |
| `Incidents_HIV`| New HIV infections per 1,000 uninfected population (ages 15–49).     |

---

### 🧬 Lifestyle & Nutrition

| **Column**                   | **Description**                                                  |
|------------------------------|------------------------------------------------------------------|
| `Alcohol_consumption`        | Liters of pure alcohol consumed per person per year.             |
| `BMI`                        | Average Body Mass Index across the population.                   |
| `Thinness_ten_nineteen_years`| % of thin adolescents aged 10–19.                                |
| `Thinness_five_nine_years`   | % of thin children aged 5–9.                                     |

---
    """)
