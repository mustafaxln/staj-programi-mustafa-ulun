# Hafta 03 — CLI Uygulamasi ve Git Is Akisi

> 📌 Gorev yoneticisi CLI · branch · commit · push · pull request · merge · conflict

| Bölüm | |
|:---:|:---|
| 📂 | [Ne yaptım](#ne-yaptim) |
| ▶️ | [Nasıl çalıştırılır](#nasil-calistirilir) |
| 💡 | [Ne öğrendim](#ne-ogrendim) |
| 🧩 | [Nerede takıldım](#nerede-takildim) |

---

## Ne yaptim

Bu hafta iki parcali calisma yaptim: terminalden calisan bir **gorev yoneticisi CLI** ve bu kodu **Git branch / PR / merge** akisiyla gelistirme.

<br>

### 📄 `cli_app.py`

Menulu bir dongu ile calisan basit bir gorev listesi uygulamasi:

| Secim | Islev |
|:---:|---|
| 1 | Yeni gorev ekle (`append`) |
| 2 | Gorevleri numarali listele (`for` + `index`) |
| 3 | Numaraya gore gorev sil (`pop`) |
| 4 | Programdan cik (`on_off` bayragi) |

Gorevler program acikken `gorevler` listesinde tutulur; uygulama kapaninca liste sifirlanir (dosyaya kayit yok).

<br>

### 🌿 Git calismasi (`feature/week-03-cli`)

Ozellikleri adim adim feature branch uzerinde gelistirdim, commit attim, GitHub'a push ettim ve **pull request** ile `main` ile birlestirdim. Yerelde de `merge`, **merge conflict** cozme ve branch senkronu denedim.

| Adim | Commit mesaji (ozet) |
|---|---|
| Ilk kayit | `branch test hello world` |
| Cikis menusu | `uygulamaya cikis ozelligi eklendi` |
| Gorev ekleme | `uygulamaya gorev ekleme ozelligi eklendi` |
| Gorev listeleme | `uygulamaya gorev listeleme ozelligi eklendi` |
| Gorev silme | `uygulamaya gorev silme eklendi` |
| Veda mesaji | `uygulamanin sonunda veda mesaji eklendi` |

Detayli Git komutlari ve ornekler: [`cheatsheets/git.md`](../cheatsheets/git.md)

---

## Nasil calistirilir

Python 3 yuklu olmali. Terminalde `week-03` klasorune girip uygulamayi calistirin:

```bash
cd week-03
python3 cli_app.py
```

Menuden 1–4 arasi bir sayi girin. Ornek akis:

```text
--------------------------------
--- CLI Uygulamasi ---
1. Gorev ekle
2. Gorevleri listele
3. Gorev sil
4. Cikis
--------------------------------
Seciminizi yapin: 1
Gorevi girin: alisveris
...
Seciminizi yapin: 4
Program sonlandirildi
```

> ℹ️ Hafta 01–02'deki gibi bu program da `input()` ile etkilesimlidir; secimler sayi (`int`) olarak okunur.

---

## Ne ogrendim

### 🐍 Python (CLI uygulamasi)

- **Menu dongusu:** `while on_off != 1` ile programi acik tutup her turda menuyu tekrar basmayi ogrendim (hafta 01'deki `calculator.py` gibi `if/elif` ile dallanma, ama bu sefer dongu icinde).
- **Liste ile durum tutma:** Gorevleri `gorevler = []` listesinde sakladim; ekleme `append`, silme `pop`, bos liste kontrolu `if gorevler == []`.
- **Numarali listeleme:** `for gorev in gorevler` icinde `gorevler.index(gorev) + 1` ile 1'den baslayan sira numarasi verdim (hafta 02'deki `enumerate` mantigina benzer ama menu numarasi kullaniciya gosterim icin).
- **Silmede indeks:** Kullanici listedeki **sira numarasini** giriyor; `gorevler.pop(int(gorev) - 1)` ile 0 tabanli indekse ceviriyorum. `remove()` ile metin silmeye calisinca `ValueError` almistim — numara ile silmek icin `pop` dogru arac.
- **Sinir kontrolu:** `int(gorev) > len(gorevler)` ise "Gorev bulunamadi" mesaji; gecerli aralikta degilse listeyi patlatmiyorum.

<br>

### 🌿 Git is akisi

- **Untracked dosyalar branch degistirince kaybolmaz:** `cheatsheets/git.md` ve `cli_app.py` once commit edilmeden hem `main` hem `feature/week-03-cli` uzerinde "untracked" olarak gorunuyordu; branch sadece **commit'lenmis** icerigi tasir.
- **Feature branch:** `git checkout -b feature/week-03-cli` ile yeni branch acip ayni anda ona gecmeyi ogrendim.
- **Kucuk, anlamli commit'ler:** Her ozellik (cikis, ekle, listele, sil) ayri commit ile ilerledim; geri almak ve PR'da incelemek kolaylasir.
- **Push ve uzak repo:** `git push origin feature/week-03-cli` ile branch'i GitHub'a gonderdim; remote linkten PR acilabiliyor.
- **Pull request:** Feature'daki degisiklikleri once GitHub'da PR ile `main`'e aldim. Takim calismasinda genelde **dogrudan `main`'e merge yapilmaz**; kod incelemesi ve CI icin PR kullanilir (bunu bu hafta pratik ettim).
- **Pull / fetch:** `git fetch` ve `git pull origin main` ile uzaktaki `main` guncellemelerini yerel `main`'e cektim (ornegin PR merge sonrasi `cli_app.py` main'de de gorundu).
- **Yerel merge:** `git checkout main` → `git merge feature/week-03-cli` ile feature'i main'e birlestirdim.
- **Merge conflict:** Ayni satiri hem `main` hem feature'da farkli sekilde degistirince conflict cikti. Isaretleri (`<<<<<<<`, `=======`, `>>>>>>>`) temizleyip dogru metni birakarak `git add` + `git commit` ile tamamladim.
- **Branch'i guncel tutma:** Conflict sonrasi `feature/week-03-cli` uzerinde `git merge main` (fast-forward) ile feature'i main ile hizaladim.

Conflict ornegi (veda mesaji satiri):

```text
<<<<<<< HEAD
print("Program sonlandirildi")
=======
print("Program sonlandirildi kendine cook iyi bak!")
>>>>>>> feature/week-03-cli
```

Cozumde tek bir `print(...)` satiri birakip conflict isaretlerini sildim.

---

## Nerede takildim

### 🐍 Python

- **SyntaxError:** `secim = int input(...)` yazinca parantez eksikligi; dogrusu `int(input(...))`.
- **ValueError (silme):** `Silinecek gorevi girin: 2` deyip `gorevler.remove(gorev)` kullandim; `gorev` string `"2"`, listede o metin yoktu → `list.remove(x): x not in list`. Cozum: kullanicidan **numara** alip `pop(int(gorev) - 1)` kullanmak.
- **IndentationError / else hizasi:** `if/else` bloklarinda girinti kaymasi; Python'da bloklar boslukla ayrilir, `else` dogru `if` ile hizalanmali.
- **Sinir disi numara:** `4` gorev varken `4` silmek isteyince once hata verdi; `int(gorev) > len(gorevler)` kontrolu ekleyince "Gorev bulunamadi" mesaji geldi.

<br>

### 🌿 Git

- **Main'e dogrudan merge aliskanligi:** Ilk denemelerde feature'i yerelde `main`'e merge ettim; ogrendigim kadariyla ekipte genelde PR uzerinden `main` guncellenir, feature branch'e geri merge ile senkron yapilir.
- **Ayni degisikligi iki branch'te commit:** Veda mesajini hem `main` hem `feature/week-03-cli` uzerinde ayri commit'ledim; sonra `git merge feature/week-03-cli` conflict uretti. Tek branch'te gelistirip digerini merge/pull ile almak daha temiz.
- **PR merge vs yerel main:** GitHub'da PR merge edildikten sonra yerel `main` eski kalabiliyor; `git pull origin main` ile uzak degisiklikleri cekmek gerekiyor.
- **Untracked dosya kafasi:** `git.md` cheatsheet'i hala untracked; branch degistirince "kayboldu" sanilabilir ama commit edilmedigi icin her branch'te ayni durumda duruyor.

---

## Iliskili dosyalar

| Dosya | Rol |
|---|---|
| `week-03/cli_app.py` | Bu haftanin Python uygulamasi |
| `cheatsheets/git.md` | Git komutlari ve ornek terminal ciktilari |
| `cheatsheets/python-basics.md` | Hafta 01 — `input`, `if/elif`, donguler (CLI menusu icin temel) |
| `cheatsheets/python-algorithms.md` | Hafta 02 — liste, `append`, indeks mantigi (gorev listesi icin temel) |
