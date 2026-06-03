**- degisken**
* Bilgisayarın hafızasında geçici olarak veri saklamak ve bu verilere sonradan isimleriyle kolayca ulaşmak için kullanılır.  
* Etiketli bir kutu gibi dusunebiliriz, kutunun ustune isim yazar icine de bir deger koyariz, daha sonra o degere  ulasmak istedigimizde o isimde ki kutuyu cagiririz.  


**- veri tipleri**
* Veri tipleri degiskenlerin tuttuklari degerin turunu belirler, bunu da etiketli kutularin icine koydugumuz esyanin (verinin) turunu belirtmek icin kullanilir gibi dusunebiliriz.  
* Ornek olarak `int`,`float`,`str`,`bool` gosterilebilir.  
* calculator.py  dosyamizda sayi1 ve sayi2 icin float kullandik mesela, bunun sebebi kullanici eger 10 sayisini 6 sayisina bolmek(/) isterse sonuc kusurlu bir sayi cikicaktir(`1.666`). Eğer `int` kullansaydık program bu küsuratı atıp yanlış sonuç verebilirdi veya hata çıkarabilirdi. `float` veri tipi sayesinde kullanıcının hem küsuratlı sayı girmesine izin verdik hem de bölme gibi işlemlerin sonucunun ondalıklı çıkmasını garanti altına aldık.

**- if/else**
* Programın belirli şartlara göre farklı kararlar vermesini ve farklı kod bloklarını çalıştırmasını sağlamak için kullanılır.  

* `if` : Kontrol edilen ilk şarttır. Şart doğru (True) ise altındaki kod çalışır.

* `elif`: İlk şart yanlışsa, bakılacak diğer alternatif şartları sıralamak için kullanılır.

* `else`: Yukarıdaki şartların hiçbiri uymadığında, en son çare olarak çalışacak varsayılan kod bloğudur.

* sartlar kontrol edilirken `==`, `=!`, `and(&&)`, `or(||)` kullanilir.

* calculator.py dosyamizdan asagidaki kod blogu ile orneklendirebiliriz.  

```python
if secim == '1' or secim == '+':
    sonuc = sayi1 + sayi2
    print("Toplam:", sonuc)

elif secim == '2' or secim == '-':
    sonuc = sayi1 - sayi2
    print("Fark:", sonuc)

elif secim == '3' or seismic == '*':
    sonuc = sayi1 * sayi2
    print("Carpim:", sonuc)

elif secim == '4' or secim == '/':
    if sayi2 != 0:
        sonuc = sayi1 / sayi2
        print("Bolum:", sonuc)
    else:
        print("Bir sayi sifira bolunemez!")

else:
    print("Hatali secim yaptiniz!")
```
**- for**
* Döngüsü (Eleman Tabanlı / Sınırları Belli): Bir listenin, kelimenin veya belirli bir sayı aralığının (range) üzerinden sırayla geçer. Listenin sonuna geldiğinde otomatik olarak durur. "Adım sayısı" baştan bellidir.  

```python
# 1. FOR YÖNTEMİ: Listenin içindeki her bir elemanı ('n') sırayla kendisi yakalar.
# Sayaç artırmaya veya listenin boyuna bakmaya gerek yoktur, otomatik biter.
sum_for = 0
for n in sayilar:
    sum_for += n
```

**- while**
* Döngüsü (Koşul Tabanlı / Sınırları Belirsiz): Başına yazılan şart doğru (True) olduğu sürece dönmeye devam eder. Döngünün bitmesi için içeride o şartı bozacak bir güncelleme (sayaç artırma gibi) yapılması şarttır, yoksa sonsuz döngüye girer.  

```python
# 2. WHILE YÖNTEMİ: Şarta bağlı çalışır. 
# Elimizle bir 'i' indeksi (sayaç) kurup, bunu listenin boyundan küçük olduğu sürece döndürürüz.
# İçeride 'i += 1' diyerek sayacı kendimiz artırmak zorundayız.
sum_while = 0
i = 0
while i < len(sayilar):
    sum_while += sayilar[i]
    i += 1  # Bu satırı unutursak i hep 0 kalır ve program sonsuza kadar döner!
```

**- function**
* Belirli bir görevi yerine getiren kod bloklarını bir çatı altında toplayarak, ihtiyaç duyulduğunda isimleriyle tekrar tekrar çağırabilmek için kullanılır.  
* `def:` Fonksiyon tanımlama (define) kelimesidir.  
* `Parametre / Argüman:` Fonksiyonun çalışması için dışarıdan gönderilen girdilerdir.  
* `return:` Fonksiyonun işini bitirdikten sonra çağrıldığı yere ürettiği sonucu geri fırlatmasıdır. return satırına gelindiğinde o fonksiyonun çalışması anında durur.  
* yazdigim function.py dosyasindan ornek vermek gerekirse:  

```python
# 1. PARAMETRE ALAN VE DEĞER DÖNDÜREN (RETURN) FONKSİYON
def toplama(a, b):
    return a + b  # Gelen iki sayıyı toplar ve çağrıldığı yere cevabı döner.

# 2. ALGORİTMİK VE KOŞULLU FONKSİYON
def palindrom_kontrolu(s):
    s = str(s)
    return s == s[::-1]  # stringi ters çevirip kendisiyle eşit mi diye bakar (True/False döner).

# 3. ERKEN ÇIKIŞ (EARLY RETURN) VE GÜVENLİK KONTROLÜ
def liste_ortalamasi(liste):
    if not liste:
        return None  # Boş liste geldiyse hata vermemesi için erkenden None dönüp fonksiyonu bitirir.
    return sum(liste) / len(liste)
```

**- input alma**
* Dışarıdan kullanıcı ile etkileşime girerek dinamik şekilde çalışması için terminal üzerinden veri toplamak amacıyla kullanılır.  
* `input()` fonksiyonu terminalde çalıştırıldığında programı durdurur ve kullanıcının klavyeden bir şey yazıp `Enter` tuşuna basmasını bekler.  


python3 calculator.py  
`Birinci sayiyi girin: 10`
`Ikinci sayiyi girin: 20`
Yapmak istediginiz islemi secin:
1. Toplama (+)
2. Cikarma (-)
3. Carpma (*)
4. Bolme (/)
`Seciminiz (1/2/3/4): 3`
Carpim: 200.0

**- python dosyasi terminalden nasil calistirilir**
Python dosyasını terminalden çalıştırmak için önce terminalden çalıştırmak istediğimiz dosyanın olduğu konuma gitmemiz lazım. Sonra terminalde şu komutu yollayarak Python dosyasını çalıştırabiliriz: python3 dosya_adi.py

Örneğin week-01 klasöründeki hello.py dosyasını çalıştırmak için sırasıyla şu komutları yazarız:
# Önce dosyanın olduğu klasöre gidiyoruz
cd week-01

# Sonra dosyayı çalıştırıyoruz
python3 hello.py