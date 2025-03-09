import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

bikes_per_day_df = pd.read_csv("data/day.csv")
bikes_per_hour_df = pd.read_csv("data/hour.csv")

bikes_per_day_df["dteday"] = pd.to_datetime(bikes_per_day_df["dteday"])
bikes_per_hour_df["dteday"] = pd.to_datetime(bikes_per_hour_df["dteday"])

min_date = bikes_per_day_df["dteday"].min().date()
max_date = bikes_per_day_df["dteday"].max().date()

with st.sidebar:
    st.header("📊 Bike Sharing Dashboard")
    st.image("https://img.freepik.com/premium-vector/young-man-rides-bicycle-flat-style-vector-illustration_787461-1042.jpg", width=150)
    st.write("Analisis tren peminjaman sepeda berdasarkan musim, cuaca, dan tipe pengguna.")

    start_date, end_date = st.date_input(
        "Pilih Rentang Waktu",
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

filtered_day_df = bikes_per_day_df[
    (bikes_per_day_df["dteday"].dt.date >= start_date) &
    (bikes_per_day_df["dteday"].dt.date <= end_date)
]

st.header("📆 Tren Peminjaman Sepeda Per Bulan & Musim")

filtered_day_df["year_month"] = filtered_day_df["dteday"].dt.to_period("M")
monthly_trend = filtered_day_df.groupby("year_month")["cnt"].sum()

fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x=monthly_trend.index.astype(str), y=monthly_trend.values, marker="o", linewidth=2, color="royalblue", ax=ax)
ax.set_title("Tren Jumlah Peminjaman Sepeda per Bulan", fontsize=14)
ax.set_xlabel("Bulan", fontsize=12)
ax.set_ylabel("Jumlah Peminjaman Sepeda", fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.6)
st.pyplot(fig)

st.markdown("💡 **Tren peminjaman sepeda meningkat di musim panas dan gugur, lalu menurun saat musim dingin.**")

st.header("🌦️ Pengaruh Kondisi Cuaca terhadap Peminjaman")

fig, ax = plt.subplots(figsize=(12, 6))
sns.scatterplot(x=filtered_day_df["temp"], y=filtered_day_df["cnt"], hue=filtered_day_df["weathersit"], palette="coolwarm", ax=ax)
ax.set_title("Hubungan Suhu dan Peminjaman Sepeda", fontsize=14)
ax.set_xlabel("Suhu (scaled)", fontsize=12)
ax.set_ylabel("Jumlah Peminjaman", fontsize=12)
st.pyplot(fig)

st.markdown("💡 **Semakin hangat suhu, semakin banyak peminjaman sepeda. Namun, kondisi cuaca buruk menurunkan peminjaman.**")

st.header("👤 Perbandingan Pengguna Kasual & Terdaftar")

casual_total = filtered_day_df["casual"].sum()
registered_total = filtered_day_df["registered"].sum()

fig, ax = plt.subplots(figsize=(6, 6))
plt.pie([casual_total, registered_total], labels=["Kasual", "Terdaftar"], autopct="%1.1f%%", colors=["#FF9999", "#66B3FF"], startangle=140)
plt.title("Proporsi Peminjaman: Kasual vs Terdaftar")
st.pyplot(fig)

st.markdown("💡 **Pengguna terdaftar jauh lebih dominan dibandingkan pengguna kasual.**")

st.header("📅 Pola Pengguna Kasual di Akhir Pekan")

weekday_usage = filtered_day_df.groupby("weekday")[["casual", "registered"]].sum()
weekday_usage.index = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]

fig, ax = plt.subplots(figsize=(10, 5))
weekday_usage["casual"].plot(kind="bar", color="#FF9999", label="Kasual", ax=ax)
weekday_usage["registered"].plot(kind="bar", color="#66B3FF", label="Terdaftar", alpha=0.7, ax=ax)
ax.set_title("Peminjaman Sepeda per Hari", fontsize=14)
ax.set_xlabel("Hari", fontsize=12)
ax.set_ylabel("Jumlah Peminjaman", fontsize=12)
plt.xticks(rotation=0)
plt.legend()
st.pyplot(fig)

st.markdown("💡 **Pengguna kasual lebih sering meminjam sepeda di akhir pekan, sedangkan pengguna terdaftar lebih merata sepanjang minggu.**")

st.markdown("---")
st.markdown("🚲 **Dashboard ini dikembangkan untuk memahami tren peminjaman sepeda dan memberikan wawasan berbasis data.**")
