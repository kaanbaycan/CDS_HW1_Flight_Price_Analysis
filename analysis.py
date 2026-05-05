import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
df = pd.read_csv('Clean_Dataset.csv', index_col=0)

# 1) Describe
desc = df.describe()
print("--- DESCRIBE ---")
print(desc)
print("\n")

# 2) Outlier Detection (IQR Method)
numeric_cols = df.select_dtypes(include=[np.number]).columns
outliers_summary = []

print("--- DETAILED IQR OUTLIER ANALYSIS ---")
for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    
    col_info = {
        'column': col,
        'Q1': Q1,
        'Q3': Q3,
        'IQR': IQR,
        'lower_bound': lower_bound,
        'upper_bound': upper_bound,
        'count': len(outliers)
    }
    outliers_summary.append(col_info)
    
    print(f"Column: {col}")
    print(f"  Q1 (25%): {Q1:.2f}")
    print(f"  Q3 (75%): {Q3:.2f}")
    print(f"  IQR: {IQR:.2f}")
    print(f"  Lower Bound: {lower_bound:.2f}")
    print(f"  Upper Bound: {upper_bound:.2f}")
    print(f"  Outliers Detected: {len(outliers)}")
    print("-" * 30)

print("\n")

# 3) Correlation
correlation = df[numeric_cols].corr()
print("--- CORRELATION ---")
print(correlation)
print("\n")

# 4) Histograms
plt.figure(figsize=(15, 5))
for i, col in enumerate(numeric_cols):
    plt.subplot(1, len(numeric_cols), i+1)
    sns.histplot(df[col], kde=True)
    plt.title(f'Histogram of {col}')

plt.tight_layout()
plt.savefig('histograms.png')
print("Histograms saved to histograms.png")
