## *RFM Analizi*

#### ***Veri Seti Hikayesi*** :
###### Bu, Birleşik Krallık merkezli ve kayıtlı mağaza dışı çevrimiçi perakende için 01/12/2010 ve 09/12/2011 arasında gerçekleşen tüm işlemleri içeren uluslararası bir veri kümesidir. 
###### Şirket esas olarak her durumda benzersiz hediyeler satmaktadır. Firmanın birçok müşterisi toptancıdır.

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


## *İşlemler Sonrası Aksiyon Planı Önerileri*

#### :red_circle: Şampiyonlar İçin Yorumlar

###### :small_orange_diamond: Şampiyonlar bu işletmenin gelirlerinin *%49'a* yakınını oluşturuyor. Bu nedenle bu kişileri kaybetmememiz gerekiyor. 
###### Fakat bu kişiler zaten bizden sık ve çok alışveriş yapıyorlar. Bu kişilere çok indirim yapmak, kazandırdıkları parayı düşürebilir. 
###### Bir insan olarak sık alışveriş yaptığımız yerden diğerlerine göre ayrıcalık bekleriz. O halde bu işletme :

###### :small_orange_diamond: 1-Şampiyonlara özel üyelik sistemi getirmeli. Üyelik sisteminde ***%3-7 belki %10'lara*** varan indirimler yapılabilir. 
###### Bu indirimler sürekli olmamalı ve genel indirim zamanlarına da denk gelmemeli. Belki süreli indirim olabilir. Her ay başlangıcından itibaren 1 hafta gibi bir süre bu indirimlerden yararlanabilirler.

###### :small_orange_diamond: 2-Bu kişilere zaman zaman güzel dileklerde bulunmak, önemli hissettirecek mesajlar atmak değerli hissettirecektir ve bu da kalıcılığı arttıracaktır. Her insan, önemli hissetmeyi sever.

###### :small_orange_diamond: 3-Promosyon linkleri olmalı ve bunlar da ödüllendirilmeli. Yeni bir müşteri getirme başına bir hediye sistemi olabilir. Bu ayrıca yeni müşteri de çekecektir.


#### :green_circle: Need Attention İçin Yorumlar

###### :small_blue_diamond: Bu kişiler işletmenin gelirlerinin yaklaşık %2'sini oluşturmakta. 
###### :small_blue_diamond: Bu kişiler bizden yeterince alışveriş yapıyorlar fakat arzu ettiğimiz geliri bize kazandırmıyorlar.

###### :small_blue_diamond: 1- Bu kişilerin alışveriş faturaları incelenmeli, apriori gibi algoritmalarla analiz edilmeliler. 
###### Bu şekilde fazla ürün almaları sağlanmaya çalışılabilir.

###### :small_blue_diamond: 2- Zaman zaman hatırlatıcı mesajlar atılmalı fakat sık olursa bu kişide hoşnutsuzluğa sebep olabilir. Bu yüzden ayda 1 veya 2 mesaj atılabilir. 
###### Bu mesajlar iyi dilekler içermeli belki de birkaç gün geçerli %10-15 indirim kuponu sağlanmalı ya da 3 al 2 öde şeklinde kampanyaların olduğu haber edilmeli.

#### :purple_circle: Yeni Müşteriler İçin Yorumlar

###### :small_orange_diamond: Yeni müşteriler bir işletmede kan tazeletecektir. Yeni ürünlerin satılması imkanı sağlayabilir, yeni pazar payları elde etmeye araç olabilirler. 
###### Her insan yeni bir yere girdiğinde bir gariplik hisseder ve araştırmak, güvende olma isteği duyar. Bu yüzden bu kişilere :

###### :small_orange_diamond: 1- Güvenlice alışveriş yapabileceklerine dair 1-2 bilgilendirici mesaj gönderilebilir.

###### :small_orange_diamond: 2- Yeni gelenlere özel küçük promosyonlar yapılabilir. X ürünü alana Y ürünü %10 indirimli gibi kampanyalar yapılabilir.

###### :small_orange_diamond: 3- İlk 3 alışverişte %5-10 arasında indirim uygulanabilir.

###### :small_orange_diamond: 4- Çok fazla reklam göstermek müşteride negatif etki yapacaktır. Belli başlı reklamlar veya haberler müşterinin ilgisini çekebilir.
