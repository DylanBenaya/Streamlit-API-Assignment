import streamlit as st
import pandas as pd

def load_data(sheets_url):
  csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
  return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gsheets_url"])

# Set the page title
st.set_page_config(page_title="Indonesian Population Data", page_icon=":bar_chart:")

st.header("Indonesian Population Data from 2015 to 2020")


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
st.checkbox("Use container width", value=False, key="use_container_width")
st.dataframe(df, use_container_width=st.session_state.use_container_width)
st.line_chart(data_chart, x='TAHUN', y=data_option)



