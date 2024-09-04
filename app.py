
import streamlit as st
import pickle
import numpy as np



with open('pipe.pkl', 'rb') as model_file:
    pipe = pickle.load(model_file, encoding='latin1')

with open('df.pkl', 'rb') as df_file:
    df = pickle.load(df_file, encoding='latin1')

st.title("Laptop Price Predictor")



company = st.selectbox('Brand', df['Company'].unique())
laptop_type = st.selectbox('Type', df['TypeName'].unique())
ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
weight = st.number_input('Weight of the Laptop (in kg)')
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
ips = st.selectbox('IPS Display', ['No', 'Yes'])
screen_size = st.slider('Screen Size (in inches)', 10.0, 18.0, 13.0)
resolution = st.selectbox('Screen Resolution', ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2560x1600', '2560x1440', '2304x1440'])
cpu = st.selectbox('CPU Brand', df['Cpu brand'].unique())
hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])
ssd = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])
gpu = st.selectbox('GPU Brand', df['Gpu brand'].unique())
os = st.selectbox('Operating System', df['os'].unique())



if st.button('Predict Price'):
   

    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0



    X_res, Y_res = map(int, resolution.split('x'))
    ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size

    
    query = np.array([company, laptop_type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os])
    query = query.reshape(1, 12)

   
    predicted_price = np.exp(pipe.predict(query)[0])
    st.title(f"The predicted price of this configuration is RNS = {predicted_price:.2f}")


