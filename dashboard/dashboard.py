import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi tema visualisasi
sns.set_theme(style="darkgrid")

# Load dataset
all_df = pd.read_csv("dashboard/all_data.csv")
df_daily = pd.read_csv("data/day.csv")
df_hourly = pd.read_csv("data/hour.csv")

# Konversi kolom tanggal
df_daily["dteday"] = pd.to_datetime(df_daily["dteday"])
df_hourly["dteday"] = pd.to_datetime(df_hourly["dteday"])

# Rentang tanggal
min_date = df_daily["dteday"].min().date()
max_date = df_daily["dteday"].max().date()

# Sidebar
with st.sidebar:
    st.header("🚲 Bike Sharing Dashboard")
    st.image("https://img.freepik.com/premium-vector/young-man-rides-bicycle-flat-style-vector-illustration_787461-1042.jpg", width=120)
    
    start_date, end_date = st.date_input(
        "Pilih Rentang Waktu",
        value=[min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

    st.subheader("Tentang Dashboard")
    st.write(
        "Dashboard ini menyajikan analisis data peminjaman sepeda berdasarkan berbagai faktor, "
        "seperti musim, cuaca, hari dalam seminggu, dan kecepatan angin."
    )

# Filter data berdasarkan tanggal yang dipilih
df_filtered = df_daily[
    (df_daily["dteday"].dt.date >= start_date) & 
    (df_daily["dteday"].dt.date <= end_date)
]

# === FUNGSI UNTUK MEMBUAT VISUALISASI === #
def plot_monthly_trend():
    """Visualisasi tren peminjaman sepeda per bulan."""
    df_filtered["year_month"] = df_filtered["dteday"].dt.to_period("M")
    monthly_trend = df_filtered.groupby("year_month")["cnt"].sum()

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x=monthly_trend.index.astype(str), y=monthly_trend.values, marker="o", linewidth=2, color="royalblue", ax=ax)
    ax.set_title("Tren Peminjaman Sepeda per Bulan", fontsize=14)
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Jumlah Peminjaman")
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.6)
    st.pyplot(fig)

def plot_weekly_usage():
    """Visualisasi peminjaman sepeda berdasarkan hari dalam seminggu."""
    df_weekday = df_daily.groupby("weekday")["cnt"].sum().reset_index()
    day_labels = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x=df_weekday["weekday"], y=df_weekday["cnt"], palette="Blues_r", ax=ax)
    ax.set_title("Total Peminjaman Sepeda per Hari", fontsize=14)
    ax.set_xlabel("Hari")
    ax.set_ylabel("Jumlah Peminjaman")
    ax.set_xticklabels(day_labels, rotation=45)
    st.pyplot(fig)

def plot_seasonal_usage():
    """Visualisasi peminjaman sepeda berdasarkan musim."""
    df_season = df_hourly.groupby("season")[["casual", "registered"]].sum()
    df_season["total"] = df_season["casual"] + df_season["registered"]
    df_season = df_season.sort_values(by="total", ascending=False)

    season_labels = ["Musim Gugur 🍂", "Musim Panas ☀️", "Musim Dingin ❄️", "Musim Semi 🌿"]
    
    fig, ax = plt.subplots(figsize=(8, 5))
    df_season[["casual", "registered"]].plot(kind="bar", stacked=True, ax=ax, color=["lightblue", "royalblue"])
    ax.set_xticklabels(season_labels, rotation=0)
    ax.set_title("Peminjaman Sepeda Berdasarkan Musim", fontsize=14)
    ax.set_xlabel("Musim")
    ax.set_ylabel("Jumlah Peminjaman")
    st.pyplot(fig)

def plot_windspeed_effect():
    """Visualisasi pengaruh kecepatan angin terhadap peminjaman sepeda."""
    df_wind = df_hourly.groupby("windspeed")[["cnt"]].sum().reset_index()

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.lineplot(x=df_wind["windspeed"], y=df_wind["cnt"], marker="o", color="green", ax=ax)
    ax.set_title("Pengaruh Kecepatan Angin pada Peminjaman Sepeda", fontsize=14)
    ax.set_xlabel("Kecepatan Angin")
    ax.set_ylabel("Jumlah Peminjaman")
    plt.grid(True, alpha=0.6)
    st.pyplot(fig)

# === TAMPILAN DASHBOARD === #
st.title("🚲 Bike Sharing Dashboard")

# METRIK RINGKASAN
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Pengguna Kasual", value=df_filtered["casual"].sum())
with col2:
    st.metric("Pengguna Terdaftar", value=df_filtered["registered"].sum())
with col3:
    st.metric("Total Peminjaman", value=df_filtered["cnt"].sum())

# Visualisasi Tren Peminjaman Sepeda
st.subheader("📈 Tren Peminjaman Sepeda Per Bulan")
plot_monthly_trend()
st.markdown("💡 **Insight**: Jumlah peminjaman cenderung meningkat di pertengahan tahun dan menurun di musim dingin.")

# Visualisasi Peminjaman Berdasarkan Hari dalam Seminggu
st.subheader("📅 Peminjaman Sepeda Berdasarkan Hari")
plot_weekly_usage()
st.markdown("💡 **Insight**: Peminjaman sepeda lebih tinggi pada akhir pekan dibandingkan hari kerja.")

# Visualisasi Peminjaman Berdasarkan Musim
st.subheader("🌦️ Pengaruh Musim terhadap Peminjaman Sepeda")
plot_seasonal_usage()
st.markdown("💡 **Insight**: Pengguna kasual cenderung meminjam lebih banyak di musim panas dan gugur, sementara pengguna terdaftar lebih konsisten sepanjang tahun.")

# Visualisasi Pengaruh Kecepatan Angin
st.subheader("🌬️ Pengaruh Kecepatan Angin terhadap Peminjaman")
plot_windspeed_effect()
st.markdown("💡 **Insight**: Kecepatan angin tinggi cenderung mengurangi jumlah peminjaman sepeda.")

# FOOTER
st.markdown("---")
st.write("📊 **Dashboard Bike Sharing** dibuat untuk menganalisis pola penggunaan sepeda dan membantu pengambilan keputusan berdasarkan data yang ada.")

