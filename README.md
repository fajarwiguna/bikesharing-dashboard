# 🚴‍♂️ **Bike Sharing Dashboard**  

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)  
![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python&logoColor=white)  
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)  
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)  

---

## 📌 Overview  
**Bike Sharing Dashboard** adalah aplikasi berbasis **Streamlit** yang memungkinkan eksplorasi interaktif terhadap tren peminjaman sepeda. Dengan memanfaatkan **visualisasi data**, pengguna dapat memahami pola peminjaman berdasarkan **musim, cuaca, dan kecepatan angin**.  

### 🔎 **Mengapa menggunakan dashboard ini?**  
✔️ Memudahkan analisis tren penggunaan sepeda  
✔️ Interaktif & mudah digunakan  
✔️ Dibangun dengan **Python, Pandas, Seaborn, dan Matplotlib**  

---

## ✨ Features  

✅ **📊 Analisis Musiman** – Lihat bagaimana tren peminjaman berubah di berbagai musim.  
✅ **🌤️ Pengaruh Cuaca & Kecepatan Angin** – Ketahui dampak kondisi lingkungan terhadap jumlah peminjaman.  
✅ **📈 Visualisasi Data yang Informatif** – Menggunakan **Seaborn** & **Matplotlib** untuk menyajikan grafik yang menarik.  
✅ **⚡ Dashboard Interaktif** – Dibangun dengan **Streamlit** untuk pengalaman yang lebih dinamis.  
✅ **🔍 Filter & Insights** – Gunakan filter interaktif untuk menggali informasi lebih dalam.  

---

## 🛠️ Installation & Setup  

### 1️⃣ **Persiapan Lingkungan**  
Pastikan **Python 3.12** telah terinstal di perangkat Anda. Jika belum, unduh dan instal dari [python.org](https://www.python.org/downloads/).  

### 2️⃣ **Setup Virtual Environment**  
Buat dan aktifkan lingkungan virtual untuk proyek ini:  

```sh
mkdir bike_sharing_dashboard
```
```sh
cd bike_sharing_dashboard
```
```sh
python -m venv venv
```
```sh
source .venv\Scripts\activate
```
### 3️⃣ Instalasi Dependensi
Setelah lingkungan virtual aktif, instal pustaka yang dibutuhkan:

```sh
pip install -r requirements.txt
```
### 🚀 Running the Dashboard
Untuk menjalankan dashboard, jalankan perintah berikut di terminal:

```sh
streamlit run dashboard/dashboard.py
```
Aplikasi akan terbuka di browser secara otomatis di http://localhost:8501.


### 🌍 Deployment
🔹 Hosting di Streamlit Cloud
Buat repository GitHub dan unggah proyek Anda.
Kunjungi Streamlit Cloud dan hubungkan ke repo GitHub.
Klik Deploy, dan dashboard akan tersedia secara online.
🔹 Alternatif Hosting
Anda juga bisa menggunakan Render atau Hugging Face Spaces untuk hosting gratis.

📌 Link Deploy: https://bikesharing-dashboard-fajar.streamlit.app/

📂 Project Structure
```bash
bike_sharing_dashboard/
│-- dashboard/
│   │-- dashboard.py   # Skrip utama untuk dashboard
│   │-- all_data.csv   # Dataset gabungan dari day.csv dan hour.csv
│-- data/
│   │-- day.csv        # Dataset peminjaman harian
│   │-- hour.csv       # Dataset peminjaman berdasarkan jam
│-- notebook.ipynb     # Notebook eksplorasi data
│-- README.md          # Dokumentasi proyek
│-- requirements.txt   # Daftar pustaka yang diperlukan
│-- url.txt            # Link ke dashboard Streamlit
```

### 📊 Data Source
Dataset yang digunakan berasal dari Bike Sharing Dataset, yang mencakup data peminjaman sepeda harian dan per jam.

Kolom utama dalam dataset:
season → Musim saat peminjaman dilakukan
temp → Suhu rata-rata
windspeed → Kecepatan angin
cnt → Jumlah total peminjaman

📜 License
Proyek ini menggunakan MIT License. Anda bebas menggunakannya dan memodifikasinya sesuai kebutuhan.

📬 Feedback & Kontribusi
💡 Punya ide atau saran? Silakan buat issue atau pull request di GitHub Repository.

🚀 Nikmati pengalaman eksplorasi data peminjaman sepeda! 📊🚴‍♂️







