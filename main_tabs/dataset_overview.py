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

Each row represents a **country-year** pair (from **2000 to 2015**) and includes multiple indicators grouped by category:

---

### 🌍 General Information

| **Column**               | **Description**                                                  |
|--------------------------|------------------------------------------------------------------|
| `Country`                | Name of the country (e.g., Japan, Saudi Arabia).                 |
| `Region`                 | Geographic region of the country (e.g., Eastern Mediterranean).  |
| `Year`                   | Year of the observation (2000–2015).                             |
| `Population_mln`         | Total population in millions.                                    |
| `GDP_per_capita`         | GDP per capita in current USD.                                   |
| `Schooling`              | Average years of formal education for people aged 25+.           |
| `Developed`              | `1` if country is economically developed, else `0`.              |
| `Developing`             | `1` if country is economically developing, else `0`.             |

---

### ❤️ Health Outcomes

| **Column**         | **Description**                                                  |
|--------------------|------------------------------------------------------------------|
| `Life_expectancy`  | Average life expectancy (both genders) from 2000 to 2015.        |
| `Infant_deaths`    | Infant deaths per 1,000 population.                              |
| `0-5yrs_deaths`    | Deaths of children under 5 years per 1,000 population.           |
| `Adult_mortality`  | Deaths of adults (15–60 years) per 1,000 population.             |

---

### 🦠 Disease & Immunization

| **Column**     | **Description**                                                                 |
|----------------|---------------------------------------------------------------------------------|
| `Hepatitis_B`  | % coverage of Hepatitis B (HepB3) immunization among 1-year-olds.               |
| `Measles`      | % coverage of Measles (MCV1) immunization among 1-year-olds.                    |
| `Polio`        | % coverage of Polio (Pol3) immunization among 1-year-olds.                      |
| `Diphtheria`   | % coverage of Diphtheria (DTP3) immunization among 1-year-olds.                 |
| `Incidents_HIV`| New HIV infections per 1,000 population (ages 15–49).                           |

---

### 🧬 Lifestyle & Nutrition

| **Column**            | **Description**                                                                  |
|------------------------|----------------------------------------------------------------------------------|
| `Alcohol`              | Liters of pure alcohol consumed per capita (age 15+).                           |
| `BMI`                  | Average Body Mass Index (BMI = weight/height² in kg/m²).                        |
| `Thinness_10-19`       | % of adolescents aged 10–19 with BMI < -2 SD below the median.                  |
| `Thinness_5-9`         | % of children aged 5–9 with BMI < -2 SD below the median.                       |

---
""")
