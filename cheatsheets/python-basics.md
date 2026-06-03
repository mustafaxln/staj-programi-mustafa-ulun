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


**- while**


**- function**


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