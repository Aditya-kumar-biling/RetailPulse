import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(page_title="RetailPulse Dashboard", layout="wide")

# Title
st.title("🛒 RetailPulse - Customer Analytics Dashboard")

# Load data
@st.cache_data
def load_data():
    rfm = pd.read_csv("data/rfm_clusters.csv")
    rfm['Churn'] = (rfm['Recency'] > 180).astype(int)
    forecast = pd.read_csv("data/forecast_results.csv")
    return rfm, forecast

rfm, forecast = load_data()

# KPI Cards
st.subheader("📊 Key Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Customers", f"{len(rfm):,}")
col2.metric("Churned Customers", f"{(rfm['Churn']==1).sum():,}")
col3.metric("Champions", f"{(rfm['Segment']=='Champion').sum():,}")
col4.metric("Avg Monetary Value", f"£{rfm['Monetary'].mean():,.0f}")

# Customer Segments
st.subheader("👥 Customer Segments")
fig1, ax1 = plt.subplots(figsize=(10, 4))
rfm['Segment'].value_counts().plot(kind='bar', color='steelblue', edgecolor='white', ax=ax1)
ax1.set_title('Customer Segments')
ax1.set_xlabel('Segment')
ax1.set_ylabel('Count')
plt.xticks(rotation=30)
plt.tight_layout()
st.pyplot(fig1)

# Forecast
st.subheader("📈 Sales Forecast")
forecast['ds'] = pd.to_datetime(forecast['ds'])
fig2, ax2 = plt.subplots(figsize=(12, 4))
ax2.plot(forecast['ds'], forecast['yhat'], color='coral', label='Forecast')
ax2.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], alpha=0.3)
ax2.set_title('90 Day Sales Forecast')
ax2.set_xlabel('Date')
ax2.set_ylabel('Revenue (£)')
plt.tight_layout()
st.pyplot(fig2)

# Churn Distribution
st.subheader("⚠️ Churn Analysis")
fig3, ax3 = plt.subplots(figsize=(6, 4))
rfm['Churn'].value_counts().plot(kind='pie', labels=['Active', 'Churned'], 
                                   autopct='%1.1f%%', colors=['steelblue', 'coral'], ax=ax3)
ax3.set_title('Churn Distribution')
plt.tight_layout()
st.pyplot(fig3)

st.success("Dashboard loaded successfully! ✅")

