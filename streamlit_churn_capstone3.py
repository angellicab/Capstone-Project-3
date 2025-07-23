# Deploy Churn Predictor

# ======================================================
import pandas as pd
import numpy as np

import streamlit as st
import pickle


# ======================================================

# Judul Utama
st.write('''
# E-COMMERCE CUSTOMER CHURN PREDICTOR
''')

# Menambahkan Sidebar
st.sidebar.header("Please input the Customer's Feature")

# Menambahkan feature untuk user input
def user_input_feature():
# Data numerikal
    Tenure = st.sidebar.number_input(label = 'Tenure', min_value=0, max_value=61, value=10)
    WarehouseToHome = st.sidebar.number_input(label = 'WarehouseToHome', min_value=5, max_value=127, value=10)
    NumberOfDeviceRegistered = st.sidebar.number_input(label = 'NumberOfDeviceRegistered', min_value=1, max_value=6, value=5)
    SatisfactionScore = st.sidebar.number_input(label = 'SatisfactionScore', min_value=1, max_value=5, value=5)
    NumberOfAddress = st.sidebar.number_input(label = 'NumberOfAddress', min_value=1, max_value=22, value=5)
    Complain = st.sidebar.number_input(label = 'Complain', min_value=0, max_value=1, value=0)
    DaySinceLastOrder = st.sidebar.number_input(label = 'DaySinceLastOrder', min_value=0, max_value=46, value=10)
    CashbackAmount = st.sidebar.number_input(label = 'CashbackAmount', min_value=0, max_value=350, value=100)

# Data categorical
    PreferedOrderCat = st.sidebar.selectbox(label = 'PreferedOrderCat',options=['Laptop & Accessory', 'Mobile', 'Fashion', 'Others', 'Mobile Phone', 'Grocery'])
    MaritalStatus = st.sidebar.selectbox(label = 'MaritalStatus',options=['Single', 'Married', 'Divorced'])

# Membuat table

    df = pd.DataFrame()
    df['Tenure'] = [Tenure]
    df['WarehouseToHome'] = [WarehouseToHome]
    df['NumberOfDeviceRegistered'] = [NumberOfDeviceRegistered]
    df['SatisfactionScore'] = [SatisfactionScore]
    df['NumberOfAddress'] = [NumberOfAddress]
    df['Complain'] = [Complain]
    df['DaySinceLastOrder'] = [DaySinceLastOrder]
    df['CashbackAmount'] = [CashbackAmount]
    df['PreferedOrderCat'] = [PreferedOrderCat]
    df['MaritalStatus'] = [MaritalStatus]

    return df

# Menampilkan user input dan dataframe
df_customer = user_input_feature()
df_customer.index = ['Value']


# Predict Customer

# Load model
model = pickle.load(open('model_lgbmclassifier_m3.sav', 'rb'))
kelas = model.predict(df_customer)

# Buat 2 kolom
column1, column2 = st.columns(2)

# column1 --> kontainer kiri
with column1:
    st.subheader('Customer Feature')
    st.write(df_customer.T)

# column2 --> kontainer kanan
with column2:
    st.subheader('Prediction')
    if kelas == 1:
        st.write('Class 1: This customer will CHURN')
    else:
        st.write('Class 0: This customer will STAY')

