# Veri Analizi Bulguları (Clean_Dataset.csv)

Bu rapor, uçuş veri seti üzerinde yapılan temel istatistiksel analizleri, aykırı değer tespitini ve değişkenler arası ilişkileri içermektedir.

## 1. Temel İstatistikler (Describe)
- **Süre (Duration):** Ortalama uçuş süresi yaklaşık **12.22 saat**tir. Minimum süre 0.83 saat iken, maksimum süre 49.83 saattir.
- **Kalan Gün (Days Left):** Biletlerin uçuşa ortalama **26 gün** kala alındığı görülmektedir.
- **Fiyat (Price):** Ortalama bilet fiyatı **20,889** birimdir. Standart sapmanın (22,697) ortalamadan yüksek olması, fiyatlarda büyük bir değişkenlik olduğunu (muhtemelen Ekonomi/Business sınıfı farkından dolayı) göstermektedir.

## 2. Aykırı Değerler (Outliers - IQR Yöntemi)
- **Duration:** 2,110 adet aykırı değer tespit edilmiştir. Bu değerler normalden çok daha uzun süren uçuşları temsil eder.
- **Days Left:** Aykırı değer bulunmamaktadır. Veri seti 1-49 gün aralığında homojen dağılmıştır.
- **Price:** 123 adet aykırı değer tespit edilmiştir. Bunlar pazar ortalamasının çok üzerindeki lüks veya son dakika biletlerini temsil edebilir.

## 3. Korelasyon Analizi
- **Süre ve Fiyat (0.204):** Pozitif ancak zayıf bir ilişki vardır. Uçuş süresi arttıkça fiyatın artma eğilimi olsa da bu belirleyici tek faktör değildir.
- **Kalan Gün ve Fiyat (-0.091):** Negatif ve çok zayıf bir ilişki vardır. Genel beklentinin aksine, bu veri setinde uçuşa kalan gün sayısının fiyat üzerindeki doğrudan etkisi (tek başına) düşük görünmektedir.

## 4. Görselleştirme (Histogramlar)
- **Duration:** Veriler sağa çarpıktır (right-skewed). Çoğu uçuş 5-20 saat arasındadır.
- **Days Left:** Neredeyse üniform bir dağılım sergilemektedir; her gün aralığında benzer sayıda veri bulunmaktadır.
- **Price:** Dağılımın bimodal (iki tepeli) olduğu veya geniş bir kuyruğa sahip olduğu gözlenmektedir. Bu durum, farklı kabin sınıflarının fiyatlandırma politikalarını yansıtmaktadır.

---
*Not: Görsel grafikler `histograms.png` dosyasında mevcuttur.*
