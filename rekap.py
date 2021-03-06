import streamlit as st
import numpy as np
import pandas as pd
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
ch_ = csvHandler('data-iaaf.csv')
df = ch_.dataFrame

st.set_page_config(layout="wide")

st.title('Program Ikatan Alumni Al-Uswah Foundation')
image = Image.open('crop.png')
st.image(image)
st.header('Rekapitulasi Update Donasi')

#upper left col
#start jenis unik, total donasi
Jenis_unik = list(df['Jenis'].unique())
total_donasi = []
for Jenis in Jenis_unik:
    Nominal = df[df['Jenis']==Jenis]['Nominal'].str.replace(',','').astype(int)
    total_donasi.append(Nominal.sum())
dic_jen_tot ={'Jenis Donatur':Jenis_unik,'Total Donasi':total_donasi}
jenis_total = pd.DataFrame(dic_jen_tot)


total_rp = "Rp{:,.2f}".format(sum(total_donasi))

st.info('IAAF merukan program pengadaan beasiswa oleh para alumni/non alumni untuk membantu alumni Al-Uswah Boarding School untuk melanjutkan kuliah. Sebagai informasi al-uswah boarding school merupakan rintisan Boarding School yang diperuntukkan untuk anak-anak yatim/piatu/dhuafa berprestasi agar mampu melanjutkan pendidikan sampai tingkat menegah atas (SMA) dan membekali mereka dengan ilmu Agama Islam')
st.success('Total Donasi Sampai Saat Ini : {}'.format(total_rp))


left_col, right_col = st.columns([1,2])
right_col.subheader('Jumlah Donasi Berdasarkan Jenis Donatur')
pilih_jenis = right_col.selectbox('Pilih Jenis Donatur',Jenis_unik)
def a_ ():
    a = Jenis_unik.index(pilih_jenis)
    return a
def b_():
    frame_jenis = jenis_total [a_():a_()+1]
    return frame_jenis
right_col.write(b_())
#finish jenis, total donasi

#start Nama unik, Jumlah donasi
nama_unik=list(df['Nama'].unique()) #nama unik
jumlah_nominal = []
for nama in nama_unik:
    sub_nom = df[df['Nama']==nama]['Nominal'].str.replace(',','').astype(int)
    jumlah_nominal.append(sub_nom.sum())
dic_nama_jumnom={'Nama Donatur':nama_unik,'Jumlah Donasi':jumlah_nominal}
nama_jumnom = pd.DataFrame(dic_nama_jumnom)

tulis_nama = []
for i, nama in enumerate(nama_unik):
    tulis_nama.append(f"{str(i+1)}. {nama}\n")
tulis_nama = ' '.join(map(str, tulis_nama))

left_col.subheader('Daftar Nama Donatur')
left_col.write(tulis_nama)

right_col.subheader('Jumlah Donasi Berdasarkan Donatur')
choose = right_col.selectbox('Pilih Nama Donatur',nama_unik) # nama_unik[0],....
def c_ ():
    c = nama_unik.index(choose)
    return c
def d_():
    d = nama_jumnom[c_():c_()+1]
    return d
right_col.write(d_())
#finish nama, jumlah

#start tujuan unik, Nominal
tujuan_unik = list(df['Tujuan'].unique())
donasi_tujuan = []
for tujuan in tujuan_unik:
    sub_tujuan = df[df['Tujuan']==tujuan]['Nominal'].str.replace(',','').astype(int)
    donasi_tujuan.append(sub_tujuan.sum())
dic_donasi_tujuan={'Alamat Donasi Tujuan':tujuan_unik,'Nominal':donasi_tujuan}
don_tu = pd.DataFrame(dic_donasi_tujuan)
right_col.write()
right_col.subheader('Jumlah Donasi Berdasarkan Alamat Tujuan Donasi')
pil_dontu = right_col.selectbox('Pilih Alamat Tujuan Donasi',tujuan_unik)
def e_ ():
    e = tujuan_unik.index(pil_dontu)
    return e
def f_():
    f = don_tu[e_():e_()+1]
    return f
right_col.write(f_())
#finish tujuan, nominal

#start bulan unik, jumlah donasi (Donatur Tetap)
bulan_unik = list(df['Bulan'].unique())
donasi_bulan = []
for bulan in bulan_unik:
    sub_bulan = df[df['Bulan']==bulan]['Nominal'].str.replace(',','').astype(int)
    donasi_bulan.append(sub_bulan.sum())
dic_donasi_bulan={'Bulan':bulan_unik,'Nominal':donasi_bulan}
don_bul = pd.DataFrame(dic_donasi_bulan)
right_col.write()
right_col.subheader('Jumlah Donasi Berdasarkan Bulan')
pil_donbul = right_col.selectbox('Pilih Bulan',bulan_unik)
def g_ ():
    g = bulan_unik.index(pil_donbul)
    return g
def h_():
    h = don_bul[g_():g_()+1]
    return h
right_col.write(h_())

st.write()
st.header('Summary')
st.subheader('Total Donasi Sampai Saat Ini : {}'.format(total_rp))
st.table(df)
