# Hafta 02 — Python ile Algoritma ve Veri Yapilari

> 📌 Liste · `dict` · arama · frekans · ek tekrar

| Bölüm | |
|:---:|:---|
| 📂 | [Ne yaptım](#ne-yaptim) |
| ▶️ | [Nasıl çalıştırılır](#nasil-calistirilir) |
| 💡 | [Ne öğrendim](#ne-ogrendim) |
| 🧩 | [Nerede takıldım](#nerede-takildim) |

---

## Ne yaptim

Python ile liste, dict ve temel algoritma calismalari yaptim. Gorevleri iki dosyaya ayirdim:

<br>

### 📄 `data_structures.py`

| Fonksiyon | Aciklama |
|---|---|
| `arama_yap` | Liste icinde aranan elemani `enumerate` ile arar, indeks dondurur |
| `tekrar_edenleri_bul` | Tekrar eden elemanlari bulur |
| `kelime_frekanslari` | Cumledeki kelime frekanslarini `dict` ile hesaplar |
| `en_yuksek_notu_bulan` | Ogrenci listesinde en yuksek notu alani bulur |
| `urun_katalogu_olustur` | ID → urun bilgisi ic ice `dict` katalogu olusturur |

<br>

### 📄 `algorithms.py`

| Fonksiyon | Aciklama |
|---|---|
| `fibonacci` | n terimli Fibonacci dizisi uretir |
| `binary_search` | Sirali listede ikiye bolerek arama yapar |
| `liste_ters_cevir` | Listeyi `[::-1]` ile ters cevirir (orijinali degismez) |
| `liste_reverse_ile_ters_cevir` | Ayni isi `.reverse()` ile yapar (orijinal liste degisir) |
| `duplicate_temizle` | Tekrar edenleri dongu +  `set` ile temizler, sirayi korur |
| `duplicate_temizle_dict` | Ayni isi `dict.fromkeys` ile yapar |
| `en_uzun_kelimeyi_bul` | En uzun kelime(ler)i list comprehension ile bulur |

<br>

### 🔁 Ek tekrar (ayni problem, iki yontem)

Staj gorevinde iki problemi farkli yontemle cozup `algorithms.py` icindeki testlerle farklari gosterdim:

| Problem | Yontem 1 | Yontem 2 | Testte gorulen fark |
|---|---|---|---|
| Liste ters cevirme | `liste_ters_cevir` → `[::-1]` | `liste_reverse_ile_ters_cevir` → `.reverse()` | Slice orijinali bozmaz; reverse ayni listeyi yerinde ters cevirir |
| Duplicate temizleme | `duplicate_temizle` → dongu + `set` | `duplicate_temizle_dict` → `dict.fromkeys` | Sonuc ayni (`[5,1,4,3,2]`); `sorted(set())` ise sirayi bozar (`[1,2,3,4,5]`) |

---

## Nasil calistirilir

Python 3 yuklu olmali. Terminalde `week-02` klasorune girip dosyalari calistirin:

```bash
cd week-02
python3 data_structures.py
python3 algorithms.py
```

> ℹ️ Her iki dosya da `if __name__ == "__main__":` blogu icinde fonksiyon testlerini calistirir ve ornek ciktilari ekrana basar.

> 🔁 `algorithms.py` calistirildiginda **ek tekrar** karsilastirma ciktilari da gelir (`Liste ters cevirme — iki yontem`, `Duplicate temizleme — iki yontem` basliklari).

---

## Ne ogrendim

### 📋 Liste & dict

- bazi liste islemleri orjinal listeyi degistirirken bazi liste islemlerinin orjinalini degistirmedigini ogrendim.
- `enumerate(liste)` ile hem indeks hem elemana ayni dongude ulasip dogrusal arama yapmayi ogrendim (`arama_yap`).
- `set` kullanarak daha once gorulen elemanlari takip edip tekrar edenleri ayirt etmeyi ogrendim (`tekrar_edenleri_bul`).
- Cumleyi `split()` ile kelime listesine cevirdikten sonra `dict` ile frekans saymayi ogrendim; kelime varsa `+= 1`, yoksa `= 1` (`kelime_frekanslari`).
- Tuple listelerinde `ogrenci[1]` ile nota erisip, `ogrenciler[0]` baslangic alip `ogrenciler[1:]` ile kalanini tarayarak en yuksek notu bulmayi ogrendim.
- Bos liste gelince erken `return None` ile programin patlamamasini saglamayi ogrendim (`en_yuksek_notu_bulan`).
- Ic ice `dict` yapisi: dis anahtar urun id, ic dict `isim` / `fiyat` / `stok`; `.items()` ve `katalog[id]` ile gezmeyi ogrendim (`urun_katalogu_olustur`).
- Dict'te anahtar yokken `if ornek_id in katalog:` ile kontrol etmeden erismemek gerektigini ogrendim.

<br>

### 🔍 Algoritmalar

- `binary_search` icin listenin **sirali** olmasi gerektigini; `sol`, `sag`, `orta` ile araligi her adimda daraltmayi ogrendim.
- `liste[::-1]` ile ters listeyi **yeni liste** olarak alip orijinalin degismedigini gordum (`liste_ters_cevir`).
- Tekrar **bulmak** (`tekrar_edenleri_bul`) ile tekrari **temizleyip yeni liste** uretmek (`duplicate_temizle`) farkli isler; ikincisinde sirayi `append` ile korudum.
- `fibonacci` icin `while len(dizi) < n` ve `dizi[-1] + dizi[-2]` ile diziyi buyutmeyi ogrendim.
- `max(len(k) for k in kelimeler)` ve list comprehension ile filtreleme yapmayi ogrendim (`en_uzun_kelimeyi_bul`); bos listede `return []` kontrolu ekledim.

<br>

### 🔁 Ek tekrar

- Ek tekrar: ayni isi iki yontemle yazinca sadece sonuc degil **yan etki** de onemli — `liste_ters_cevir` orijinal listeyi korurken `liste_reverse_ile_ters_cevir` girdigi listeyi kalici degistirir; testte iki ayri `orijinal_*` listesi kullanarak bunu net gordum.
- Ek tekrar: `duplicate_temizle` (dongu + `set`) ile `duplicate_temizle_dict` (`list(dict.fromkeys(liste))`) ayni tekrarsiz listeyi verir; ikinci yol daha kisa, ilki adim adim daha okunur.
- `sorted(set(liste))` tekrarlari silse de **ilk gecis sirasini korumaz**; `[5,1,4,1,3,5,2]` orneginde dongu/dict `[5,1,4,3,2]` verirken `sorted(set())` `[1,2,3,4,5]` verir — “tekrar temizle” ile “sirala” karistirilmamali.
- Ayni problemi iki yontemle cozmenin kazanimi: hangi yontemin orijinal veriyi bozdugunu, hangisinin kisa yazildigini ve test ciktisiyla `==` karsilastirmasi yaparak farki kanitlamayi ogrendim.

---

## Nerede takildim

### 🧠 List comprehension (`en_uzun_kelimeyi_bul`)

- Asagidaki kod blogunda takildim, aslinda uzun olarak  3 4 satir halinde yazildiklarinda anlamasi cok basit seyler oldugunu gordum sadece tek satir kisaltmalari biraz kafa karistirici oldu benim icin, gerekli arastirmalari yaparak eksiklerimi tamamladim.

```python
max_uz = max(len(k) for k in kelimeler) 
[k for k in kelimeler if len(k) == max_uz]
```

- `max_uz = max(len(k) for k in kelimeler)` Bu tek satırın arka planda yaptığı iş tam olarak şudur:

```python
uzunluklar = []
for k in kelimeler:
    uzunluklar.append(len(k))  # Her kelimenin uzunluğunu listeye ekle

max_uz = max(uzunluklar)  # Sonra bu uzunlukların en büyüğünü seç
```

- `[k for k in kelimeler if len(k) == max_uz]`
- for k in kelimeler: Klasik döngümüz. Listedeki her kelimeye sırayla k diyoruz.
- if len(k) == max_uz: Filtremiz. Sadece uzunluğu max_uz olanları içeri al diyoruz.
- En baştaki tek başına duran k: "Eğer filtreden geçebilirse, yeni listenin içine bu k kelimesinin bizzat kendisini fırlat" anlamına geliyor.

<br>

### 📌 Diger konular

- `binary_search` yazarken listeyi siralamadan denedim; karisik listede sonuc yanlis geliyordu. Sonra testte `sirali = [1, 3, 5, 7, 9, 11, 13]` kullaninca mantigin sadece sirali listede calistigini anladim.
- `arama_yap` ile `binary_search`i karistirdim. Biri bastan sona `enumerate` ile bakiyor, digeri ortadan ikiye boluyor; hangi fonksiyonda hangi kosulun sart oldugunu not alarak ayirdim.
- `tekrar_edenleri_bul` ile `duplicate_temizle` isimleri benzer geldi; biri tekrar eden **elemanlari raporluyor**, digeri listeyi **temizleyip yeni liste** donduruyor. Ayni `set` mantigina benzeseler de gorev farkli.
- Urun katalogunda `bilgi['isim']` yazarken bazen tek `[]` ile yetinip ic dict alanlarina ulasamadim; `katalog[102]` sonrasi ikinci kez anahtar (`'fiyat'`, `'stok'`) gerektigini yazarak cozdum.
- Olmayan urun id ile `katalog[999]` deneyince `KeyError` aldim; test kodunda `if ornek_id in katalog:` kontrolunu ekleyince duzeldi.
- `en_yuksek_notu_bulan` icinde donguyu `ogrenciler`in tamamina kurup ilk ogrenciyi iki kez kiyaslamaya calistim; `en_yuksek = ogrenciler[0]` ve `for ogrenci in ogrenciler[1:]` ayrimini yapinca mantik netlesti.
- Bos ogrenci listesi verince `ogrenciler[0]` satirinda hata aldim; `if not ogrenciler: return None` kontrolunu eklemek zorunda kaldim.
- `kelime_frekanslari` icinde cumleyi bolmeden donguye girmeye calistim; once `cumle.split()` yapmadan kelime kelime sayimin calismayacagini fark ettim.
- `liste_ters_cevir` sonrasi orijinal listenin degisip degismedigini karistirdim; `[::-1]` yeni liste veriyor, `.reverse()` ise yerinde degistiriyor — testte `orijinal` listeyi tekrar yazdirarak kontrol ettim.
- `fibonacci(0)` ve `fibonacci(1)` gibi kenar durumlarda bos veya tek elemanli liste donmek gerektigini; `n <= 0` ve `n == 1` ayri ele alinmazsa dongunun yanlis calistigini gordum.
- `enumerate` kullanimini ilk basta `for i in range(len(liste))` ile yazmaya calistim; `for i, eleman in enumerate(liste)` ile hem daha kisa hem daha okunur oldugunu fark ettim (`arama_yap`).
- Ek tekrar testlerinde once `liste_ters_cevir` ve `liste_reverse_ile_ters_cevir`i ayni `orijinal` listesi uzerinde arka arkaya denedim; reverse sonrasi listenin zaten ters donmus olmasi slice testini karistirdi — iki ayri liste (`orijinal_slice`, `orijinal_reverse`) kullaninca fark netlesti.
- Duplicate karsilastirmasinda ilk basta sadece `set()` kullandim; sonuc sayilari dogru gelse de `[5,1,4,3,2]` yerine baska sira cikabilecegini `sorted(set())` ile kiyaslayinca anladim; gorev “sirayi koru” diyorsa `dict.fromkeys` veya dongu + `append` gerekir.
