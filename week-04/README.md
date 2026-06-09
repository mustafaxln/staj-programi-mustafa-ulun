# Hafta 04 — SQL ve Veritabani

> 📌 SQLite · tablo tasarimi · seed · sorgular · Python `sqlite3`

| Bölüm | |
|:---:|:---|
| 📂 | [Ne yaptım](#ne-yaptim) |
| ▶️ | [Nasıl çalıştırılır](#nasil-calistirilir) |
| 💡 | [Ne öğrendim](#ne-ogrendim) |
| 🧩 | [Nerede takıldım](#nerede-takildim) |

---

## Ne yaptim

Bu hafta iki parcali calisma yaptim: **SQL ile veri modeli kurma** ve **Python ile sorgu calistirma**.

<br>

### 📄 `create_tables.sql`

Basit bir e-ticaret veri modeli icin 4 tablo tanimladim:

| Tablo | Ne tutar? |
|---|---|
| `users` | Siparis veren kullanicilar (`id`, `name`, `email`) |
| `products` | Satilan urunler ve fiyatlari (`id`, `name`, `price`) |
| `orders` | Siparis ozeti: kim, ne zaman, toplam tutar (`user_id` → `users`) |
| `order_items` | Siparisteki her urun satiri (`order_id`, `product_id`, `quantity`, `unit_price`) |

Tablo sirasi onemli: once `users` ve `products`, sonra `orders`, en son `order_items`.

<br>

### 📄 `seed.sql`

Ornek veri ekledim: 3 kullanici, 4 urun, 4 siparis, 6 siparis esyasi satiri.

| Kullanici | Siparis sayisi (ozet) |
|---|---|
| Ali | 2 siparis |
| Ayse | 1 siparis |
| Mehmet | 1 siparis |

Klavye urunu hic satilmadi — 4. sorgu icin bilerek biraktim.

<br>

### 📄 `queries.sql`

4 is sorusuna cevap veren SELECT sorgulari yazdim:

| # | Soru | Beklenen sonuc (ornek veri) |
|---|---|---|
| 1 | En cok siparis veren kullanici | Ali, 2 siparis |
| 2 | En cok satilan urun | USB Kablo, 5 adet |
| 3 | Toplam siparis tutari | 925.0 TL |
| 4 | Hic satilmayan urunler | Klavye |

<br>

### 📄 `run_queries.py`

`sqlite3` modulu ile `shop.db`'ye baglanip `queries.sql` dosyasindaki sorgulari calistiran ve sonuclari ekrana yazdiran Python scripti.

| Adim | Ne yapiyor? |
|---|---|
| `sqlite3.connect` | `shop.db`'ye baglan |
| `open(queries.sql)` | SQL dosyasini oku |
| `split(";")` | 4 ayri sorguya bol |
| `cursor.execute` + `fetchall` | Her sorguyu calistir, sonucu al |
| `print` | Baslik ve satirlari yazdir |

<br>

### 📦 `shop.db` (otomatik, teslim dosyasi degil)

`create_tables.sql` ve `seed.sql` calistirilinca otomatik olusur. Git'e eklemek zorunlu degil.

Detayli SQL kavramlari ve komutlar: [`cheatsheets/sql.md`](../cheatsheets/sql.md)

---

## Nasil calistirilir

Ekstra kurulum gerekmedi — Python 3 ve macOS'taki `sqlite3` komutu yeterli.

Proje kokunden veritabanini sifirdan kurmak:

```bash
rm -f week-04/shop.db
sqlite3 week-04/shop.db < week-04/create_tables.sql
sqlite3 week-04/shop.db < week-04/seed.sql
```

SQL sorgularini terminalden calistirmak:

```bash
sqlite3 week-04/shop.db < week-04/queries.sql
```

Tek sorguyu baslikli gormek icin:

```bash
sqlite3 -header -column week-04/shop.db "SELECT u.name, u.email, COUNT(*) AS siparis_sayisi FROM users u JOIN orders o ON u.id = o.user_id GROUP BY u.id, u.name, u.email ORDER BY siparis_sayisi DESC LIMIT 1;"
```

Python scripti:

```bash
python3 week-04/run_queries.py
```

Ornek cikti:

```text
----------------------------------------
1. En cok siparis veren kullanici
----------------------------------------
('Ali', 'ali@mail.com', 2)

----------------------------------------
2. En cok satilan urun
----------------------------------------
('USB Kablo', 5)

----------------------------------------
3. Toplam siparis tutari
----------------------------------------
(925.0,)

----------------------------------------
4. Hic satilmayan urunler
----------------------------------------
('Klavye',)
```

---

## Ne ogrendim

### 🗄️ Veritabani mantigi

- Veritabani = verilerin **kalici** ve **duzenli** tutuldugu yer. Hafta 03'teki `gorevler = []` listesi program kapaninca siliniyordu; `.db` dosyasi diskte kalir.
- Bu hafta **SQLite** kullandim: tek dosya, kurulum gerektirmez, Python ile uyumlu.
- Tablo = ayni turden kayitlarin tutuldugu yapi; satir = tek kayit; sutun = o kayittaki bir alan (ornegin `name`, `email`).

<br>

### 🏗️ 4 tablo mimarisi

```
users          products
  │                │
  └── orders ──────┘
         │
    order_items
```

- **`users`** → Kim siparis veriyor?
- **`products`** → Ne satiliyor?
- **`orders`** → Siparis ozeti (kim, ne zaman, toplam) — fatura ust bilgisi
- **`order_items`** → Siparisteki her urun satiri — fatura detayi

**Neden `orders` ve `order_items` ayri?** Bir siparisde birden fazla urun olabilir. `orders` = 1 satir = 1 siparis; `order_items` = her urun icin 1 satir.

**`order_items.id`:** `order_id` hangi siparise ait oldugunu soyler; `id` o tablodaki satirin benzersiz kimligidir.

<br>

### 📝 SQL dosyalarinin rolleri

| Dosya | Rol |
|---|---|
| `create_tables.sql` | Bos tablolarin iskeleti (`CREATE TABLE`) |
| `seed.sql` | Ornek veri (`INSERT`) — gercek uygulamada siparis verilince program ekler; bu hafta elle yazdim |
| `queries.sql` | Is sorularina cevap (`SELECT`, `JOIN`, `GROUP BY`...) |
| `run_queries.py` | Python ile sorgulari otomatik calistir |

<br>

### 🔀 SQL sorgu kavramlari

- **JOIN:** Tablolari ortak sutun uzerinden birlestirme (`u.id = o.user_id`).
- **GROUP BY:** Satirlari gruplama; `COUNT(*)` satir sayar, `SUM(quantity)` adetleri toplar.
- **LEFT JOIN + IS NULL:** Hic satilmayan urunleri bulma.
- **Alias (`u`, `o`, `p`):** Tabloya kisa ad verme; `u.name` = `users.name`.
- **AS:** Sonuc sutununa isim verme (`AS siparis_sayisi`).

<br>

### 🐍 Python (`run_queries.py`)

- `sqlite3.connect` ile veritabanina baglanma
- `Path(__file__).parent` ile dosya yollarini script'in yanindan bulma
- `cursor.execute` + `fetchall` ile SQL calistirma ve sonuc alma
- `zip(BASLIKLAR, sorgular)` ile baslik ve sorguyu eslestirme
- `if __name__ == "__main__":` ile dogrudan calistirma (hafta 01)

<br>

### 🔗 Onceki haftalarla baglanti

| Onceki hafta | Bu hafta |
|---|---|
| `gorevler = []` (hafta 03) | `users`, `orders` tablolari |
| `append` / `pop` | `INSERT` / `SELECT` |
| `for gorev in gorevler` | `for satir in sonuclar` |
| `print(gorev)` | `print(satir)` |

---

## Nerede takildim

### ⚠️ `AUTO_INCREMENT` vs `AUTOINCREMENT`

Ilk `create_tables.sql` denememde MySQL sozdizimi kullandim:

```text
Parse error near line 2: near "AUTO_INCREMENT": syntax error
```

SQLite'ta dogrusu: `INTEGER PRIMARY KEY AUTOINCREMENT` (tek kelime, alt cizgi yok).

<br>

### 📋 `.tables` bos gorundu

SQL hata verince tablolar olusmuyordu; `shop.db` vardi ama icinde tablo yoktu. Cozum: SQL'i duzeltip `shop.db`'yi silip yeniden calistirmak.

<br>

### 👁️ `sqlite_sequence` tablosu

DB viewer'da gorundu ama `sqlite3 ... ".tables"` cikisinda yoktu. `AUTOINCREMENT` kullaninca SQLite'in otomatik ekledigi ic tablo; benim olusturdugum tablo degil.

<br>

### 🔢 `GROUP BY` satirinda virgul unuttum

Sorgu 2'de `GROUP BY p.id p.name` yazinca syntax error aldim. Birden fazla sutunda virgul gerekli: `GROUP BY p.id, p.name`.

<br>

### 🤔 `COUNT` vs `SUM` karisikligi

- Sorgu 1: Kac **siparis**? → `COUNT(*)` (gruptaki satir sayisi)
- Sorgu 2: Kac **adet urun**? → `SUM(quantity)` (adetleri topla)

Ayni urun 2 satirda gorunebilir; `COUNT` = 2 satir, `SUM` = 3+2 = 5 adet.

<br>

### 🏷️ `SELECT` ve `AS` mantigi

`SELECT` her virgullu parca icin bir sutun secer. `COUNT(*) AS siparis_sayisi` = once hesapla (`COUNT`), sonra sutuna isim ver (`AS`). `AS` otomatik gelmez; ben veriyorum.

<br>

### 🐍 `run_queries.py` ilk bakista karmasik geldi

`Path`, `zip`, `split(";")` gibi parcalar hafta 01-03'teki `for`, `open`, `def main` uzerine biniyor. Adim adim ogrenince mantik oturdu: baglan → dosya oku → sorgulari bol → calistir → yazdir → kapat.

<br>

### 💡 Bilerek basit biraktiklarim

| Konu | Not |
|---|---|
| `INT` vs `INTEGER` | Sonra `INTEGER`'a cevirdim; SQLite'ta ikisi de calisir |
| `email UNIQUE` | Gercek projede olur; bu task'ta basit kalsin diye eklemedim |
| `PRAGMA foreign_keys = ON` | `seed.sql`'de var; yanlis id eklenmesin diye |

---

## Iliskili dosyalar

| Dosya | Rol |
|---|---|
| `week-04/create_tables.sql` | Tablo tanimlari |
| `week-04/seed.sql` | Ornek veri |
| `week-04/queries.sql` | 4 is sorgusu |
| `week-04/run_queries.py` | Python ile sorgu calistirma |
| `week-04/shop.db` | Calistirinca olusan veritabani (otomatik) |
| `cheatsheets/sql.md` | SQL kavramlari, komutlar, sik hatalar |

