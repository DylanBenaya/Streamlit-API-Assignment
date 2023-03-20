import streamlit as st
import pandas as pd

tab1, tab2, tab3, tab4 = st.tabs(['Dataframe', 'Chart', 'Widget', 'Full Element'])
data = pd.read_csv("datakependudukan.csv")

with tab1:
    
    st.header("Indonesian Population Data from 2015 to 2020")
    data_chart = pd.DataFrame(data)
    st.checkbox("Use container width", value=False, key="use_container_width")    
    st.dataframe(data_chart, use_container_width=st.session_state.use_container_width)

with tab2:

    st.header("Indonesian Population Data from 2015 to 2020")
    data_chart = pd.DataFrame(data)
    st.line_chart(data_chart, x='TAHUN', y='INDONESIA')

with tab3:
    data_option = st.multiselect(

        'Pilih Daerah yang kamu mau',
        ['ACEH', 'SUMATERA UTARA', 'SUMATERA BARAT', 'RIAU', 'JAMBI', 'SUMATERA SELATAN', 'BENGKULU', 'LAMPUNG', 
        'KEP. BANGKA BELITUNG', 'KEP. RIAU', 'DKI JAKARTA', 'JAWA BARAT', 'JAWA TENGAH','DI YOGYAKARTA', 'JAWA TIMUR', 'BANTEN',
        'BALI',' NUSA TENGGARA BARAT', 'NUSA TENGGARA TIMUR', 'KALIMANTAN BARAT', 'KALIMANTAN TENGAH', 'KALIMANTAN SELATAN', 
        'KALIMANTAN TIMUR', 'KALIMANTAN UTARA',' SULAWESI UTARA', 'SULAWESI TENGAH', 'SULAWESI SELATAN', 'SULAWESI TENGGARA', 
        'GORONTALO', 'SULAWESI BARAT', 'MALUKU', 'MALUKU UTARA', 'PAPUA BARAT' , 'PAPUA', 'INDONESIA'
    ]
    )
    st.header("Indonesian Population Data from 2015 to 2020")
    data_chart = pd.DataFrame(data)
    st.line_chart(data_chart, x='TAHUN', y=data_option)

with tab4:

    st.header("Indonesian Population Data from 2015 to 2020")
    data_chart = pd.DataFrame(data)
    st.checkbox("Use container width", value=False, key="container_width")    
    st.dataframe(data_chart, use_container_width=st.session_state.container_width)
    st.line_chart(data_chart, x='TAHUN', y=data_option)