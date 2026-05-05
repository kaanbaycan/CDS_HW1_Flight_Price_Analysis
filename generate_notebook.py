import nbformat as nbf

nb = nbf.v4.new_notebook()

# Title and Intro
nb['cells'] = [
    nbf.v4.new_markdown_cell("# Uçuş Veri Seti Kapsamlı Analizi\nBu notebook, uçuş verileri üzerinde temel istatistikler, aykırı değer tespiti (IQR), korelasyon analizi ve K-Means kümeleme çalışmalarını içermektedir."),
    
    nbf.v4.new_code_cell("import pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nfrom sklearn.cluster import KMeans\nfrom sklearn.preprocessing import StandardScaler\n\n# Estetik ayarlar\nsns.set_theme(style='whitegrid')\nplt.rcParams['figure.figsize'] = (12, 6)\n\n# Veriyi yükleme\ndf = pd.read_csv('Clean_Dataset.csv', index_col=0)\ndf.head()"),
    
    nbf.v4.new_markdown_cell("## 1. Temel İstatistiksel Analiz (Describe)\nVeri setindeki sayısal değişkenlerin merkezi eğilim ve yayılım ölçülerini inceliyoruz."),
    
    nbf.v4.new_code_cell("df.describe()"),
    
    nbf.v4.new_markdown_cell("## 2. Detaylı Aykırı Değer Tespiti (IQR Metodu)\nHer değişken için Q1, Q3 ve IQR değerlerini hesaplayarak alt ve üst sınırları belirliyoruz."),
    
    nbf.v4.new_code_cell("""numeric_cols = df.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    print(f"Sütun: {col}")
    print(f"  IQR: {IQR:.2f} | Sınırlar: [{lower_bound:.2f}, {upper_bound:.2f}]")
    print(f"  Aykırı Değer Sayısı: {len(outliers)}\\n" + "-"*30)"""),
    
    nbf.v4.new_markdown_cell("## 3. Korelasyon Analizi\nDeğişkenler arasındaki doğrusal ilişkiyi inceliyoruz."),
    
    nbf.v4.new_code_cell("corr_matrix = df[numeric_cols].corr()\nsns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.3f')\nplt.title('Korelasyon Matrisi Heatmap')\nplt.show()"),
    
    nbf.v4.new_markdown_cell("## 4. Gelişmiş Kümeleme (K-Means)\nFiyat ve Süre değişkenlerine göre veriyi 4 ana segmente ayırıyoruz."),
    
    nbf.v4.new_code_cell("""X = df[['price', 'duration']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(X_scaled)

sns.scatterplot(data=df.sample(5000), x='duration', y='price', hue='cluster', palette='viridis')
plt.title('K-Means Kümeleme: Fiyat vs Süre')
plt.show()"""),
    
    nbf.v4.new_markdown_cell("## 5. Görselleştirmeler\nDeğişkenlerin dağılımlarını görsel olarak analiz ediyoruz."),
    
    nbf.v4.new_code_cell("""fig, axes = plt.subplots(1, 3, figsize=(18, 5))
for i, col in enumerate(numeric_cols):
    sns.histplot(df[col], kde=True, ax=axes[i], color='skyblue')
    axes[i].set_title(f'{col} Dağılımı')
plt.tight_layout()
plt.show()""")
]

with open('Flight_Analysis.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print("Jupyter Notebook 'Flight_Analysis.ipynb' başarıyla oluşturuldu.")
