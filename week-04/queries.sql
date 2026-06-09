-- 1. En cok siparis veren kullanici
SELECT u.name, u.email, COUNT(*) AS siparis_sayisi      --group by sonrasi id isim ve mail ve count sutunlarindan bir tablo olusturuyoruz ve counta da siparis_sayisi diyoruz
FROM users u                                                  --users tablosunu u diye kisalttik
JOIN orders o ON u.id = o.user_id                             --orders tablosunu o diye kisaltip verilen sarta gore users ve orders tablosunu birlestirdik
GROUP BY u.id, u.name, u.email                                --tablolarin birlesmesi sonrasi id name ve emaile gore grupluyoruz bunun sonucunda ali 2 satir ayse 1 satir gibi bi sonuc elde ediyoruz        
ORDER BY siparis_sayisi DESC                                  --select sonrasi olusan tabloyu siparis sayisi'na gore azalan sekilde siraliyoruz
LIMIT 1;                                                      --sadece 1 satir olsun diyoruz ve encok siparis vereni buluyoruz

-- 2. En cok satilan urun
SELECT p.name, SUM(oi.quantity) AS toplam_adet              --group by sonrasi name ve toplam adet sutunlarindan bir tablo olusturuyoruz ve sum'a da toplam_adet diyoruz
FROM products p                                               --products tablosunu p diye kisalttik
JOIN order_items oi ON p.id = oi.product_id                     --order_items tablosunu oi diye kisaltip verilen sarta gore products ve order_items tablosunu birlestirdik
GROUP BY p.id, p.name                                         --tablolarin birlesmesi sonrasi id ve name'e gore grupluyoruz bunun sonucunda usb kablo 2 satir kitap 2 satir gibi bi sonuc elde ediyoruz
ORDER BY toplam_adet DESC                                     --select sonrasi olusan tabloyu toplam adet'e gore azalan sekilde siraliyoruz
LIMIT 1;                                                      --sadece 1 satir olsun diyoruz ve en cok satilan urunu buluyoruz