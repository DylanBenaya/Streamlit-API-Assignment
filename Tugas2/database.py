import streamlit as st
import mysql.connector
import pandas as pd

def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

kodeaktor = run_query("SELECT `kode_aktor` FROM `webframework`.`aktor`;")
namaaktor = run_query("SELECT `nama_aktor` FROM `webframework`.`aktor`;")
alamat = run_query("SELECT `alamat` FROM `webframework`.`aktor`;")
kota = run_query("SELECT `kota` FROM `webframework`.`aktor`;")
email = run_query("SELECT `email` FROM `webframework`.`aktor`;")



def listdata():
    return pd.DataFrame(
        
        {
        
            "Kode Aktor": kodeaktor,
            "Nama Aktor" : namaaktor,
            "Alamat": alamat,
            "Kota": kota,
            "Email": email
        }
    )

st.checkbox("Use container width", value=False, key="use_container_width")

data = listdata()

st.dataframe(data, use_container_width=st.session_state.use_container_width)
