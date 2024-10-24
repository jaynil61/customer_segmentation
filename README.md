# Customer Segmentation Web-App

**Web-app link:** https://customersegmentation-lxdes4ncd8qy9ucuthgjnk.streamlit.app/
## Overview
This project involves building a **Customer Segmentation App** using RFM (Recency, Frequency, Monetary) analysis. The app categorizes customers into three segments based on their purchasing behavior: **Occasional Spenders**, **Moderate Buyers**, and **Active Customers**. The segmentation helps in understanding customer behavior and optimizing marketing strategies.

## Segmentation Insights
### Cluster 1: Occasional Spenders
- **Recency**: High, indicating less recent purchases.
- **Frequency**: Low, suggesting infrequent purchases.
- **Monetary**: Low, indicating lower spending.
- **Interpretation**: These customers make occasional purchases and may not be highly engaged with the brand.

### Cluster 2: Moderate Buyers
- **Recency**: Moderate, with purchases more recent than Cluster 1 but less than Cluster 3.
- **Frequency**: Moderate, indicating a steady purchasing pattern.
- **Monetary**: Moderate, representing a balanced spending behavior.
- **Interpretation**: These customers purchase regularly and contribute consistently to revenue.

### Cluster 3: Active Customers
- **Recency**: Low, showing the most recent purchases.
- **Frequency**: High, indicating frequent buying behavior.
- **Monetary**: High, representing significant spending.
- **Interpretation**: These are the most valuable customers, contributing greatly to the revenue and showing high engagement.

## App Functionality
- **User Input**: Users can enter the last purchase date, frequency, and total amount spent to see the customer's segment.
- **Prediction**: Based on the input values, the app predicts the segment to which the customer belongs..

## Tools & Technologies
- **Language**: Python
- **Framework**: Streamlit for the web application.
- **Libraries**: pandas, numpy, matplotlib and seaborn for visualizations, scikit-learn for RFM analysis and clustering
- **Deployment**: Hosted on Streamlit.

## How to Use
1. **Input Data**: Enter the last purchase date, frequency, and total amount spent.
2. **Click Predict**: The app will display the customer segment based on the input.

## Conclusion
The Customer Segmentation App helps businesses identify and target different customer segments effectively. By focusing on the needs of each segment, businesses can improve customer retention and drive revenue growth.
