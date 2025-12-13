# Customer Segmentation & RFM Analysis

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Library](https://img.shields.io/badge/Library-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-Completed-green)

## 📌 Project Overview
This project performs an end-to-end **Customer Segmentation** analysis using the **RFM (Recency, Frequency, Monetary)** technique and **K-Means Clustering**. 

By analyzing transactional data from an online retailer, the project identifies distinct customer behaviors to optimize marketing strategies, improve retention, and maximize customer lifetime value (CLV).

## 🚀 Key Features
* **Data Cleaning:** Handling null values, cancellations, and outliers to ensure data integrity.
* **Cohort Analysis:** Visualizing customer retention rates over time using heatmaps.
* **RFM Modeling:** Engineering Recency, Frequency, and Monetary features.
* **Statistical Preprocessing:** Log-transformation and scaling to normalize skewed sales data.
* **Unsupervised Learning:** Implementing **K-Means Clustering** with the Elbow Method to determine optimal segments.
* **Advanced Visualization:** Generating **Snake Plots** to interpret cluster attributes visually.

## 📊 Business Insights & Strategy
The analysis identified three distinct customer segments using K-Means (K=3):

| Segment | Characteristics | Recommended Strategy |
| :--- | :--- | :--- |
| **Champions** | High Spend, Recent Buyers, Frequent Visitors | **Loyalty Programs:** Offer exclusivity and early access. Avoid mass discounting. |
| **At-Risk** | Low Recency (Haven't bought recently), Low Frequency | **Retention Campaigns:** Automated "We Miss You" emails with time-bound coupons. |
| **Casual Buyers** | Low Frequency, Low Monetary Value | **Cross-Selling:** Recommend complementary items at checkout to boost basket size. |

## 🛠️ Technologies Used
* **Python:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (K-Means, StandardScaler)
* **Visualization:** Matplotlib, Seaborn
* **Data Source:** Online Retail Dataset (UCI Machine Learning Repository)

## ⚙️ Setup & Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/aditya-rudre/Customer-Segmentation-RFM.git](https://github.com/aditya-rudre/Customer-Segmentation-RFM.git)

Author: Aditya Rudre