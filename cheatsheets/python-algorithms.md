# Python Algoritmalar ve Veri Yapilari

> 📌 Liste · `dict` · string · arama · frekans · ek tekrar · hatalar

## Icindekiler

| Bölüm | |
|:---:|:---|
| 📋 | [Liste islemleri](#liste-islemleri) |
| 📦 | [Dict kullanimi](#dict-kullanimi) |
| ✂️ | [String parcala](#string-parcala) |
| 🔍 | [Arama mantigi](#arama-mantigi) |
| 📊 | [Frekans hesaplama](#frekans-hesaplama) |
| 🔁 | [Ek tekrar — ayni problem iki yontem](#ek-tekrar--ayni-problem-iki-yontem) |
| ⚠️ | [Sik yaptigin hatalar](#sik-yaptigin-hatalar) |

---

## 📋 Liste islemleri

### ✂️ Dilimleme / Slicing ([:] ve [::-1])

- Bir listenin belirli bir aralığını kopyalamak veya listeyi ters çevirmek için kullanılır. Orijinal listeyi bozmaz, yeni bir liste üretir.
- Yazdigim koddan ornek vermem gerekirse, `data_structures.py` dosyamizda en yuksek notu alan ogrenciyi bulan fonksiyonumuzda ilk ogrenciyi en yuksek not olarak kabul edip sonra listenin kalanini taramak uzere ele almak icin for `ogrenci in ogrenciler[1:]:` seklinde listemizi slice ile ilk elemani dahil etmicek sekilde dilimledik:

```python
# 4. Bir ogrenci listesi icinde en yuksek notu alan ogrenciyi bulan program
    for ogrenci in ogrenciler[1:]:
```

- Ayni sekilde herhangi bir listeyi ters cevirmek icinde slice dan uygun uctan basla uygun uca kadar geriye dogru git diyerek yardim alabiliriz ornegin:

```python
def liste_ters_cevir(liste):
    """Bir listenin tersini döndürür (kendi orjinalini değiştirmez)."""
    return liste[::-1]
```

<br>

### 🔄 `.reverse()` ile ters cevirme (ek tekrar — yontem 2)

- Ayni problemi ikinci kez `.reverse()` ile cozdum. Bu yontem listeyi **yerinde** ters cevirir; donen referans yine ayni liste nesnesidir.
- `algorithms.py` testinde slice oncesi/sonrasi ve reverse oncesi/sonrasi ayri listelerle kiyasladim:

```python
def liste_reverse_ile_ters_cevir(liste):
    liste.reverse()
    return liste
```

- `[::-1]` → orijinal `[10, 20, 30, 40]` kalir. `.reverse()` → ayni liste `[40, 30, 20, 10]` olur.

<br>

### ➕ Eleman Ekleme (.append())

- Listenin en sonuna yeni bir eleman ekler ve listenin boyutunu dinamik olarak 1 artırır
- Yazdigim koddan ornek vermem gerekirse, `algorithms.py` dosyamizda verilen sayi kadar uzunlugu olan fibonacci dizisi uretirken su sekilde kullandik:

```python
while len(dizi) < n:
        dizi.append(dizi[-1] + dizi[-2])
```

<br>

### 📐 Gömülü Matematiksel Fonksiyonlar (max(), len())

- Listeler üzerinde döngü kurmadan hızlıca analiz yapmamızı sağlar.
- Ornek olarak `algorithms.py` dosyamizda binary searchte sag variablesini belirlemek icin kullandik:

```python
sag = len(liste) - 1
```

- Listenin içindeki en uzun karakter sınırını tek satırda bulduk:

```python
max_uz = max(len(k) for k in kelimeler)
```

<br>

### ⚡ List Comprehension (Gelişmiş Liste Üretimi)

- Klasik for döngüsü yazıp boş listeye append yapmak yerine, tek satırda filtreleme ve liste üretme yöntemidir.
- Sadece uzunluğu maksimuma eşit olan kelimeleri filtreleyip yeni bir liste yaptık, kodumuzdan Örnek:

```python
[k for k in kelimeler if len(k) == max_uz] 
```

<br>

### ⌨️ Ise yarayan komutlar

- `liste.append()` -> Sona eleman ekler.
- `liste.insert()` -> İstenen indekse eleman sıkıştırır.
- `liste.pop()` -> Belirtilen indeksteki elemanı silip döndürür.
- `liste.remove()` -> Belirtilen elemanı bulup ilkini siler.
- `liste.extend()` -> Listenin sonuna başka liste ekler.
- `liste.index()` -> Elemanın indeks numarasını bulur.
- `liste.sort()` -> Listeyi kalıcı olarak sıralar.
- `max(liste)` -> Listedeki en büyük değeri bulur.
- `len(liste)` -> Listenin eleman sayısını verir.

---

## 📦 Dict kullanimi

### 🗂️ Ic ice dict (anahtar -> baska bir dict)

- Dict, anahtar-deger eslesmesi tutar. Mini urun katalogunda her urun id'si (101, 102...) anahtar; deger tarafinda da o urunun `isim`, `fiyat`, `stok` bilgilerini tutan ikinci bir dict vardir. Yani tek sozluk icinde hem urunleri gruplar hem her urunun detayini ayri tutariz.
- Yazdigim koddan ornek vermem gerekirse, `data_structures.py` dosyamizda `urun_katalogu_olustur` fonksiyonunda katalogu su sekilde kurduk:

```python
katalog = {
    101: {"isim": "Laptop", "fiyat": 15000, "stok": 7},
    102: {"isim": "Klavye", "fiyat": 350, "stok": 33},
    103: {"isim": "Mouse", "fiyat": 200, "stok": 42},
    104: {"isim": "Monitor", "fiyat": 2400, "stok": 9},
    105: {"isim": "USB Bellek", "fiyat": 120, "stok": 61},
}
```

<br>

### 🔁 `.items()` ile tum anahtar ve degerleri gezme

- Dict uzerinde dongu kurarken hem urun id'sine hem icindeki bilgi sozlugune ayni anda ulasmak icin `.items()` kullanilir. Her turda `(anahtar, deger)` cifti gelir.
- Katalogu ekrana yazdirirken su kalibi kullandik:

```python
for uid, bilgi in katalog.items():
    print(f"ID: {uid} | Isim: {bilgi['isim']} | Fiyat: {bilgi['fiyat']} TL | Stok: {bilgi['stok']}")
```

<br>

### 🔑 Ic dict'e anahtar ile erisim (`bilgi['isim']`)

- Dis dict'te urunu `katalog[102]` ile buluruz; donen deger yine dict oldugu icin alanlara ikinci koseli parantezle gireriz: `bilgi['fiyat']`, `bilgi['stok']` gibi.
- Fonksiyon sonunda `return katalog` dedigimiz icin bu yapıyı baska yerde de kullanabiliriz; ornek test kodunda tek urun cekmek icin:

```python
ornek_id = 102
if ornek_id in katalog:
    urun = katalog[ornek_id]
    print(f"ID {ornek_id} urunu: Isim: {urun['isim']}, Fiyat: {urun['fiyat']} TL, Stok: {urun['stok']}")
```

<br>

### ✅ `in` ile anahtar kontrolu

- Dict'te bir anahtar var mi diye bakmak icin `if ornek_id in katalog:` yazariz. Yoksa `katalog[999]` KeyError verebilir; once `in` ile kontrol etmek guvenli.
- Liste gibi indeks degil, **anahtar** aranir; katalogumuzda anahtar urun id'sidir (101, 102...).

<br>

### 🔁 `dict.fromkeys` ile duplicate temizleme (ek tekrar — yontem 2)

- `duplicate_temizle` fonksiyonunda dongu + `set` + `append` ile ilk gecis sirasini koruduk. Ayni isi tek satirda `list(dict.fromkeys(liste))` ile de yapilabilir; orijinal liste degismez.
- Testte `[5, 1, 4, 1, 3, 5, 2]` listesinde iki yontem de `[5, 1, 4, 3, 2]` verdi (`True`).
- `sorted(set(liste))` ise `[1, 2, 3, 4, 5]` uretir — tekrar siler ama **ilk sirayi degil, sayisal sirayi** uygular; karistirilmamali.

```python
def duplicate_temizle_dict(liste):
    return list(dict.fromkeys(liste))
```

<br>

### ⌨️ Ise yarayan komutlar

- `dict.keys()` -> Sadece anahtarlari verir.
- `dict.values()` -> Sadece degerleri verir.
- `dict.items()` -> (anahtar, deger) ciftlerini verir.
- `dict.get(anahtar)` -> Anahtar yoksa hata vermeden None veya varsayilan dondurur.
- `anahtar in sozluk` -> Anahtar var mi kontrol eder.

---

## ✂️ String parcala

### 📝 `.split()` ile cumleyi kelimelere ayirma

- Bir string'i bosluklardan (veya verdigin ayiracdan) bolup **liste** haline getirir. Kelime frekansi veya kelime listesi uzerinde islem yapmadan once cumleyi parcalamak icin kullanilir.
- Yazdigim koddan ornek vermem gerekirse, `data_structures.py` dosyamizda `kelime_frekanslari` fonksiyonunda once cumleyi kelimelere ayirdik:

```python
kelimeler = cumle.split()
```

- `"python kolay ve python"` cumlesi `['python', 'kolay', 've', 'python']` listesine donusur; sonra bu liste uzerinde dongu ile dict doldurduk.

<br>

### ⌨️ Ise yarayan komutlar

- `cumle.split()` -> Varsayilan olarak bosluktan boler, kelime listesi verir.
- `cumle.split(',')` -> Virgulden bolmek icin ayirac verirsin.
- `len(kelime)` -> Tek kelimenin karakter uzunlugunu verir (en uzun kelime icin).

---

## 🔍 Arama mantigi

### 👣 Dogrusal arama (`enumerate` ile liste tarama)

- Siralanmamis veya kucuk listelerde bastan sona her elemani kontrol ederiz. Bulursak indeksini dondururuz, bulamazsak `-1`.
- `data_structures.py` dosyamizda `arama_yap` fonksiyonunda hem indeks hem elemana ayni anda ulasmak icin `enumerate` kullandik:

```python
for i, eleman in enumerate(liste):
    if eleman == aranan:
        return i
return -1
```

- Bu yontem her liste icin calisir; ama liste cok buyurse her seferinde bastan sona bakmak yavas kalabilir.

<br>

### ⚡ Binary search (ikiye bolerek arama)

- **Sadece sirali listede** calisir. Ortadaki elemana bakar; aranan buyukse sag yarim, kucukse sol yarima iner. Her adimda arama alani yarilanir.
- `algorithms.py` dosyamizda `binary_search` fonksiyonunda `sol`, `sag` ve `orta` ile araligi daralttik:

```python
sol = 0
sag = len(liste) - 1
while sol <= sag:
    orta = (sol + sag) // 2
    if liste[orta] == aranan:
        return orta
    elif liste[orta] < aranan:
        sol = orta + 1
    else:
        sag = orta - 1
return -1
```

- Testte `sirali = [1, 3, 5, 7, 9, 11, 13]` kullandik; `8` arandiginda `-1` doner cunku listede yok.

<br>

### ↔️ Iki yontemin farki (kisa)

- `arama_yap` -> sirali olmasi sart degil, basit dongu.
- `binary_search` -> liste once siralanmali, ama buyuk listelerde daha verimli mantik.

<br>

### ⌨️ Ise yarayan komutlar

- `enumerate(liste)` -> (indeks, eleman) cifti verir, dogrusal aramada kullanislidir.
- `eleman in liste` -> Var mi diye hizli kontrol (indeks lazim degilse).
- `liste.sort()` -> Binary search oncesi listeyi siralar (orijinali degistirir, dikkat).

---

## 📊 Frekans hesaplama

### 🔢 Dict ile kelime sayaci

- Her kelimenin kac kez gectigini tutmak icin bos bir dict acariz; anahtar kelime, deger sayi (frekans).
- `data_structures.py` dosyamizda `kelime_frekanslari` fonksiyonunda once `split()`, sonra dict ile sayim yaptik:

```python
frekans = {}
for kelime in kelimeler:
    if kelime in frekans:
        frekans[kelime] += 1
    else:
        frekans[kelime] = 1
```

- Kelime daha once gorulduyse `+= 1`, ilk kez goruluyorsa `= 1` ile baslatiyoruz.

<br>

### 🖨️ Sonuclari yazdirma (`.items()`)

- Sayim bitince dict'i gezip ekrana basmak icin yine `.items()` kullandik:

```python
for k, v in frekans.items():
    print(f"{k!r}: {v}")
```

- `{k!r}` kelimeyi tirnak icinde gosterir; hangi kelimenin kac kez gectigini net okuruz.

<br>

### ⌨️ Ise yarayan komutlar

- `kelime in frekans` -> Bu kelime daha once sayildi mi kontrolu.
- `frekans.items()` -> (kelime, adet) ciftlerini gezmek icin.

---

## 🔁 Ek tekrar — ayni problem iki yontem

### 🔄 Liste ters cevirme

- Yontem 1: `return liste[::-1]` — yeni liste, orijinal korunur.
- Yontem 2: `liste.reverse(); return liste` — ayni nesne ters doner.
- Kazanim: fonksiyon cagirisinda “donen liste” ile “parametre olarak verilen liste”nin ayni sey olup olmadigina dikkat etmek.

<br>

### 🧹 Duplicate temizleme

- Yontem 1: `duplicate_temizle` — dongu + `set` + `append`.
- Yontem 2: `duplicate_temizle_dict` — `list(dict.fromkeys(liste))`.
- Kazanim: iki yontem ayni sonucu verebilir; `sorted(set())` ise farkli amac (sirali tekrarsiz liste) — gorevde “ilk sirayi koru” deniyorsa kullanma.

---

## ⚠️ Sik yaptigin hatalar

### 🔍 Binary search icin listeyi siralamadan aramak

- `binary_search` sadece **sirali** listede dogru calisir. `[3, 1, 9, 5]` gibi karisik listeyle denersen yanlis indeks veya `-1` alabilirsin. Once `sort()` veya sirali veri kullan.

<br>

### ↔️ `binary_search` ile `arama_yap`i karistirmak

- `arama_yap` her listeyle calisir; `binary_search` sirali liste ister. Hangi fonksiyonun hangi kosulu gerektirdigini karistirmamak lazim.

<br>

### 🔁 Tekrar bulmak ile tekrari temizlemek farki

- `tekrar_edenleri_bul` (`data_structures.py`) hangi elemanlarin birden fazla gectigini bulur.
- `duplicate_temizle` (`algorithms.py`) listeyi tekrarsiz yeni liste yapar, sirayi korur. Ikisi farkli gorev; ayni fonksiyon sanma.

<br>

### 🔑 Dict'te olmayan anahtara direkt erisim

- `katalog[999]` yazip anahtar yoksa `KeyError` alirsin. Once `if ornek_id in katalog:` kontrolu veya `.get()` kullan.

<br>

### 📭 Bos liste uzerinde islem

- `en_yuksek_notu_bulan` ve `en_uzun_kelimeyi_bul` fonksiyonlarinda bos liste gelince erken cikis (`return None` / `return []`) koyduk; koymazsan `ogrenciler[0]` veya `max(...)` hata verebilir.

<br>

### 🔄 `liste[::-1]` ile `liste.reverse()` karistirmak

- `[::-1]` **yeni liste** uretir, orijinal degismez.
- `.reverse()` listeyi **yerinde** ters cevirir; orijinal liste degisir.
- Ek tekrar testinde iki yontemi **ayni liste** uzerinde denersen sonuc karisir; `orijinal_slice` ve `orijinal_reverse` gibi ayri listeler kullan.

<br>

### ⚠️ `sorted(set())` ile duplicate temizlemek (sira bozulur)

- `duplicate_temizle` ve `duplicate_temizle_dict` ilk gecis sirasini korur (`[5,1,4,3,2]`).
- `sorted(set(tekrarli))` tekrarlari siler ama `[1,2,3,4,5]` gibi **siralar**; “tekrar temizle” gorevinde yanlis arac.

<br>

### ✂️ Slice'ta ilk elemani atlayip baslangic varsayimini unutmak

- `en_yuksek_notu_bulan` icinde ilk ogrenciyi `en_yuksek = ogrenciler[0]` alip donguyu `ogrenciler[1:]` ile baslattik. Ilk elemani hem baslangic hem dongude tekrar kiyaslarsan mantik karisir.
