import pandas as pd

# İlk satırı atla ve sütun isimlerini manuel ver
cols = ["IID", "ALLELE_CT", "NAMED_ALLELE_DOSAGE_SUM", "SCORE1_AVG"]

df_1000g = pd.read_csv("prs_result.sscore", sep='\t', skiprows=1, names=cols)

print(df_1000g.columns)
print(df_1000g.head())

scores_1000g = df_1000g["SCORE1_AVG"]

new_score = -0.00780959

percentile = (scores_1000g < new_score).mean() * 100
print(f"Yüzdelik dilim: %{percentile:.2f}")

mean = scores_1000g.mean()
std = scores_1000g.std()
z = (new_score - mean) / std
print(f"Z-score: {z:.2f}")

OR_per_SD = 1.6
RR = OR_per_SD ** z
print(f"Relative Risk: {RR:.2f} kat")
