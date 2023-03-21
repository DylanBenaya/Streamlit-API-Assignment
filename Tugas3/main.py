import streamlit as st
import pandas as pd
from PIL import Image
import time


def load_data(sheets_url):
  csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
  return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gsheets_url"])

def main():
    with st.spinner('In Progress...'):
        time.sleep(2)
        st.header('Welcome To Indonesian Population Data Sorting')
        st.image("https://setkab.go.id/wp-content/uploads/2021/01/Screen-Shot-2021-01-23-at-17.44.12.png")
        with st.sidebar:
            st.header("Settings Area")
            st.checkbox("Use container width", value=False, key="use_container_width") 
            data_option = st.multiselect(

                'Pilih Daerah yang kamu mau',
                ['ACEH', 'SUMATERA_UTARA', 'SUMATERA_BARAT', 'RIAU', 'JAMBI', 'SUMATERA_SELATAN', 'BENGKULU', 'LAMPUNG', 
                'KEP_BANGKA BELITUNG', 'KEP_RIAU', 'DKI_JAKARTA', 'JAWA_BARAT', 'JAWA_TENGAH','DI_YOGYAKARTA', 'JAWA_TIMUR', 'BANTEN',
                'BALI',' NUSA_TENGGARA_BARAT', 'NUSA_TENGGARA_TIMUR', 'KALIMANTAN_BARAT', 'KALIMANTAN_TENGAH', 'KALIMANTAN_SELATAN', 
                'KALIMANTAN_TIMUR', 'KALIMANTAN_UTARA',' SULAWESI_UTARA', 'SULAWESI_TENGAH', 'SULAWESI_SELATAN', 'SULAWESI_TENGGARA', 
                'GORONTALO', 'SULAWESI_BARAT', 'MALUKU', 'MALUKU_UTARA', 'PAPUA_BARAT' , 'PAPUA', 'INDONESIA'
            ]
            )
        data_chart = pd.DataFrame(df)
        st.dataframe(data_chart, use_container_width=st.session_state.use_container_width)
        st.line_chart(data_chart, x='TAHUN', y=data_option)
        st.experimental_show(data_chart)
        st.stop()

main()