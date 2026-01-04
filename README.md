# 🎯 Customer Segmentation & RFM Analysis

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Power BI](https://img.shields.io/badge/Power_BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange)

## 📌 Project Overview
This project performs an end-to-end **Customer Segmentation** analysis using the **RFM (Recency, Frequency, Monetary)** technique and **K-Means Clustering**.

By analyzing transactional data, the project identifies distinct customer personas ("Champions", "At Risk") and enables marketing teams to download targeted lists via an interactive **Power BI Dashboard**.

## 🚀 Key Features
* **Data Engineering:** Python script to clean nulls, handle cancellations, and aggregate transaction logs into customer-level RFM features.
* **Unsupervised Learning:** Implemented **K-Means Clustering** (K=3) with Log-transformation to handle skewed monetary data.
* **Cohort Analysis:** Pre-calculated retention rates in Python to visualize drop-off trends in Power BI.
* **Interactive Reporting (Power BI):**
    * **Persona Scatter Plot:** Log-scale visualization of Frequency vs. Recency to spot clusters.
    * **Retention Matrix:** Conditional formatting to track user retention over 12 months.
    * **Actionable Targeting:** A filterable table allowing marketers to export "At Risk" customer lists for email campaigns.

## 📊 Business Insights & Strategy
| Segment | Characteristics | Recommended Strategy |
| :--- | :--- | :--- |
| **Champions** | High Spend, Recent Buyers | **Loyalty Programs:** Offer exclusivity and early access. |
| **At-Risk** | High Past Spend, Low Recency | **Win-Back Campaigns:** Automated emails with time-bound coupons. |
| **Casual Buyers** | Low Frequency, Low Spend | **Cross-Selling:** Recommend complementary items to boost basket size. |

## 🛠️ Technologies Used
<<<<<<< HEAD
* **Python:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (K-Means, StandardScaler)
* **Visualization:** Matplotlib, Seaborn
* **Data Source:** [Online Retail Dataset - UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/352/online+retail) 
=======
* **Backend:** Python (Pandas, NumPy, Scikit-Learn) for ETL and Modeling.
* **Frontend:** Microsoft Power BI for Dashboarding and Data Storytelling.
* **Data Source:** Online Retail Dataset (UCI Machine Learning Repository)
>>>>>>> 4d202bc (migration from streamlit to power bi)

## ⚙️ Setup & Installation
1. **Generate Data:**
   ```bash
<<<<<<< HEAD
   git clone [https://github.com/aditya-rudre/Customer-Segmentation-RFM.git](https://github.com/aditya-rudre/Customer-Segmentation-RFM.git)

Author: Aditya Rudre
=======
   pip install -r requirements.txt
   python generate_customer_data.py
>>>>>>> 4d202bc (migration from streamlit to power bi)
