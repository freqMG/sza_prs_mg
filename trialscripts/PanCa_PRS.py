import pandas as pd
from scipy.stats import rankdata

# Bireyin PRS skoru
user_score = 0.03745  # burayı ihtiyacına göre güncelleyebilirsin

# 1000G skorlarını oku
df_1000g = pd.read_csv("prs_kidney_1000G_chrpos.sscore", sep="\t", skiprows=1,
                       names=["IID", "ALLELE_CT", "NAMED_ALLELE_DOSAGE_SUM", "SCORE1_AVG"])

# Ortalama skor
mean_score = df_1000g["SCORE1_AVG"].mean()
double_mean = 2 * mean_score
relative_risk = user_score / mean_score

# Kullanıcı verisini ekle
df_all = pd.concat([
    df_1000g,
    pd.DataFrame([["P001024_12", None, None, user_score]],
                 columns=["IID", "ALLELE_CT", "NAMED_ALLELE_DOSAGE_SUM", "SCORE1_AVG"])
], ignore_index=True)

# Büyükten küçüğe sıralı yüzdelik hesapla
df_all["percentile"] = rankdata(-df_all["SCORE1_AVG"], method="average") / len(df_all) * 100

# Kullanıcının yüzdelik değeri
user_percentile = df_all[df_all["IID"] == "P001024_12"]["percentile"].values[0]

# Skorun 2x ortalama eşik değerine oranı
percent_of_double_mean = (user_score / double_mean) * 100

# Çıktılar
print(f"Pancreatic Cancer PRS mean (1000G): {mean_score:.6f}")
print(f"Individual score: {user_score:.6f}")
print(f"Relative Risk: {relative_risk:.2f} kat")
print(f"2x mean threshold: {double_mean:.6f}")
print(f"Individual percentile: %{percent_of_double_mean:.2f}")