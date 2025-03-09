import pandas as pd

# Load dataset
day_df = pd.read_csv("data/day.csv")
hour_df = pd.read_csv("data/hour.csv")

# Ubah dteday ke format datetime
day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

# Gabungkan berdasarkan dteday
merged_df = pd.merge(hour_df, day_df, on="dteday", suffixes=("_hour", "_day"))

# Simpan ke CSV
merged_df.to_csv("data/all_data.csv", index=False)

print("Dataset berhasil digabung dan disimpan sebagai 'data/all_data.csv'")
