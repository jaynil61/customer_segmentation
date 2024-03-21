import streamlit as st
import pandas as pd
import numpy as np

# Load the average values DataFrame from the pickle file
avg_values = pd.read_pickle('avg_values.pkl')

# Create a function to calculate Euclidean distance
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

# Streamlit app
def main():
    st.title('Customer Segmentation App')

    # User input
    st.sidebar.write('User Input:')
    last_purchase_date = st.sidebar.date_input('Last Purchase Date', value=pd.Timestamp('2010-12-01'), min_value=pd.Timestamp('2010-12-01'), max_value=pd.Timestamp('2011-12-09'))
    frequency = st.sidebar.number_input('Frequency', min_value=0)
    total_amount = st.sidebar.number_input('Total Amount Spent', min_value=0.0)

    # Convert last_purchase_date to Timestamp
    last_purchase_date = pd.Timestamp(last_purchase_date)

    # Calculate number of days from last purchase date to 2011/12/09
    num_days = (pd.Timestamp('2011-12-09') - last_purchase_date).days

    # Prediction button
    if st.sidebar.button('Predict'):
        # Calculate Euclidean distance and find the nearest cluster
        user_input = np.array([num_days, frequency, total_amount])
        distances = avg_values[['R_avg', 'F_avg', 'M_avg']].apply(lambda x: euclidean_distance(x, user_input), axis=1)
        nearest_cluster = avg_values.loc[distances.idxmin(), 'Cluster']
        
        # Output message based on cluster prediction
        if nearest_cluster == 1:
            st.write("<span style='color:red; font-size:35px'><b>You are an occasional spender.</b></span>", unsafe_allow_html=True)
        elif nearest_cluster == 2:
            st.write("<span style='color:green; font-size:35px'><b>You are a moderate buyer.</b></span>", unsafe_allow_html=True)
        elif nearest_cluster == 3:
            st.write("<span style='color:blue; font-size:35px'><b>You are an active customer.</b></span>", unsafe_allow_html=True)
        else:
            st.write("Cluster prediction not available.")

if __name__ == '__main__':
    main()
