# ⚡ Energy Demand Forecasting for Nigeria  

## 📖 Project Overview  
Reliable energy planning requires accurate forecasting of electricity demand. In Nigeria, **inadequate forecasting and supply shortfalls** contribute to chronic blackouts, suppressed demand, and stalled development.  

This project builds a **machine learning model** using national time-series data (2016) of **suppressed** and **unsuppressed demand** to forecast daily electricity demand. The aim is to demonstrate how data-driven forecasting can inform **renewable system design** (e.g., sizing solar, biogas, and storage) and bridge the gap between supply and actual community needs.  

---

## 🎯 Objectives  
1. Explore patterns in Nigeria’s hourly energy demand.  
2. Build ML models to forecast future demand.  
3. Compare model performance against a **naïve baseline** ("yesterday = today").  
4. Interpret results to support planning of decentralized, low-cost energy systems.  

---

## 🔬 Methodology  

### 1. Data  
- Source: Hourly national electricity demand (2016).  
- Columns:  
  - **DateTime** (hourly)  
  - **Year**  
  - **Quarter**  
  - **Unsuppressed Demand (MW)** → *true electricity need if supply were unlimited*  
  - **Suppressed Demand (MW)** → *what was actually delivered, constrained by supply*  

### 2. Preprocessing  
- Convert timestamps, set chronological ordering.  
- Feature engineering:  
  - Lag features (previous hour, yesterday same hour).  
  - Rolling means (7-day, 24-hour).  
  - Seasonal patterns (quarter, month, weekday).  

### 3. Modeling  
- Models:  
  - Linear Regression  
  - Decision Tree  
  - Random Forest  
- Baseline: "yesterday’s demand at the same hour = today’s prediction".  

### 4. Evaluation  
- Metric: **Mean Absolute Error (MAE)**.  
- Compare ML models vs baseline.  
- Example results (MAE):  
  - Linear Regression → 124 MW  
  - Decision Tree → 170 MW  
  - Random Forest → 105 MW  

---

## 📊 Results & Insights  
- ML models consistently **outperformed the baseline**, showing predictive power beyond simple historical averages.  
- Random Forest gave the **lowest error**, capturing non-linear demand patterns.  
- Peak national demand exceeded **6,900 MW**, while average generation is ~3,900 MW → showing a significant **supply-demand gap**.  
- Forecasting models can help:  
  - Size hybrid microgrids for rural communities.  
  - Plan investments in renewable systems (solar, biogas, storage).  
  - Reduce suppressed demand by better anticipating true needs.  

---

## 🛠 Tools & Libraries  
- **Python** → Pandas, NumPy, Scikit-learn, Matplotlib  
- **Excel/CSV** → Data exploration and cleaning  

---

## 🌍 Impact  
- Highlights the **mismatch between demand and supply** in Nigeria.  
- Demonstrates how **AI/ML can improve energy planning**.  
- Provides a foundation for **scaling down forecasts** to communities, enabling the design of realistic renewable energy systems.  

---

