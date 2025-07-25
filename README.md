# Life Expectancy Dashboard

Welcome to the Life Expectancy Dashboard!  
This project provides an interactive Streamlit dashboard for exploring global life expectancy data, health indicators, and trends across countries and regions.

---

## 🧭 Project Overview

The dashboard leverages a rich dataset comprising country-year pairs, offering insights into:

- Life expectancy metrics
- Health outcomes & disease statistics
- Lifestyle & nutrition indicators
- Socioeconomic and schooling factors

**Tech Stack:**  
- Python, Streamlit, Pandas, Plotly  
- Directory structure:  
  - `main_app.py` (main entry point)
  - `pages/` (dashboard page)
  - `main_tabs/` (project overview tabs: motivation, dataset, preprocessing)
  - `tabs/` (dashboard analysis tabs)
  - `data/` (CSV datasets)

---

## 🚀 How to Run (Step-by-Step for Instructors)

### 1. Clone the Repository

```bash
git clone https://github.com/YasserAlbogami/Life-expentancy-dashboard.git
cd Life-expentancy-dashboard
```

### 2. Set Up Python Environment

Recommended: Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Dashboard

Start the main app:

```bash
streamlit run main_app.py
```

---

## 🏗️ Architecture: Tabs & Navigation

### Entry Point: `main_app.py`

- **Purpose:** Landing page and project overview.
- **Tabs:**
  1. **Why This Project?**  
     - Explains the motivation and problem statement.
  2. **Dataset Overview**  
     - Shows dataset summary, descriptive stats, and column descriptions.
  3. **Preprocessing and Cleaning**  
     - Details data cleaning and preparation steps.

- **Button:**  
  - 📈 **Open Dashboard** — navigates to the main dashboard (`pages/Dashboard.py`).

---

### Dashboard: `pages/Dashboard.py`

- **Sidebar:** Filter by country, region, year.
- **Tabs:**  
  1. **General Insights** (`tabs/general_insights.py`)  
     - Distribution by development status  
     - Life expectancy growth in Middle East  
     - Impact of schooling, HIV, and adult mortality  
  2. **Region-Based Analytics** (`tabs/region_based_analytics.py`)  
     - BMI trends by region  
     - Heatmaps of BMI by region/status  
     - Regional comparisons  
  3. **Numerical Analysis & Comparison** (`tabs/overall_insights.py`)  
     - Overall life expectancy stats  
     - Country count  
     - Trend direction  
     - Correlation with health variables  
     - Saudi Arabia vs. global comparison  
  4. **Saudi Arabia** (`tabs/saudi_arabia.py`)  
     - Focused analysis for Saudi Arabia (filters forced)

---

### Data & Analysis

- **main_tabs/dataset_overview.py:**  
  - Dataset stats, summary metrics, progress table by country
  - Full column descriptions:
    - Country, Region, Year, Population, GDP, Schooling, Economy status, Life expectancy, Infant deaths, Adult mortality, Immunization rates, Disease stats, Lifestyle indicators

- **tabs/** (`general_insights.py`, `region_based_analytics.py`, `overall_insights.py`, `saudi_arabia.py`):  
  - Each file holds a `.render(df_filtered)` function for Streamlit tab content
  - Visualizations: Histograms, line charts, heatmaps, progress columns, sunburst charts

---

## 📂 Directory Structure

```
Life-expentancy-dashboard/
├── main_app.py              # Main entry point
├── pages/
│   └── Dashboard.py         # Main dashboard UI
├── main_tabs/
│   ├── dataset_overview.py  # Dataset stats & overview tab
│   └── preprocessing.py     # Preprocessing steps tab
├── tabs/
│   ├── general_insights.py
│   ├── region_based_analytics.py
│   ├── overall_insights.py
│   └── saudi_arabia.py
├── data/
│   └── Life-Expectancy-Data-Updated.csv
├── requirements.txt
└── README.md
```

---

## 🙋 Contributing

Pull requests and suggestions are welcome!

## 📜 License

MIT

---

**For instructors:**  
- Start with `main_app.py` for project walkthrough and context.  
- Use the "Open Dashboard" button to launch the full interactive dashboard.  
- Explore each tab for specialized health insights and analytics.
