import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import json
from PIL import Image

#start handler
class csvHandler:
    def __init__(self,fileName):
        self.fileName = fileName
        df = pd.read_csv(fileName)
        self.data = {}
        for i in df:
            self.data[i]=df[i].tolist()
        self.dataFrame = df
ch_ = csvHandler('progres-donatur.csv')
df = ch_.dataFrame

st.set_page_config(layout="wide")

st.title('DONASI IAAF')
st.header('Okeee')
st.table(df)

#Konfigurasi Pengaturan
config = st.sidebar.radio("Pilih bagian yang ingin Anda ketahui", ('Deskripsi', 'Rekapitulasi', 'Kontak Kami'))
#if......

left_col, mid_col, right_col = st.columns(3)

#upper left col
#dict jenis unik, total donasi
Jenis_unik = list(df['Jenis'].unique())
total_donasi = []
for Jenis in Jenis_unik:
    Nominal = df[df['Jenis']==Jenis]['Nominal'].astype(int)
    total_donasi.append(Nominal.sum())
dic_jen_tot ={'Jenis Donasi':Jenis_unik,'total donasi':total_donasi}
left_col.dataframe(dic_jen_tot)

#upper middle col
#tujuan unik
tujuan_unik = list(df['Tujuan'].unique())
donasi_tujuan = []
for tujuan in tujuan_unik:
    sub_tujuan = df[df['Tujuan']==tujuan]['Nominal'].astype(int)
    donasi_tujuan.append(sub_tujuan.sum())
dic_donasi_tujuan={'Tujuan':tujuan_unik,'Jumlah donasi':donasi_tujuan}
mid_col.dataframe(dic_donasi_tujuan)

#upper right col
#nama unik
#dict nama unik, jumlah donasi
nama_unik=list(df['Nama'].unique()) #nama unik
jumlah_nominal = []
for nama in nama_unik:
    sub_nom = df[df['Nama']==nama]['Nominal'].astype(int)
    jumlah_nominal.append(sub_nom.sum())
dic_nama_jumnom={'Nama':nama_unik,'Jumlah Donasi':jumlah_nominal}
right_col.dataframe(dic_nama_jumnom)

#bawah
#dic bulan unik, jumlah donasi (Donatur Tetap)
bulan_unik = list(df['Bulan'].unique())
donasi_bulan = []
for bulan in bulan_unik:
    sub_bulan = df[df['Bulan']==bulan]['Nominal'].astype(int)
    donasi_bulan.append(sub_bulan.sum())
bulan = right_col.selectbox('Pilih Bulan: ',bulan_unik)
dic_donasi_bulan={'Bulan':bulan,'Jumlah Donasi':donasi_bulan}
st.dataframe(dic_donasi_bulan)
