import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Set aesthetic style
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams['figure.figsize'] = (12, 8)

# Load dataset
df = pd.read_csv('Clean_Dataset.csv', index_col=0)

# 1. Advanced Clustering
# We'll cluster based on price and duration to find 'segments' of flights
features = ['price', 'duration']
X = df[features]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-Means clustering (let's use 4 clusters for distinct segments: Short-Cheap, Short-Expensive, Long-Cheap, Long-Expensive)
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(X_scaled)

# Analyze variance reduction
total_price_std = df['price'].std()
cluster_price_stds = df.groupby('cluster')['price'].std()

print("--- VARIANCE ANALYSIS ---")
print(f"Global Price Std Dev: {total_price_std:.2f}")
for i, std in enumerate(cluster_price_stds):
    count = len(df[df['cluster'] == i])
    print(f"Cluster {i} Price Std Dev: {std:.2f} (n={count})")
print("\n")

# 2. Enhanced Visualizations

# A. Cluster Scatter Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df.sample(5000), x='duration', y='price', hue='cluster', palette='viridis', alpha=0.6)
plt.title('Flight Segments: Price vs Duration (Clustered)', fontsize=15)
plt.savefig('cluster_scatter.png')
plt.close()

# B. Improved Distribution (KDE)
plt.figure(figsize=(10, 6))
for i in range(4):
    sns.kdeplot(df[df['cluster'] == i]['price'], label=f'Cluster {i}', fill=True)
plt.title('Price Distribution by Cluster', fontsize=15)
plt.legend()
plt.savefig('cluster_kde.png')
plt.close()

# C. Class vs Price Boxplot (Showing how 'class' naturally clusters)
plt.figure(figsize=(10, 6))
sns.boxenplot(data=df, x='class', y='price', palette='magma')
plt.title('Price Distribution by Travel Class', fontsize=15)
plt.savefig('class_boxplot.png')
plt.close()

print("Advanced visualizations saved.")
