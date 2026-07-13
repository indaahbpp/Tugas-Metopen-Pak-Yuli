import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# =========================
# SET FONT
# =========================
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 12

# =========================
# NAMA FILE EXCEL
# =========================
file = "DATA MENTAH.xlsx"

print(f"\nProcessing: {file}")

# =========================
# LOAD DATA
# =========================
data = pd.read_excel(file)

# =========================
# TARGET = KOLOM TERAKHIR
# =========================
target_col = data.columns[-1]

# Semua kolom sebelum target = variabel X
feature_cols = data.columns[:-1]

X = data[feature_cols]
y = data[target_col]

print(f"Variabel X: {list(feature_cols)}")
print(f"Variabel Y: {target_col}")

# =========================
# MODEL REGRESI
# =========================
model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

# =========================
# METRICS
# =========================
r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))
mae = mean_absolute_error(y, y_pred)
mape = np.mean(np.abs((y - y_pred) / (y + 1e-8))) * 100

# =========================
# PERSAMAAN REGRESI
# =========================
coeffs = model.coef_
intercept = model.intercept_

equation = f"y = {intercept:.4f}"

for i, col in enumerate(feature_cols):
    equation += f" + ({coeffs[i]:.4f} × {col})"

print("\nPersamaan Regresi:")
print(equation)

print("\nMetrics:")
print(f"R²   : {r2:.4f}")
print(f"RMSE : {rmse:.4f}")
print(f"MAE  : {mae:.4f}")
print(f"MAPE : {mape:.2f}%")

# =========================
# HEATMAP
# =========================
plt.figure(figsize=(6,5))

sns.heatmap(
    data.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Heatmap Korelasi CH dan BANJIR")

plt.savefig(
    "CH_BANJIR_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# =========================
# REKAP HASIL
# =========================
hasil = pd.DataFrame({
    "File": [file],
    "Variabel X": [", ".join(feature_cols)],
    "Variabel Y": [target_col],
    "Persamaan": [equation],
    "R2": [r2],
    "RMSE": [rmse],
    "MAE": [mae],
    "MAPE (%)": [mape]
})

hasil.to_excel(
    "hasil_CH_BANJIR.xlsx",
    index=False
)

print("\n✅ ANALISIS SELESAI!")
print("✔ Heatmap tersimpan sebagai CH_BANJIR_heatmap.png")
print("✔ Rekap hasil tersimpan sebagai hasil_CH_BANJIR.xlsx")