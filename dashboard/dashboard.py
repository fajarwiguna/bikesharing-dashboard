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

st.markdown("""
📌 **Insight:**
- 🚴 Total peminjaman sepeda sepanjang tahun ini mencapai **{} kali**.
- 📊 Rata-rata peminjaman harian menunjukkan pola penggunaan reguler oleh masyarakat.
- 🔥 Terdapat hari dengan lonjakan peminjaman tertinggi, bisa jadi karena **event khusus, cuaca bagus, atau hari libur**.
""".format(df_filtered["cnt_day"].sum()))

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

    st.markdown("""
    📌 **Insight:**
    - 📈 Peminjaman meningkat pada bulan tertentu, bisa jadi karena **cuaca yang lebih baik** atau **liburan**.
    - 🔻 Jika ada bulan dengan peminjaman rendah, bisa dianalisis lebih lanjut penyebabnya.
    """)

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

    st.markdown("""
    📌 **Insight:**
    - ☀️ **Musim panas memiliki peminjaman tertinggi**, menunjukkan bahwa cuaca yang baik mendorong lebih banyak orang bersepeda.
    - ❄️ **Musim dingin memiliki peminjaman terendah**, kemungkinan karena cuaca dingin dan salju membuat bersepeda kurang nyaman.
    - 🚲 **Saran:** Penyedia layanan bisa meningkatkan jumlah sepeda saat musim panas dan mengurangi saat musim dingin untuk efisiensi.
    """)

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

st.markdown("""
📌 **Insight:**
- ☀️ Cuaca cerah berkontribusi pada peminjaman tertinggi, menunjukkan preferensi orang untuk bersepeda saat cuaca mendukung.
- 🌧️ Peminjaman menurun saat hujan lebat, menandakan **kebutuhan alternatif transportasi di kondisi ekstrem**.
- 🚲 **Saran:** Penyedia layanan bisa memberikan **diskon saat cuaca mendung** untuk mendorong penggunaan yang lebih stabil.
""")

# 4️⃣ Perbandingan Pengguna Kasual vs Terdaftar
st.header("👥 Kasual vs Terdaftar")
user_data = df_filtered[["casual_day", "registered_day"]].sum()

plt.figure(figsize=(6, 6))
plt.pie(user_data, labels=["Kasual", "Terdaftar"], autopct="%1.1f%%", colors=["lightblue", "orange"])
plt.title("Proporsi Pengguna Sepeda")
st.pyplot(plt)

st.markdown("""
📌 **Insight:**
- 👤 **Mayoritas pengguna adalah pengguna terdaftar**, yang mungkin berlangganan layanan penyewaan sepeda.
- 🚲 Pengguna kasual lebih sedikit, tetapi bisa ditingkatkan dengan **promosi atau kemudahan akses** bagi mereka yang tidak berlangganan.
""")

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

st.markdown("""
📌 **Insight:**
- 🚀 **Puncak peminjaman kasual terjadi di akhir pekan**, menunjukkan bahwa pengguna kasual lebih sering menggunakan sepeda untuk rekreasi.
- 📅 **Hari kerja memiliki peminjaman lebih rendah**, kemungkinan karena sebagian besar orang lebih memilih transportasi lain untuk ke kantor.
- 💡 **Strategi:** Promosi khusus di hari kerja bisa meningkatkan jumlah peminjaman kasual pada hari-hari biasa.
""")

st.success("🎉 Analisis selesai! Semoga bermanfaat dalam memahami tren peminjaman sepeda. 🚴‍♂️💨")
