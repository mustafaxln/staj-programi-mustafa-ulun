# SQL ve SQLite — Temel Kavramlar

> 📌 Hafta 04 · `create_tables.sql` · `seed.sql` · `queries.sql` · `run_queries.py`

## Icindekiler

| Bölüm | |
|:---:|:---|
| 📦 | [Table, row, column](#table-row-column) |
| 🔑 | [Primary key](#primary-key) |
| 🔗 | [Foreign key](#foreign-key) |
| 📖 | [SELECT](#select) |
| ➕ | [INSERT](#insert) |
| ✏️ | [UPDATE](#update) |
| 🗑️ | [DELETE](#delete) |
| 🔍 | [WHERE](#where) |
| 🔀 | [JOIN](#join) |
| 📊 | [GROUP BY](#group-by) |
| ↕️ | [ORDER BY](#order-by) |
| ⚠️ | [NULL ile ilgili dikkat notlari](#null-ile-ilgili-dikkat-notlari) |
| 🏗️ | [Week-04 veri modeli](#week-04-veri-modeli) |
| 🖥️ | [Terminal komutlari](#terminal-komutlari) |
| 🐍 | [Python sqlite3 (`run_queries.py`)](#python-sqlite3-run_queriespy) |
| ❌ | [Sik yaptigim hatalar](#sik-yaptigim-hatalar) |

---

## Table, row, column

- **Table (tablo)** = Ayni turden kayitlarin tutuldugu yapi. Ornegin `users`, `products`.
- **Row (satir / kayit)** = Tablodaki tek bir veri satiri. Ornegin bir kullanici: `Ali, ali@mail.com`.
- **Column (sutun / alan)** = Her kayitta tutulan bilgi alani. Ornegin `name`, `email`, `price`.

`week-04/create_tables.sql` dosyamda 4 tablo tanimladim:

```sql
CREATE TABLE users (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    name  TEXT NOT NULL,
    email TEXT NOT NULL
);
```

| Kavram | Bu ornekte |
|---|---|
| Tablo | `users` |
| Sutunlar | `id`, `name`, `email` |
| Satir | `(1, 'Ali', 'ali@mail.com')` — `seed.sql` ile eklenir |

---

## Primary key

- Her satirin **benzersiz kimligi**. Ayni tabloda iki satirin `id`'si ayni olamaz.
- Genelde `id` adinda bir tam sayi sutunu kullanilir.
- SQLite'ta otomatik artan id:

```sql
id INTEGER PRIMARY KEY AUTOINCREMENT
```

- `AUTOINCREMENT` kullaninca SQLite arka planda `sqlite_sequence` adli **sistem tablosu** olusturur. Benim olusturdugum tablo degil; son kullanilan id'yi takip eder. `.tables` komutunda gorunmez.
- `order_items.id` de primary key ama farkli soru sorar: "hangi siparis?" degil (`order_id`), "bu satirin kimligi ne?"

---

## Foreign key

- Baska bir tablodaki `id`'ye referans veren sutun.
- "Bu satir, su tablodaki su kayda bagli" der.

`week-04/create_tables.sql` ornekleri:

```sql
FOREIGN KEY (user_id) REFERENCES users(id)

FOREIGN KEY (order_id)   REFERENCES orders(id),
FOREIGN KEY (product_id) REFERENCES products(id)
```

Gorsel:

```
users.id       ◄──  orders.user_id
orders.id      ◄──  order_items.order_id
products.id    ◄──  order_items.product_id
```

`seed.sql` basinda foreign key kontrolunu aciyorum:

```sql
PRAGMA foreign_keys = ON;
```

---

## SELECT

- Tablodan veri **okumak** icin.

```sql
SELECT name, email FROM users;
SELECT * FROM products;
SELECT name FROM products WHERE price > 100;
```

`week-04/queries.sql` dosyasindaki 4 sorgu da `SELECT` ile baslar.

Alias (takma ad) ornegi:

```sql
SELECT u.name, u.email
FROM users u
```

`u` = `users` tablosunun kisa adi; `u.name` = `users.name`.

`AS` ile sonuc sutununa isim verme:

```sql
COUNT(*) AS siparis_sayisi
SUM(oi.quantity) AS toplam_adet
```

---

## INSERT

- Tabloya **yeni satir eklemek** icin.

```sql
INSERT INTO users (id, name, email) VALUES
(1, 'Ali', 'ali@mail.com');
```

`week-04/seed.sql` sira onemli:

1. `users`, `products` (bagimsiz)
2. `orders` (`user_id` gerekir)
3. `order_items` (`order_id` ve `product_id` gerekir)

`AUTOINCREMENT` kullaniyorsam `id` yazmak zorunda degilim; `seed.sql`'de okunaklilik icin id'leri elle yazdim.

---

## UPDATE

- Mevcut satiri **degistirmek** icin.

```sql
UPDATE products SET price = 160.00 WHERE id = 1;
```

Bu haftada zorunlu degil; ileride fiyat guncelleme ornegi olarak kullanilabilir.

---

## DELETE

- Satir **silmek** icin.

```sql
DELETE FROM order_items WHERE id = 2;
```

`WHERE` olmadan `DELETE FROM users` tum kullanicilari siler — dikkat!

---

## WHERE

- Sonuclari **filtrelemek** icin.

```sql
SELECT * FROM orders WHERE user_id = 1;
SELECT * FROM products WHERE price >= 100;
```

Sorgu 4'te `WHERE oi.id IS NULL` ile hic satilmayan urunleri filtreledim.

---

## JOIN

- Birden fazla tabloyu **ortak sutun** uzerinden birlestirmek.

### INNER JOIN — sadece eslesenler

Sorgu 1 (`queries.sql`):

```sql
SELECT u.name, u.email, COUNT(*) AS siparis_sayisi
FROM users u
JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name, u.email
ORDER BY siparis_sayisi DESC
LIMIT 1;
```

Sorgu 2:

```sql
SELECT p.name, SUM(oi.quantity) AS toplam_adet
FROM products p
JOIN order_items oi ON p.id = oi.product_id
GROUP BY p.id, p.name
ORDER BY toplam_adet DESC
LIMIT 1;
```

### LEFT JOIN — soldakilerin hepsi

Sorgu 4:

```sql
SELECT p.name
FROM products p
LEFT JOIN order_items oi ON p.id = oi.product_id
WHERE oi.id IS NULL;
```

| JOIN tipi | Ne zaman? |
|---|---|
| INNER JOIN | Iki tabloda da karsiligi olan kayitlar |
| LEFT JOIN | "Hic yok" veya eslesmeyenleri bul |

**On kurali:** `users.id = orders.user_id` (`user_id` ile `order_id` ayni sey degil!)

---

## GROUP BY

- Satirlari gruplayip **saymak** veya **toplamak** icin.

```sql
SELECT user_id, COUNT(*) AS siparis_sayisi
FROM orders
GROUP BY user_id;
```

| Fonksiyon | Ne yapar? | Ornek soru |
|---|---|---|
| `COUNT(*)` | Gruptaki **satir sayisi** | Kac siparis? |
| `SUM(quantity)` | Sutun **degerlerini toplar** | Kac adet urun? |
| `SUM(total_amount)` | Tutarlari toplar | Toplam ciro? |

Gruplamayi `id` ile yapmak daha guvenli; ayni isimde iki kullanici olursa sadece `name` ile gruplamak yanlis birlestirir.

Birden fazla sutunda virgul gerekir:

```sql
GROUP BY u.id, u.name, u.email   -- dogru
GROUP BY p.id p.name             -- HATA: virgul eksik
```

---

## ORDER BY

- Sonuclari **siralamak** icin.

```sql
ORDER BY siparis_sayisi DESC   -- buyukten kucuge
LIMIT 1                        -- sadece ilk satir
```

`DESC` = descending (azalan), `ASC` = ascending (artan, varsayilan).

---

## NULL ile ilgili dikkat notlari

- `NULL` = "deger yok / bilinmiyor". Sifir veya bos string degil.
- Esitlik kontrolu: `= NULL` yerine `IS NULL` / `IS NOT NULL` kullan.

```sql
WHERE oi.id IS NULL    -- LEFT JOIN'de eslesme yok = hic satilmamis
```

Sorgu 4 mantigi: Tum `products` solda kalir; `order_items`'ta karsiligi olmayan urunlerde `oi.id` NULL olur.

---

## Week-04 veri modeli

```
users          products
  │                │
  └── orders ──────┘
         │
    order_items
```

| Tablo | Soru | Ornek sutunlar |
|---|---|---|
| `users` | Kim? | `id`, `name`, `email` |
| `products` | Ne? | `id`, `name`, `price` |
| `orders` | Hangi siparis? (ozet) | `id`, `user_id`, `order_date`, `total_amount` |
| `order_items` | Sipariste ne var? (detay) | `id`, `order_id`, `product_id`, `quantity`, `unit_price` |

**Neden iki siparis tablosu?**

- `orders` = 1 satir = 1 siparis (fatura ust bilgisi)
- `order_items` = 1 satir = 1 urun satiri (siparisteki esya)
- Bir sipariste 3 urun varsa `order_items`'ta 3 satir, `orders`'ta 1 satir

**`.db` dosyasi teslim listesinde yok** — SQL dosyalari calistirilinca otomatik olusur.

**Kurulum gerekmez** — Python `sqlite3` modulu ve macOS `sqlite3` komutu yeterli.

---

## Terminal komutlari

Proje kokunden:

```bash
# Tablolari olustur
sqlite3 week-04/shop.db < week-04/create_tables.sql

# Ornek veri ekle
sqlite3 week-04/shop.db < week-04/seed.sql

# Tum sorgulari calistir
sqlite3 week-04/shop.db < week-04/queries.sql

# Tablolari listele
sqlite3 week-04/shop.db ".tables"

# Sifirdan basla
rm week-04/shop.db
sqlite3 week-04/shop.db < week-04/create_tables.sql
sqlite3 week-04/shop.db < week-04/seed.sql
```

Baslikli tek sorgu:

```bash
sqlite3 -header -column week-04/shop.db "SELECT SUM(total_amount) FROM orders;"
```

---

## Python sqlite3 (`run_queries.py`)

`week-04/run_queries.py` akisi:

```python
conn = sqlite3.connect(DB_DOSYASI)   # baglan
cursor = conn.cursor()               # sorgu kalemi

cursor.execute(sorgu)                # SQL calistir
sonuclar = cursor.fetchall()         # tum satirlari al

conn.close()                         # baglantiyi kapat
```

| Parca | Ne? |
|---|---|
| `sqlite3.connect` | `shop.db`'ye baglanti |
| `cursor.execute` | SQL calistir |
| `fetchall` | Sonuc satirlarini liste olarak al (tuple) |
| `Path(__file__).parent` | Script'in bulundugu `week-04` klasoru |

Calistirma:

```bash
python3 week-04/run_queries.py
```

---

## Sik yaptigim hatalar

### `AUTO_INCREMENT` (MySQL) yerine `AUTOINCREMENT` (SQLite)

```text
Parse error near line 2: near "AUTO_INCREMENT": syntax error
```

| Yanlis (MySQL) | Dogru (SQLite) |
|---|---|
| `INT PRIMARY KEY AUTO_INCREMENT` | `INTEGER PRIMARY KEY AUTOINCREMENT` |

<br>

### `GROUP BY` satirinda virgul eksik

```sql
GROUP BY p.id p.name    -- HATA
GROUP BY p.id, p.name   -- dogru
```

<br>

### `user_id` ile `order_id` karistirmak

| Sutun | Anlam |
|---|---|
| `orders.user_id` | Siparisi kim verdi? → `users.id` |
| `order_items.order_id` | Esya hangi siparise ait? → `orders.id` |

JOIN: `u.id = o.user_id` (`user_id` = `order_id` degil!)

<br>

### `COUNT` vs `SUM` karistirmak

- Kac **siparis**? → `COUNT(*)` (Sorgu 1)
- Kac **adet urun**? → `SUM(quantity)` (Sorgu 2)
- Toplam **para**? → `SUM(total_amount)` (Sorgu 3)

<br>

### `= NULL` kullanmak

```sql
WHERE oi.id = NULL     -- calismaz
WHERE oi.id IS NULL    -- dogru
```

<br>

### SQL hata verince `.tables` bos

`shop.db` olusur ama tablolar olusmaz. Cozum:

```bash
rm week-04/shop.db
sqlite3 week-04/shop.db < week-04/create_tables.sql
```
