# ✨ Dicoding Collection Dashboard  

**Dicoding Collection Dashboard** adalah aplikasi berbasis **Streamlit** yang digunakan untuk menganalisis data e-commerce. Dashboard ini menyajikan berbagai visualisasi interaktif untuk menjawab pertanyaan seputar karakteristik pelanggan dan pola pembelian produk sepanjang musim.

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
streamlit run dashboard/dashboard.py
```

Aplikasi akan berjalan di **http://localhost:8501** (default Streamlit).  

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