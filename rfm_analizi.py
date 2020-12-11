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
