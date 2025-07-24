import streamlit as st
from data import fillters  # updated filters.py

from tabs import (
    project_info,
    overall_insights,
    saudi_arabia,

)


#  Page title
st.set_page_config(page_title="🌐 Life Expectancy Explorer", layout="wide")
st.title("🌐 Life Expectancy Explorer")
st.markdown("Use the sidebar to filter data by country, region, and year.")

# Get filtered dataframe
df_filtered = fillters.get_filtered_df()

# Create tabs
tab0, tab1, tab2, tab3 = st.tabs([
    "📍 Why This Project",
    "📊 Project Info",
    "🌍 Overall Insights",
    "🇸🇦 Saudi Arabia",
])

# Render each tab content
with tab0:
    
    st.markdown("""
## 🎯 Problem Statement

Saudi Arabia’s **life expectancy** is around **75 years**, but the **healthy life expectancy (HALE)** — years lived in good health — is **5–7 years lower** than global leaders like **Japan** and **Switzerland**.

Despite increased healthcare spending, major challenges remain:

- 🍔 **High rates of obesity and diabetes**.
- 👩‍⚕️ **Shortage of healthcare workers**, especially in **primary care** and **elderly care**.
- 💸 **Spending efficiency gaps** — high costs but outcomes still need improvement.

---

### 🔍 Key Question

> **How can Saudi Arabia increase its healthy life years (healthspan)**  
> through smarter investments and evidence-based policies  
> that align with **Hevolution Foundation’s mission**?
""")



with tab1:
    project_info.render(df_filtered)

with tab2:
    overall_insights.render(df_filtered)

with tab3:
        # Force Saudi-only data, ignoring sidebar filters
    saudi_df = df_filtered.copy()
    saudi_df = saudi_df[saudi_df["Country"] == "Saudi Arabia"]
    saudi_arabia.render(saudi_df)