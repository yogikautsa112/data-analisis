# Dicoding Collection Dashboard ✨

## Setup Environment - Anaconda
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt

## Setup Environment - Shell/Terminal
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt

## Jalankan Aplikasi Streamlit
streamlit run dashboard.py

## Deskripsi Proyek
Dicoding Collection Dashboard adalah sebuah aplikasi berbasis Streamlit yang digunakan untuk menganalisis data e-commerce. Dashboard ini menyajikan berbagai visualisasi data untuk menjawab pertanyaan seputar karakteristik pelanggan dan pola pembelian produk sepanjang musim.

## Fitur Utama
- **Analisis Karakteristik Pelanggan**: Menampilkan pelanggan yang lebih sering melakukan pembelian berdasarkan data transaksi.
- **Tren Produk di Setiap Musim**: Menganalisis produk yang paling banyak dibeli dalam berbagai periode waktu.
- **Visualisasi Data Interaktif**: Menggunakan Plotly dan Matplotlib untuk menampilkan grafik yang mudah dipahami.

## Dependensi
Pastikan telah menginstal dependensi yang diperlukan dengan menjalankan perintah berikut:
pip install -r requirements.txt

## Struktur Direktori

proyek_analisis_data/
│-- dataset/  # Folder berisi dataset CSV
│-- dashboard.py  # Script utama aplikasi Streamlit
│-- requirements.txt  # Daftar dependensi
│-- README.md  # Dokumentasi proyek