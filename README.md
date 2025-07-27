# Life Expectancy Dashboard

Welcome to the Life Expectancy Dashboard repository!

This project provides an interactive dashboard—built with Streamlit—for analyzing and visualizing life expectancy data, health, and socioeconomic indicators across countries and years.

---

## 🚀 Quick Start

1. **Clone the repository**
    ```bash
    git clone https://github.com/YasserAlbogami/Life-expentancy-dashboard.git
    cd Life-expentancy-dashboard
    ```

2. **Create and activate a virtual environment (optional but recommended)**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app**
    ```bash
    streamlit run Main_Page.py
    ```

---

## 📁 Project Structure

```
Life-expentancy-dashboard/
│
├── .streamlit/                # Streamlit configuration files
├── data/                      # Datasets (CSV files)
├── main_tabs/                 # Tabs for project overview, dataset, preprocessing
├── pages/                     # Dashboard main page(s)
├── tabs/                      # Analysis and visualization tabs for dashboard
│
├── .gitignore
├── .python-version
├── layout_set_logo.png        # Logo for dashboard
├── Main_Page.py               # Streamlit main entry point
├── pyproject.toml
├── README.md
├── requirements.txt
├── uv.lock
```

### Key Files

- **Main_Page.py**: The main entry point for running the dashboard app.
- **README.md**: This file.
- **requirements.txt**: Python dependencies for the project.
- **layout_set_logo.png**: Custom logo for dashboard UI.
- **data/**: Contains the life expectancy dataset(s).
- **main_tabs/**: Project introduction, dataset summary, and preprocessing steps.
- **pages/**: Main dashboard interface.
- **tabs/**: Contains code for individual analysis tabs in the dashboard.

---

## 🧭 Description

- Visualize and analyze life expectancy metrics, health outcomes, and related features by country, region, and year.
- Navigate through multiple tabs:
    - **Project Overview**
    - **Dataset Overview**
    - **Preprocessing and Cleaning**
    - **Dashboard** (with sub-tabs for various analyses)

- Filter by country, region, year, and more.
- Compare trends and correlations between countries and variables.
- Focused analysis for Saudi Arabia available in a dedicated tab.

---

## 🛠️ Requirements

- Python 3.8+
- All Python dependencies listed in `requirements.txt`

---

## 🤝 Contributions

Contributions, issues, and feature requests are welcome!

---

_Last updated to reflect commit "4TH REQUIREMENTS!" — directory and file names are accurate as of the latest project structure._
