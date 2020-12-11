# Kütüphaneler eklendi.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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
