import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import os

# ---------------------------------------------------------
# 1. Load Data (Excel Support Added)
# ---------------------------------------------------------
print("Loading data from 'Online Retail.xlsx'...")
# Ensure openpyxl is installed: pip install openpyxl
df = pd.read_excel('Online Retail.xlsx')

print(f"Data Loaded. Rows: {len(df)}")

# ---------------------------------------------------------
# 2. Data Cleaning & Feature Engineering
# ---------------------------------------------------------
# Drop rows without CustomerID
df = df.dropna(subset=['CustomerID'])

# Calculate Total Amount
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']

# Remove Cancellations (Invoices starting with 'C')
# This is crucial to prevent negative numbers
df = df[~df['InvoiceNo'].astype(str).str.contains('C')]

# Ensure InvoiceDate is datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# ---------------------------------------------------------
# 3. RFM Calculation
# ---------------------------------------------------------
print("Calculating RFM values...")
snapshot_date = df['InvoiceDate'].max() + pd.to_timedelta(1, 'D')

rfm = df.groupby(['CustomerID']).agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days, # Recency
    'InvoiceNo': 'nunique',                                  # Frequency (Count unique orders)
    'TotalAmount': 'sum'                                     # Monetary
}).reset_index()

rfm.rename(columns={
    'InvoiceDate': 'Recency',
    'InvoiceNo': 'Frequency',
    'TotalAmount': 'Monetary'
}, inplace=True)

# CRITICAL FIX: Filter out zero or negative Monetary values
# Log of negative numbers is impossible, so we remove them.
rfm = rfm[rfm['Monetary'] > 0]
rfm = rfm[rfm['Frequency'] > 0]

print(f"Valid customers after cleaning: {len(rfm)}")

# ---------------------------------------------------------
# 4. K-Means Clustering
# ---------------------------------------------------------
print("Running K-Means Clustering...")

# Log transformation to unskew the data
# We assume Recency, Frequency, and Monetary are all > 0 now
rfm_log = rfm[['Recency', 'Frequency', 'Monetary']].apply(np.log, axis=1).round(3)

# Scale data
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm_log)

# Fit K-Means (k=3)
kmeans = KMeans(n_clusters=3, random_state=42)
rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

# ---------------------------------------------------------
# 5. Labeling the Segments
# ---------------------------------------------------------
# Rank clusters by Monetary value to give them consistent names
cluster_avg = rfm.groupby('Cluster')['Monetary'].mean().sort_values(ascending=False).index

# Map: 0 -> Champion (High Spend), 1 -> Potential, 2 -> At Risk (Low Spend)
# Note: The specific index (0,1,2) might vary, so we map based on the sorted rank
label_map = {
    cluster_avg[0]: 'Champions', 
    cluster_avg[1]: 'Potential Loyalists', 
    cluster_avg[2]: 'At Risk'
}
rfm['Segment_Label'] = rfm['Cluster'].map(label_map)

# ---------------------------------------------------------
# 6. Cohort Analysis Data Prep (Simplified)
# ---------------------------------------------------------
print("Preparing Cohort Data...")
df['OrderMonth'] = df['InvoiceDate'].dt.to_period('M')
df['CohortMonth'] = df.groupby('CustomerID')['InvoiceDate'].transform('min').dt.to_period('M')
df['CohortIndex'] = (df['OrderMonth'] - df['CohortMonth']).apply(lambda x: x.n)

cohort_counts = df.groupby(['CohortMonth', 'CohortIndex'])['CustomerID'].nunique().reset_index()
cohort_counts.rename(columns={'CustomerID': 'UserCount'}, inplace=True)
cohort_counts['CohortMonth'] = cohort_counts['CohortMonth'].astype(str)

# ---------------------------------------------------------
# 7. Export
# ---------------------------------------------------------
rfm.to_csv('powerbi_customer_segments.csv', index=False)
cohort_counts.to_csv('powerbi_cohorts.csv', index=False)

print("\nSUCCESS! Files generated:")
print("1. powerbi_customer_segments.csv")
print("2. powerbi_cohorts.csv")