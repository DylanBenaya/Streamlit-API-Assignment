import streamlit as st
import pandas as pd
from PIL import Image
import time

data = pd.read_csv("datakependudukan.csv")
placeholder = st.empty()

actual_email = "admin"
actual_password = "admin"

def main():
    with st.spinner('In Progress...'):
        time.sleep(2)
        st.header('Welcome To Indonesian Population Data Sorting')
        image = Image.open('datasensus.png')
        st.image(image, caption='Hasil Sensus Penduduk 2020')
        with st.sidebar:
            st.header("Settings Area")
            st.checkbox("Use container width", value=False, key="use_container_width") 
            data_option = st.multiselect(

                'Select the area you want',
                ['ACEH', 'SUMATERA UTARA', 'SUMATERA BARAT', 'RIAU', 'JAMBI', 'SUMATERA SELATAN', 'BENGKULU', 'LAMPUNG', 
                'KEP. BANGKA BELITUNG', 'KEP. RIAU', 'DKI JAKARTA', 'JAWA BARAT', 'JAWA TENGAH','DI YOGYAKARTA', 'JAWA TIMUR', 'BANTEN',
                'BALI',' NUSA TENGGARA BARAT', 'NUSA TENGGARA TIMUR', 'KALIMANTAN BARAT', 'KALIMANTAN TENGAH', 'KALIMANTAN SELATAN', 
                'KALIMANTAN TIMUR', 'KALIMANTAN UTARA',' SULAWESI UTARA', 'SULAWESI TENGAH', 'SULAWESI SELATAN', 'SULAWESI TENGGARA', 
                'GORONTALO', 'SULAWESI BARAT', 'MALUKU', 'MALUKU UTARA', 'PAPUA BARAT' , 'PAPUA', 'INDONESIA'
            ]
            )
        data_chart = pd.DataFrame(data)
        st.dataframe(data_chart, use_container_width=st.session_state.use_container_width)
        st.line_chart(data_chart, x='TAHUN', y=data_option)
        st.experimental_show(data_chart)

with placeholder.form("login"):
        st.markdown("#### Enter your credentials")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
        if submit and email == actual_email and password == actual_password:
            placeholder.empty()
            with placeholder.container():
                 main()
        elif submit and email != actual_email and password != actual_password:
            st.error("Login failed")