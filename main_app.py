import streamlit as st
from utils import apply_custom_style, add_logo_to_sidebar
from data import fillters
from main_tabs import (
    dataset_overview,
    preprocessing,
)
import pandas as pd
# Apply global style and logo
apply_custom_style()
add_logo_to_sidebar()

# Set page config
st.set_page_config(page_title="🧪 Project Overview", layout="wide")


df_filtered = pd.read_csv("data/Life-Expectancy-Data-Updated.csv")

# ---- Main Content ----
st.title("🧪 Life Expectancy Project Overview")
st.markdown(
    "A quick walkthrough of the motivation, data, and preprocessing steps behind the project.")

if st.button("📈 Open Dashboard"):
    st.switch_page("pages/Dashboard.py")

# Tabs
tab1, tab2, tab3 = st.tabs([
    "📌 Why This Project?",
    "📊 Dataset Overview",
    "🛠️ Preprocessing and Cleaning"
])


with tab1:
    st.markdown("""
## 📌 Problem Statement


### ❓ What challenge are we tackling?
🧬 **Life expectancy varies greatly** across countries and over time. These variations are shaped by complex interactions of health, economic, and social factors.

---

### 🌍 Why does it matter?
📉 Understanding the **broader context**—such as healthcare access, national development levels, and education—helps us uncover **why certain populations live longer** and healthier lives.

---

### 🔍 What's behind the issue?
🧠 At the core, disparities in life expectancy may be driven by factors like:
- 💉 **Immunization rates**
- 📊 **GDP per capita**
- 🏫 **Years of schooling**
- 🏥 **Access to medical services**

---

### 🎯 What do we want to achieve?
📌 Our goal is to perform a thoughtful **Exploratory Data Analysis (EDA)** to:
- Spot trends over time 📈  
- Compare countries and regions 🌐  
- Highlight key influencing factors 🔦  

---

### 💡 How will this help?
By extracting actionable insights, we can support:
- Better **policy planning** 🧾  
- Smarter **health interventions** 🛠️  
- More **equitable global health strategies** 🌱🌍  
- 🤖 **Create an AI model** that can **predict future life expectancy** based on current trends and indicators!

---
""")

    # Path from root

with tab2:
   dataset_overview.render(df_filtered)

with tab3:
    
    preprocessing.render(df_filtered)

# ---- Optional main page button ----
st.markdown("---")
