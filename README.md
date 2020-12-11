## *RFM Analizi*

#### ***Veri Seti Hikayesi*** :
###### Bu, Birleşik Krallık merkezli ve kayıtlı mağaza dışı çevrimiçi perakende için 01/12/2010 ve 09/12/2011 arasında gerçekleşen tüm işlemleri içeren uluslararası bir veri kümesidir. Şirket esas olarak her durumda benzersiz hediyeler satmaktadır. Firmanın birçok müşterisi toptancıdır.

#### ***Değişkenler*** :
###### InvoiceNo: Fatura numarası. Nominal, her işleme benzersiz bir şekilde atanan 6 basamaklı bir integral numarası. Bu kod 'c' harfiyle başlıyorsa, bir iptal olduğunu gösterir.
###### StockCode: Ürün (öğe) kodu. Nominal, her farklı ürüne benzersiz şekilde atanmış 5 basamaklı bir integral numarası.
###### Description: Ürün (öğe) adı. Nominal.
###### Quantity: İşlem başına her bir ürünün (kalem) miktarı. Sayısal.
###### InvoiceDate: Fatura Tarihi ve saati. Sayısal, her işlemin oluşturulduğu gün ve saat.
###### UnitPrice: Birim fiyatı. Sayısal, Birim başına sterlin ürün fiyatı.
###### CustomerID: Müşteri numarası. Nominal, her müşteriye benzersiz şekilde atanmış 5 basamaklı bir integral numarası.
###### Country: Ülke adı. Nominal, her müşterinin ikamet ettiği ülkenin adı.

#### ***Problem*** :
###### Müşterilerin segmentlere ayrılıp, seçilen 3 segment için aksiyon planı yapılması istenmektedir.
###### Müşterilerin segmentlere ayrılıp aksiyon planı yapılması sektörde önemli bir yer kaplamaktadır.

###### Veri setine buradan ulaşabilirsiniz : *https://www.kaggle.com/mathchi/online-retail-data-set-from-ml-repository*