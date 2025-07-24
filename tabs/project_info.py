# tabs/project_info.py

import streamlit as st

def render(df_filtered):
    st.header("📌 Dataset Description")
    st.markdown("""
    This dataset explores global life expectancy trends and health indicators from 2000 to 2015.

    - **Source**: WHO & United Nations
    - **Features**: Life expectancy, GDP, schooling, immunization rates, etc.
    - **Goal**: Understand the factors affecting life expectancy around the world.
    """)

    st.subheader("📂 Filtered Dataset Preview")
    st.dataframe(df_filtered.head())

    st.subheader("📈 Dataset Info")
    st.text(f"{df_filtered.shape[0]} rows × {df_filtered.shape[1]} columns")
    st.write(df_filtered.dtypes)


    describe_df = df_filtered.drop(columns=["Year"])
    
    

    st.subheader("📊 Descriptive Statistics")
    st.write(describe_df.describe())


    st.markdown("""
## 🧾 Dataset Column Descriptions

Each row represents a country in a specific year and includes demographic, economic, and health-related indicators.

---

### 🌍 General Information

| **Column**         | **Description**                                                  |
|--------------------|------------------------------------------------------------------|
| `Country`          | Name of the country (e.g., Saudi Arabia, Japan).                |
| `Region`           | Geographic region the country belongs to.                       |
| `Year`             | The year the data was recorded.                                 |
| `Population_mln`   | Population size in millions.                                     |
| `GDP_per_capita`   | Gross Domestic Product per person (in USD).                     |
| `Schooling`        | Average number of years of schooling.                           |
| `Economy_status_Developed` | 1 if the country is classified as developed, else 0.     |
| `Economy_status_Developing` | 1 if the country is classified as developing, else 0.   |

---

### ❤️ Health Outcomes

| **Column**         | **Description**                                                  |
|--------------------|------------------------------------------------------------------|
| `Life_expectancy`  | Average number of years a person is expected to live.           |
| `Infant_deaths`    | Number of infant deaths per 1,000 live births.                  |
| `Under_five_deaths`| Number of deaths under age 5 per 1,000 live births.             |
| `Adult_mortality`  | Probability of dying between 15 and 60 years per 1,000 adults.  |

---

### 🦠 Disease & Immunization

| **Column**         | **Description**                                                  |
|--------------------|------------------------------------------------------------------|
| `Hepatitis_B`      | Percentage of children vaccinated against Hepatitis B.          |
| `Measles`          | Number of reported measles cases per year.                      |
| `Polio`            | Percentage of children vaccinated against Polio.                |
| `Diphtheria`       | Percentage of children vaccinated against Diphtheria.           |
| `Incidents_HIV`    | New HIV cases per 1,000 people aged 15–49.                      |

---

### 🧬 Lifestyle & Nutrition

| **Column**                   | **Description**                                                  |
|------------------------------|------------------------------------------------------------------|
| `Alcohol_consumption`        | Average alcohol intake (liters per person per year).             |
| `BMI`                        | Average Body Mass Index of the population.                       |
| `Thinness_ten_nineteen_years`| Percentage of thin adolescents aged 10–19.                       |
| `Thinness_five_nine_years`   | Percentage of thin children aged 5–9.                            |
""")
