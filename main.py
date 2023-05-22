import streamlit as st
import sqlite3
import pandas as pd

# Fungsi untuk membuat tabel gaji
def create_table():
    conn = sqlite3.connect('penggajian.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS gaji (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT,
            posisi TEXT,
            gaji INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Fungsi untuk menambahkan data gaji
def add_data(nama, posisi, gaji):
    conn = sqlite3.connect('penggajian.db')
    c = conn.cursor()
    c.execute('INSERT INTO gaji (nama, posisi, gaji) VALUES (?, ?, ?)', (nama, posisi, gaji))
    conn.commit()
    conn.close()

# Fungsi untuk mengambil data gaji
def get_data():
    conn = sqlite3.connect('penggajian.db')
    df = pd.read_sql_query('SELECT * FROM gaji', conn)
    conn.close()
    return df

# Membuat tabel jika belum ada
create_table()

# Judul aplikasi
st.title('Aplikasi Penggajian')

# Menampilkan form untuk input data
nama = st.text_input('Nama')
posisi = st.text_input('Posisi')
gaji = st.number_input('Gaji')

# Tombol untuk menambahkan data
if st.button('Tambahkan Data'):
    add_data(nama, posisi, gaji)
    st.success('Data telah ditambahkan.')

# Menampilkan tabel data gaji
df = get_data()
st.dataframe(df)
