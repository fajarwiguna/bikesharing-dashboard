import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("dashboard/all_data.csv")
    df["dteday"] = pd.to_datetime(df["dteday"])  # Konversi tanggal
    return df

df = load_data()

# Sidebar
st.sidebar.title("📊 Bike Sharing Dashboard")
st.sidebar.subheader("Filter Data")
selected_year = st.sidebar.radio("Pilih Tahun:", df["yr_day"].unique())

# Filter data berdasarkan tahun yang dipilih
df_filtered = df[df["yr_day"] == selected_year]

# Header
st.title("🚴‍♂️ Analisis Peminjaman Sepeda")

# 1️⃣ Statistik Umum
st.header("📈 Statistik Umum")
col1, col2, col3 = st.columns(3)
col1.metric("Total Peminjaman", df_filtered["cnt_day"].sum())
col2.metric("Peminjaman Harian Rata-rata", round(df_filtered["cnt_day"].mean(), 2))
col3.metric("Peminjaman Maksimum dalam Sehari", df_filtered["cnt_day"].max())

# 2️⃣ Tren Peminjaman Berdasarkan Bulan & Musim
st.header("📅 Tren Peminjaman Sepeda")
tab1, tab2 = st.tabs(["📆 Per Bulan", "🍂 Per Musim"])

with tab1:
    monthly_data = df_filtered.groupby("mnth_day")["cnt_day"].mean()
    plt.figure(figsize=(10, 5))
    sns.lineplot(x=monthly_data.index, y=monthly_data.values, marker="o")
    plt.xticks(range(1, 13), [
        "Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"
    ])
    plt.xlabel("Bulan")
    plt.ylabel("Jumlah Peminjaman")
    plt.title("Rata-rata Peminjaman Sepeda per Bulan")
    st.pyplot(plt)

with tab2:
    season_labels = {1: "Musim Semi", 2: "Musim Panas", 3: "Musim Gugur", 4: "Musim Dingin"}
    df_filtered["season_label"] = df_filtered["season_day"].map(season_labels)
    season_data = df_filtered.groupby("season_label")["cnt_day"].mean()
    
    plt.figure(figsize=(7, 5))
    sns.barplot(x=season_data.index, y=season_data.values, palette="coolwarm")
    plt.xlabel("Musim")
    plt.ylabel("Jumlah Peminjaman")
    plt.title("Rata-rata Peminjaman Sepeda per Musim")
    st.pyplot(plt)

# 3️⃣ Pengaruh Cuaca
st.header("🌦️ Pengaruh Cuaca terhadap Peminjaman")
weather_data = df_filtered.groupby("weathersit_day")["cnt_day"].mean()

plt.figure(figsize=(7, 5))
sns.barplot(x=weather_data.index, y=weather_data.values, palette="viridis")
plt.xticks([0, 1, 2, 3], ["Cerah", "Mendung", "Gerimis", "Hujan Lebat"])
plt.xlabel("Kondisi Cuaca")
plt.ylabel("Rata-rata Peminjaman")
plt.title("Dampak Cuaca terhadap Peminjaman Sepeda")
st.pyplot(plt)

# 4️⃣ Perbandingan Pengguna Kasual vs Terdaftar
st.header("👥 Kasual vs Terdaftar")
user_data = df_filtered[["casual_day", "registered_day"]].sum()

plt.figure(figsize=(6, 6))
plt.pie(user_data, labels=["Kasual", "Terdaftar"], autopct="%1.1f%%", colors=["lightblue", "orange"])
plt.title("Proporsi Pengguna Sepeda")
st.pyplot(plt)

# 5️⃣ Peminjaman Pengguna Kasual Berdasarkan Hari
st.header("📆 Pengguna Kasual Berdasarkan Hari")
day_labels = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
casual_data = df_filtered.groupby("weekday_day")["casual_day"].mean()

plt.figure(figsize=(8, 5))
sns.barplot(x=day_labels, y=casual_data.values, palette="mako")
plt.xlabel("Hari dalam Seminggu")
plt.ylabel("Rata-rata Peminjaman Kasual")
plt.title("Peminjaman Pengguna Kasual per Hari")
st.pyplot(plt)

st.success("🎉 Analisis selesai! Semoga bermanfaat dalam memahami tren peminjaman sepeda. 🚴‍♂️💨")
