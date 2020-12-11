# Kütüphaneler eklendi.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt

# bütün gözlemleri ve değişkenleri (satır ve sütunlar) görebilmek için :
pd.set_option('display.max_columns', None);
pd.set_option('display.max_rows', None);

# virgulden sonra gösterilecek olan sayı sayısı
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# veri setimizi okuyoruz :

original_df = pd.read_excel("data/online_retail_II.xlsx", sheet_name="Year 2010-2011")

# verimiz okundu mu? ilk 5 gözleme bakalım :
original_df.head()

# Daha sonraları verimizin silinmesi veya bozulması
# ihtimaline karşı, orjinal veri setini kopyalayalım :

df = original_df.copy()

# veri setimizin değişkenleri hakkında bilgi alalım :
df.info()

# veri setimizde 8 değişken var : 3 sayısal, 4 kategorik ve 1 tane de tarih

# veri setimizin herhangi bir yerinde eksik bilgi var mı diye bakalım :
# yazdığımız kod dataframe içinde, herhangi bir değerde bir eksik bilgi varsa True dönecektir.
df.isnull().values.any()

# bu eksik değerlerin, hangi değişkenlerde ve toplamda kaç adet olduğuna bakalım :
df.isnull().sum()

# veri setimizin değişkenlerine bakalım :
df.columns

# şimdi bu değişkenlerin bazılarında kaç tane eşsiz (birbirinden farklı) değer olduğuna bakalım :
print("Description : ", df["Description"].nunique())
print("StockCode : ", df["StockCode"].nunique())

# bu değişkenlerde toplamda kaç adet eleman (değer) olduğuna bakalım

print("Description : ", df["Description"].value_counts().sum())
print("StockCode : ", df["StockCode"].value_counts().sum())

# RFM ANALİZİNE GEÇELİM

# öncelikle eksik gözlemlerimizi silelim. eksik verileri doldurmanın çeşitli yolları var ama biz uzatmamak için siliyoruz.
# bu elbette bazı yan etkilere sahip olacaktır ama şuan bunu düşünmemize gerek yok.

pure_df = df.dropna()

# eksik gözlemler silinmiş mi ?
pure_df.isnull().values.any()

# eksik gözlem yok, peki değişkenlerin kaç adet elemanları kaldı, sağlaması?
pure_df.isnull().sum()

# Bu veri setindeki faturada C : geri iade edilen faturayı temsil eder. Yani negatif işleme girer. Biz bu değerleri de çıkarıyoruz :
pure_df = pure_df[~pure_df["Invoice"].str.contains("C", na=False)]

# elimizde kaç adet gözlem birimi var ?
pure_df.shape

# RFM için maksimum gelir lazım olacak bu yüzden TotalPrice değişkeni oluşturacağız :
pure_df["TotalPrice"] = pure_df["Quantity"] * pure_df["Price"]

# biraz verimizi inceleyelim. bunun için önceki haline ve şuanki haline bakabiliriz.

# önceki:
df.describe().T

# şimdiki
pure_df.describe().T

"""
Recency : Müşterinin son satın almasından bugüne kadar geçen süre

Frequency : Toplam satın alma sayısı

Monetary : Müşterinin yaptığı toplam harcama
"""

# Veri setinin en son ne zaman veri tuttuğuna bakalım. Şuan Tarih 2020 fakat biz bu tarihi baz alırsak çok yanlış yaparız :)
pure_df["InvoiceDate"].max()

# burada görüyoruz ki son tarih 2011 yılının, 12. ayının 9. günü.
# bu yüzden biz de aynı tarihlerin bir gün sonrasını alalım yani 10. günü ki güzel bir sonuç alalım.
last_time = dt.datetime(2011, 12, 10)

#  Müşterilerin son satın alımlarından itibaren, son tarihe göre kaç gün geçmiş bakalım :
# önce geçici df oluşturalım
temp_df = (last_time - pure_df.groupby("Customer ID").agg({"InvoiceDate": "max"}))
temp_df.head()

# InvoiceDate değişkenini yeniden isimlendirelim :
temp_df.rename(columns={"InvoiceDate": "Recency"}, inplace=True)
temp_df.head()

# recency df oluşturalım ve bu df, ek saat ve dakikalrı içermesin
# burada geçici dfteki, recency değişkeninin her bir elemana eriştik, bunların günlerini aldık.

recency_df = temp_df["Recency"].apply(lambda x: x.days)
recency_df.head()

# Frequency İçin İşlemler

