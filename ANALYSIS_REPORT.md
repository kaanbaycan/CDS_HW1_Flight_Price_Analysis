# Veri Analizi Bulguları (Clean_Dataset.csv)

Bu rapor, uçuş veri seti üzerinde yapılan detaylı istatistiksel analizleri, IQR tabanlı aykırı değer hesaplamalarını ve değişkenler arası ilişkileri içermektedir.

## 1. Temel İstatistikler (Describe)
- **Süre (Duration):** Ortalama 12.22 saat.
- **Kalan Gün (Days Left):** Ortalama 26 gün.
- **Fiyat (Price):** Ortalama 20,889 birim.

## 2. Detaylı Aykırı Değer (IQR) Hesaplamaları
Aykırı değerler $Q1 - 1.5 \times IQR$ ve $Q3 + 1.5 \times IQR$ formülleri kullanılarak tespit edilmiştir.

### A. Uçuş Süresi (Duration)
- **Q1 (25%):** 6.83
- **Q3 (75%):** 16.17
- **IQR:** 9.34
- **Alt Sınır:** -7.18
- **Üst Sınır:** 30.18
- **Tespit Edilen Aykırı Değer:** 2,110 (30.18 saatten uzun uçuşlar)

### B. Kalan Gün (Days Left)
- **Q1 (25%):** 15.00
- **Q3 (75%):** 38.00
- **IQR:** 23.00
- **Alt Sınır:** -19.50
- **Üst Sınır:** 72.50
- **Tespit Edilen Aykırı Değer:** 0 (Veri seti sınırları içerisinde)

### C. Fiyat (Price)
- **Q1 (25%):** 4,783.00
- **Q3 (75%):** 42,521.00
- **IQR:** 37,738.00
- **Alt Sınır:** -51,824.00
- **Üst Sınır:** 99,128.00
- **Tespit Edilen Aykırı Değer:** 123 (99,128 birimden pahalı biletler)

## 3. Korelasyon Analizi
- **Süre ve Fiyat:** 0.204 (Düşük Pozitif)
- **Kalan Gün ve Fiyat:** -0.091 (Negatif)

## 4. Görselleştirme
Detaylı grafikler ve kümeleme analizleri ekteki `histograms.png` ve `cluster_scatter.png` dosyalarında mevcuttur.
