import pandas as pd
from scipy.stats import rankdata
import matplotlib.pyplot as plt

# .sscore dosyasını oku (ilk satırı atlıyoruz, çünkü başlık # ile başlıyor)
df = pd.read_csv("prs_result.sscore", sep="\t", skiprows=1,
                 names=["IID", "ALLELE_CT", "NAMED_ALLELE_DOSAGE_SUM", "SCORE1_AVG"])

# Her birey için percentile hesapla
df["percentile"] = rankdata(df["SCORE1_AVG"], method="average") / len(df) * 100

# Sonuçları göster
print(df.sort_values("percentile", ascending=False).head())

# Histogram + percentile eğrisi
plt.figure(figsize=(10, 6))
plt.hist(df["SCORE1_AVG"], bins=50, color="skyblue", alpha=0.7, edgecolor="k")
plt.xlabel("PRS Score (SCORE1_AVG)")
plt.ylabel("Kişi Sayısı")
plt.title("1000 Genomes PRS Dağılımı")
plt.grid(True)
plt.tight_layout()
plt.show()