# yeni df oluşturduk. bunu Customer ID ye göre gruplayıp, Fatura tarihinin eşsiz değerlerine göre yaptık.
# yani bir kullanıcı kaç farklı fatura ödemiş bunu tuttuk.
freq_df = pure_df.groupby("Customer ID").agg({"InvoiceDate": "nunique"})

# değişken ismine sıklık dedik
freq_df.rename(columns={"InvoiceDate": "Frequency"}, inplace=True)
freq_df.head()

# Monetary İçin İşlemler

# Kullanıcılara göre gurp çektik ve bu kullanıcıların her bir alışverişin toplamını yeni df'e atadık.
monetary_df = pure_df.groupby("Customer ID").agg({"TotalPrice": "sum"})

# Değişkeni yeniden isimlendirdik.
monetary_df.rename(columns={"TotalPrice": "Monetary"}, inplace=True)

monetary_df.head()

# şimdi elimizdeki ayrı 3 yeni dfin bilgilerine bakalım :

print(recency_df.shape, freq_df.shape, monetary_df.shape)

# bu 3 dataframi, tek bir dataframe de birleştirelim :
rfm = pd.concat([recency_df, freq_df, monetary_df], axis=1)
rfm.head()

# yeni bir değişken oluşturalım ve buna RecencyScore diyelim.
rfm["RecencyScore"] = pd.qcut(rfm["Recency"], 5, labels=[5, 4, 3, 2, 1])
rfm.head()

# aynı işlemi frequency ve monetary için yapalım
rfm["FrequencyScore"] = pd.qcut(rfm["Frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
rfm["MonetaryScore"] = pd.qcut(rfm['Monetary'], 5, labels=[1, 2, 3, 4, 5])
rfm.head()

# rfm skorları kategorik değere dönüştürülüp df'e eklendi
rfm["RFM_SCORE"] = (rfm['RecencyScore'].astype(str) +
                    rfm['FrequencyScore'].astype(str) +
                    rfm['MonetaryScore'].astype(str))

rfm.head()

# rfm içinde koşul çalıştıralım ve bu koşulun ilk 5 gözlemine bakalım :
# burada değişkeni "555" e eşit olan gözlemler gözükürken bunların ilk 5ine bakalım
rfm[rfm["RFM_SCORE"] == "555"].head()

# Regular Expressions (Düzenli İfadeler) kullanılarak RFM haritası çıkarıldı
seg_map = {
    r'[1-2][1-2]': 'Hibernating',
    r'[1-2][3-4]': 'At Risk',
    r'[1-2]5': 'Can\'t Loose',
    r'3[1-2]': 'About to Sleep',
    r'33': 'Need Attention',
    r'[3-4][4-5]': 'Loyal Customers',
    r'41': 'Promising',
    r'51': 'New Customers',
    r'[4-5][2-3]': 'Potential Loyalists',
    r'5[4-5]': 'Champions'
}

# rfm içinde "Segment" isimli değişken oluşturduk ve bu değişkeni 2 string birleştirerek yaptık.
rfm['Segment'] = rfm['RecencyScore'].astype(str) + rfm['FrequencyScore'].astype(str)
rfm.head()

# Segment değişkeninin elemanlarının her birini, yukarıdaki regex ifadesndeki karşılıkları ile değiştirdik.
rfm['Segment'] = rfm['Segment'].replace(seg_map, regex=True)
rfm.head()

rfm[["Segment", "Recency", "Frequency", "Monetary"]].groupby("Segment").agg(["mean", "median", "count"])


# RFM İşlemleri Sonrası Öneriler

champions = rfm[rfm["Segment"] == "Champions"]["Monetary"].sum()
need_attentions = rfm[rfm["Segment"] == "Need Attention"]["Monetary"].sum()
new_customers = rfm[rfm["Segment"] == "New Customers"]["Monetary"].sum()
genel_toplam = rfm["Monetary"].sum()

print("Toplam Gelir : ",genel_toplam)
print("Şampiyonların Harcadığı Tutar : ",champions)
print("Aksiyon Bekleyenlerin Harcadığı Tutar : ",need_attentions)
print("Yeni Müşterilerin Harcadığı Tutar : ",new_customers)

def yuzde_hesapla(x):
    return x*100/genel_toplam

print("Şampiyonların Genel Toplamdaki Harcama Yüzdesi %: ", yuzde_hesapla(champions))
print("Aksiyon Bekleyenlerin Genel Toplamdaki Harcama Yüzdesi %: ", yuzde_hesapla(need_attentions))
print("Yeni Müşterilerin Genel Toplamdaki Harcama Yüzdesi %: ", yuzde_hesapla(new_customers))