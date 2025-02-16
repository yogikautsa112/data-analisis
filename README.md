# ✨ Dicoding Collection Dashboard  

**Dicoding Collection Dashboard** adalah aplikasi berbasis **Streamlit** yang digunakan untuk menganalisis data e-commerce. Dashboard ini menyajikan berbagai visualisasi interaktif untuk menjawab pertanyaan seputar karakteristik pelanggan dan pola pembelian produk sepanjang musim.

## 🚀 Fitur Utama  
👉 **Analisis Karakteristik Pelanggan**  
   - Menampilkan pelanggan yang lebih sering melakukan pembelian berdasarkan data transaksi.  

👉 **Tren Produk di Setiap Musim**  
   - Menganalisis produk yang paling banyak dibeli dalam berbagai periode waktu.  

👉 **Visualisasi Data Interaktif**  
   - Menggunakan **Plotly** dan **Matplotlib** untuk grafik yang mudah dipahami.  

👉 **Dukungan Multi-Platform**  
   - Dapat dijalankan di **Windows, macOS, dan Linux** melalui **Anaconda**, **Pipenv**, atau lingkungan virtual lainnya.  

---

## 📌 Instalasi dan Konfigurasi  

### **1️⃣ Menggunakan Anaconda**  
```sh
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

### **2️⃣ Menggunakan Terminal / Command Prompt**  
```sh
# Buat folder proyek
mkdir proyek_analisis_data && cd proyek_analisis_data

# Buat virtual environment menggunakan Pipenv
pipenv install
pipenv shell

# Install dependensi
pip install -r requirements.txt
```

---

## ▶️ Jalankan Aplikasi  

```sh
streamlit run dashboard.py
```

Aplikasi akan berjalan di **http://localhost:8501** (default Streamlit).  

---

## 📂 Struktur Direktori  

```
proyek_analisis_data/
│-- dataset/                # Folder berisi dataset CSV
│-- dashboard.py            # Script utama aplikasi Streamlit
│-- requirements.txt        # Daftar dependensi
│-- README.md               # Dokumentasi proyek
```

---

## 🛠 Dependensi  

Pastikan telah menginstal dependensi berikut sebelum menjalankan proyek:  
```sh
pip install -r requirements.txt
```

**Daftar dependensi utama:**  
- `pandas` → Manipulasi data  
- `numpy` → Operasi numerik  
- `matplotlib` → Visualisasi grafik statis  
- `seaborn` → Visualisasi data lebih estetik  
- `plotly` → Grafik interaktif  
- `streamlit` → Framework dashboard  

---

## 💡 Kontribusi  
Jika ingin berkontribusi, silakan fork repositori ini, buat branch baru, dan ajukan pull request! 😊  

---

## 🐝 Lisensi  
Proyek ini dilisensikan di bawah **MIT License**.  

🚀 **Selamat menganalisis data!** 🎉  

