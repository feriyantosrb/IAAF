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
st.dataframe(df)

'''
#Konfigurasi Pengaturan
config = st.sidebar.radio("Pilih bagian yang ingin Anda ketahui", ('Deskripsi', 'Rekapitulasi', 'Kontak Kami'))
#if......
'''

left_col, mid_col, right_col = st.columns(3)

#upper left col
#dict jenis unik, total donasi
Jenis_unik = list(df['Jenis'].unique())
pilih = left_col.selectbox('masukkan pilihan',Jenis_unik)
total_donasi = []
for Jenis in Jenis_unik:
    Nominal = df[df['Jenis']==Jenis]['Nominal'].astype(int)
    total_donasi.append(Nominal.sum())
dic_jen_tot ={'Jenis Donasi':Jenis_unik,'total donasi':total_donasi}
data = pd.DataFrame(dic_jen_tot)
if pilih == Jenis_unik [0]:
    st.write(data[0:1])
else :
    st.write(data[1:])


#upper middle col
#membuat nama unik
nama_unik=list(df['Nama'].unique()) #nama unik
jumlah_nominal = []
for nama in nama_unik:
    sub_nom = df[df['Nama']==nama]['Nominal'].astype(int)
    jumlah_nominal.append(sub_nom.sum())
dic_nama_jumnom={'Nama':nama_unik,'Jumlah Donasi':jumlah_nominal}
nama_jumnom = pd.DataFrame(dic_nama_jumnom)
#print(nama_jumnom)
choose = st.selectbox('pilih nama donatur',nama_unik) # nama_unik[0],....
if choose == nama_unik[0]:
    st.write(nama_jumnom[0:1])
if choose == nama_unik[1]:
    st.write(nama_jumnom[1:2])
if choose == nama_unik[2]:
    st.write(nama_jumnom[2:3])
if choose == nama_unik[3]:
    st.write(nama_jumnom[3:4])
if choose == nama_unik[4]:
    st.write(nama_jumnom[4:5])
if choose == nama_unik[5]:
    st.write(nama_jumnom[5:6])
if choose == nama_unik[6]:
    st.write(nama_jumnom[6:7])
if choose == nama_unik[7]:
    st.write(nama_jumnom[7:8])
if choose == nama_unik[8]:
    st.write(nama_jumnom[8:9])
if choose == nama_unik[9]:
    st.write(nama_jumnom[9:10])
if choose == nama_unik[10]:
    st.write(nama_jumnom[10:11])
if choose == nama_unik[11]:
    st.write(nama_jumnom[11:12])
if choose == nama_unik[12]:
    st.write(nama_jumnom[12:13])
if choose == nama_unik[13]:
    st.write(nama_jumnom[13:14])
if choose == nama_unik[14]:
    st.write(nama_jumnom[0:1])
if choose == nama_unik[15]:
    st.write(nama_jumnom[0:1])
if choose == nama_unik[16]:
    st.write(nama_jumnom[0:1])
if choose == nama_unik[17]:
    st.write(nama_jumnom[0:1])
if choose == nama_unik[18]:
    st.write(nama_jumnom[0:1])
if choose == nama_unik[19]:
    st.write(nama_jumnom[0:1])
if choose == nama_unik[20]:
    st.write(nama_jumnom[0:1])
if choose == nama_unik[21]:
    st.write(nama_jumnom[0:1])
if choose == nama_unik[22]:
    st.write(nama_jumnom[0:1])
if choose == nama_unik[23]:
    st.write(nama_jumnom[0:1])
if choose == nama_unik[24]:
    st.write(nama_jumnom[0:1])
if choose == nama_unik[25]:
    st.write(nama_jumnom[0:1])
if choose == nama_unik[26]:
    st.write(nama_jumnom[0:1])
if choose == nama_unik[27]:
    st.write(nama_jumnom[0:1])
if choose == nama_unik[28]:
    st.write(nama_jumnom[0:1])
if choose == nama_unik[29]:
    st.write(nama_jumnom[0:1])


#lower left col
#tujuan unik
tujuan_unik = list(df['Tujuan'].unique())
donasi_tujuan = []
for tujuan in tujuan_unik:
    sub_tujuan = df[df['Tujuan']==tujuan]['Nominal'].astype(int)
    donasi_tujuan.append(sub_tujuan.sum())
dic_donasi_tujuan={'Tujuan':tujuan_unik,'Jumlah donasi':donasi_tujuan}
don_tu = pd.DataFrame(dic_donasi_tujuan)
pil_dontu = st.selectbox('pilih alamat donasi tujuan',tujuan_unik)
if pil_dontu == tujuan_unik[0]:
    st.write(don_tu[0:1])
if pil_dontu == tujuan_unik[1]:
    st.write(don_tu[1:2])
if pil_dontu == tujuan_unik[2]:
    st.write(don_tu[2:3])
if pil_dontu == tujuan_unik[3]:
    st.write(don_tu[3:4])
if pil_dontu == tujuan_unik[4]:
    st.write(don_tu[4:5])
if pil_dontu == tujuan_unik[5]:
    st.write(don_tu[5:6])

#bawah
#dic bulan unik, jumlah donasi (Donatur Tetap)
bulan_unik = list(df['Bulan'].unique())
donasi_bulan = []
for bulan in bulan_unik:
    sub_bulan = df[df['Bulan']==bulan]['Nominal'].astype(int)
    donasi_bulan.append(sub_bulan.sum())
dic_donasi_bulan={'Bulan':bulan_unik,'Jumlah Donasi':donasi_bulan}
don_bul = pd.DataFrame(dic_donasi_bulan)
pil_donbul = st.selectbox('pilih bulan',bulan_unik)
if pil_donbul==bulan_unik[0]:
    st.write(don_bul[0:1])
if pil_donbul==bulan_unik[1]:
    st.write(don_bul[1:2])
if pil_donbul==bulan_unik[2]:
    st.write(don_bul[2:3])
if pil_donbul==bulan_unik[3]:
    st.write(don_bul[3:4])
if pil_donbul==bulan_unik[4]:
    st.write(don_bul[4:5])
