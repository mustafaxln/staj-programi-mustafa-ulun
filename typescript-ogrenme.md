# TypeScript Öğrenme Notları — Sıfırdan Başlangıç

> Bu dosya staj programı teslimi değil — öğrenmek için yazıldı.
> Python bilgisiyle oku; her bölümde **Python → TypeScript** karşılaştırması var.

---

## İçindekiler

| Bölüm | Konu |
|:---:|---|
| 0 | [Bu dosyayı nasıl kullanmalısın?](#bölüm-0-bu-dosyayı-nasıl-kullanmalısın) |
| 1 | [TypeScript nedir?](#bölüm-1-typescript-nedir) |
| 2 | [Kurulum ve proje yapısı](#bölüm-2-kurulum-ve-proje-yapısı) |
| 3 | [İlk program ve çıktı](#bölüm-3-ilk-program-ve-çıktı) |
| 4 | [Değişkenler: const ve let](#bölüm-4-değişkenler-const-ve-let) |
| 5 | [Veri tipleri](#bölüm-5-veri-tipleri) |
| 6 | [Operatörler ve işlemler](#bölüm-6-operatörler-ve-işlemler) |
| 7 | [String işlemleri](#bölüm-7-string-işlemleri) |
| 8 | [Koşullar: if / else](#bölüm-8-koşullar-if--else) |
| 9 | [Döngüler](#bölüm-9-döngüler) |
| 10 | [Fonksiyonlar](#bölüm-10-fonksiyonlar) |
| 11 | [Array — Python listesi](#bölüm-11-array--python-listesi) |
| 12 | [Object ve Record — Python dict](#bölüm-12-object-ve-record--python-dict) |
| 13 | [Set](#bölüm-13-set) |
| 14 | [interface ve type](#bölüm-14-interface-ve-type) |
| 15 | [Hata yönetimi](#bölüm-15-hata-yönetimi) |
| 16 | [Derleme ve çalıştırma](#bölüm-16-derleme-ve-çalıştırma) |
| 17 | [Gerçek örnekler — staj kodları](#bölüm-17-gerçek-örnekler--staj-kodları) |
| 18 | [Python vs TypeScript özeti](#bölüm-18-python-vs-typescript-özeti) |
| 19 | [Sık yapılan hatalar](#bölüm-19-sık-yapılan-hatalar) |
| 20 | [Kendi kendine test](#bölüm-20-kendi-kendine-test) |

---

## Bölüm 0 — Bu dosyayı nasıl kullanmalısın?

1. Bölümleri sırayla oku (1 → 20).
2. Her bölümde önce Python kodunu oku, sonra TypeScript karşılığına bak.
3. `week-05/src/` altındaki dosyaları bu bölümlerle eşleştir.
4. Bir bölüm bittiğinde kısa örnekleri kendin yazıp `npm run build` ile dene.

**Hedef:** Bu dosyayı bitirdiğinde TypeScript'in temel yapısını, Python'dan farklarını ve `week-05` kodlarını okuyup yazabilmen.

---

## Bölüm 1 — TypeScript nedir?

### 1.1 Kısa tanım

**TypeScript = JavaScript + tip sistemi.**

- JavaScript web ve Node.js'in çalıştırdığı dil.
- TypeScript, JavaScript'e **tip kuralları** ekler.
- Bilgisayar TypeScript'i doğrudan çalıştırmaz; önce JavaScript'e çevrilir.

### 1.2 Python ile karşılaştırma

| | Python | TypeScript |
|---|---|---|
| Dosya uzantısı | `.py` | `.ts` |
| Çalıştırma | Doğrudan | Önce derle, sonra çalıştır |
| Tip sistemi | İsteğe bağlı | Yazarken tip verirsin |
| Ortam | Python yorumlayıcısı | Node.js |

### 1.3 Çalışma zinciri

```
PYTHON:
  functions.py  ──►  python3 functions.py  ──►  çıktı

TYPESCRIPT:
  src/functions.ts  ──►  tsc (derle)  ──►  dist/functions.js  ──►  node  ──►  çıktı
```

**Önemli:** TypeScript'te yazdığın kod aslında JavaScript olur. Tipler derleme sonrası kaybolur; ama yazarken sana ve editöre yardımcı olur.

### 1.4 Neden TypeScript?

- Yanlış tip verirsen **çalıştırmadan önce** hata görürsün.
- Editör otomatik tamamlama ve ipucu verir.
- Büyük projede "bu fonksiyon ne alıyor, ne döndürüyor?" net kalır.
- Web (React) ve backend (Node, Express) ekosistemiyle uyumlu.

---

## Bölüm 2 — Kurulum ve proje yapısı

### 2.1 Gerekli araçlar

| Araç | Ne işe yarar? | Python karşılığı |
|---|---|---|
| Node.js | JavaScript/TS çalıştırma ortamı | Python yorumlayıcısı |
| npm | Paket yöneticisi | pip |
| TypeScript (`tsc`) | Derleyici | — (Python'da yok) |

### 2.2 week-05 klasör yapısı

```
week-05/                    ← TEK PROJE (bir npm init)
├── package.json            ← proje kartı + npm komutları
├── tsconfig.json           ← derleyici ayarları
├── node_modules/           ← indirilen paketler (elle dokunma)
├── src/                    ← SENİN YAZDIĞIN .ts dosyaları
│   ├── functions.ts
│   ├── data-structures.ts
│   └── algorithms.ts
└── dist/                   ← derlenmiş .js dosyaları (otomatik)
```

### 2.3 Python'dan farkı

**Python (week-02):**

```
week-02/
├── algorithms.py      → python3 algorithms.py  (bağımsız)
├── data_structures.py → python3 data_structures.py  (bağımsız)
```

Her dosya ayrı çalışır. Ortak kurulum yok.

**TypeScript (week-05):**

- Bir `npm init`, bir `package.json`.
- Birden fazla `.ts` dosyası aynı proje içinde.
- Her dosya için **ayrı npm projesi açmıyorsun**.

### 2.4 Önemli dosyalar

| Dosya | Görevi |
|---|---|
| `package.json` | `npm run build`, `npm run functions` gibi komutlar |
| `tsconfig.json` | `rootDir: ./src`, `outDir: ./dist` |
| `.gitignore` | `node_modules/` ve `dist/` git'e gitmesin |

---

## Bölüm 3 — İlk program ve çıktı

### 3.1 Yazdırma

**Python:**

```python
print("Hello, World!")
print("Sayi:", 5)
```

**TypeScript:**

```typescript
console.log("Hello, World!");
console.log("Sayi:", 5);
```

| Python | TypeScript |
|---|---|
| `print(...)` | `console.log(...)` |

`console` = terminal/ekran çıktısı için kullanılan araç. Node.js ortamında `print` yok.

### 3.2 Yorum satırları

**Python:**

```python
# tek satır yorum
```

**TypeScript:**

```typescript
// tek satır yorum
/* çok satırlı
   yorum */
```

### 3.3 İlk dosya: hello.ts

```typescript
console.log("Hello, World!");
```

Çalıştırma:

```bash
cd week-05
npm run build
node dist/hello.js
```

---

## Bölüm 4 — Değişkenler: const ve let

### 4.1 Değişken nedir?

Python'da öğrendiğin gibi: hafızada değer tutan, isimle erişilen kutular.

**Python:**

```python
sayi = 5
metin = "merhaba"
dogru_mu = True
```

**TypeScript:**

```typescript
const sayi: number = 5;
const metin: string = "merhaba";
const dogruMu: boolean = true;
```

### 4.2 const vs let

TypeScript'te değişken tanımlarken iki ana seçenek var:

| Anahtar | Ne demek? | Ne zaman kullan? |
|---|---|---|
| `const` | Bir kez ata, **yeniden atama yapma** | Değişmeyecek değerler |
| `let` | İstediğin zaman yeniden atayabilirsin | Döngü sayacı, biriken sonuç |

**Python'da** bu ayrım yok; her değişkeni `x = 5` ile tanımlarsın.

**Örnek — const:**

```typescript
const baslik = "Staj Programi";
// baslik = "Baska";  // ❌ HATA: const yeniden atanamaz
```

**Örnek — let (faktöriyelde):**

```typescript
let sonuc = 1;
for (let i = 1; i <= n; i++) {
    sonuc *= i;  // sonuc her turda değişiyor → let
}
```

### 4.3 Tip yazmak

`: number`, `: string` gibi ifadeler **tip** belirtir.

```typescript
const sayi: number = 5;       // sayı
const metin: string = "ali";  // metin
const aktif: boolean = true;  // doğru/yanlış
```

Python karşılığı (isteğe bağlı hint):

```python
sayi: int = 5
metin: str = "ali"
```

**Fark:** TypeScript'te derleyici tipi kontrol eder. Python'da yazsan da zorunlu değil.

Tip yazmadan da çalışır (derleyici çıkarır), ama yazmak daha güvenli:

```typescript
let sonuc = 1;  // TypeScript bunu number olarak anlar
```

### 4.4 const döngüde — sık sorulan soru

```typescript
for (const kelime of kelimeler) {
    console.log(kelime);
}
```

**Soru:** Her turda `kelime` değişiyor; neden `const`?

**Cevap:** `const` = "bu turun içinde `kelime`'yi başka bir şeye **yeniden atama**". Her tur **yeni bir `kelime`** alır; Python'daki `for kelime in kelimeler` ile aynı mantık.

```python
for kelime in kelimeler:  # her turda kelime = o anki eleman
    print(kelime)
```

---

## Bölüm 5 — Veri tipleri

### 5.1 Temel tipler tablosu

| TypeScript | Örnek | Python | Açıklama |
|---|---|---|---|
| `number` | `5`, `3.14`, `-2` | `int`, `float` | Sayılar (TS'de int/float ayrımı yok) |
| `string` | `"merhaba"`, `'ali'` | `str` | Metin |
| `boolean` | `true`, `false` | `True`, `False` | Doğru/yanlış (TS küçük harf) |
| `null` | `null` | `None` (bazen) | Bilerek boş |
| `undefined` | `undefined` | — | Tanımsız / henüz değer yok |

### 5.2 number

```typescript
const tam: number = 10;
const ondalik: number = 3.14;
const negatif: number = -5;
```

```python
tam = 10
ondalik = 3.14
negatif = -5
```

### 5.3 string

```typescript
const isim: string = "Mustafa";
const tekTirnak: string = 'Python gibi';
```

Tek ve çift tırnak ikisi de string.

### 5.4 boolean

```typescript
const gecti: boolean = true;
const kaldi: boolean = false;
```

```python
gecti = True
kaldi = False
```

### 5.5 null ve undefined

Python'da çoğu zaman `None` yeterli. TypeScript'te iki kavram var:

| Değer | Anlam |
|---|---|
| `null` | "Bu değer bilerek boş" |
| `undefined` | "Henüz değer atanmadı" |

Başlangıçta ikisini karıştırabilirsin; pratikte `??` operatörü ile güvenli kontrol yaparsın (Bölüm 6).

### 5.6 Dizi ve obje tipleri (kısa)

```typescript
const sayilar: number[] = [1, 2, 3];
const frekans: Record<string, number> = {};
```

Detay: Bölüm 11 ve 12.

---

## Bölüm 6 — Operatörler ve işlemler

### 6.1 Aritmetik

| İşlem | Python | TypeScript | Örnek sonuç |
|---|---|---|---|
| Toplama | `+` | `+` | `3 + 2` → 5 |
| Çıkarma | `-` | `-` | `5 - 2` → 3 |
| Çarpma | `*` | `*` | `4 * 2` → 8 |
| Bölme | `/` | `/` | `10 / 4` → 2.5 |
| Mod | `%` | `%` | `10 % 3` → 1 |
| Üs | `**` | `**` veya `Math.pow` | `2 ** 3` → 8 |

**TypeScript örnek:**

```typescript
const toplam = 10 + 5;
const carpim = 4 * 2;
const kalan = 10 % 3;
const us = 2 ** 3;
```

### 6.2 Karşılaştırma

| Python | TypeScript | Not |
|---|---|---|
| `==` | `===` | Tip + değer eşit mi? (TS'de `===` tercih) |
| `!=` | `!==` | Eşit değil |
| `>` | `>` | Büyük |
| `<` | `<` | Küçük |
| `>=` | `>=` | Büyük eşit |
| `<=` | `<=` | Küçük eşit |

**Örnek:**

```python
if sayi == 5:
    print("bes")
```

```typescript
if (sayi === 5) {
    console.log("bes");
}
```

**Neden `===`?** JavaScript'te `==` bazen beklenmedik sonuç verir. TypeScript'te genelde `===` kullan.

### 6.3 Mantıksal operatörler

| Python | TypeScript | Anlam |
|---|---|---|
| `and` | `&&` | İkisi de doğru |
| `or` | `\|\|` | Biri doğru yeter |
| `not` | `!` | Değil |

```python
if yas >= 18 and yas <= 65:
    print("uygun")
```

```typescript
if (yas >= 18 && yas <= 65) {
    console.log("uygun");
}
```

### 6.4 Atama ve artırma

| Python | TypeScript |
|---|---|
| `x = 5` | `x = 5` |
| `x += 1` | `x += 1` |
| `x *= 2` | `x *= 2` |
| — | `i++` (i'yi 1 artır, sık kullanılır) |

```typescript
let i = 1;
i++;        // i = 2
i += 1;     // aynı iş
```

### 6.5 Nullish coalescing: `??`

TypeScript'te sık kullanılan operatör:

```typescript
frekans[kelime] = (frekans[kelime] ?? 0) + 1;
```

**Anlam:** `frekans[kelime]` yoksa veya `null`/`undefined` ise `0` kullan.

Python karşılığı:

```python
if kelime in frekans:
    frekans[kelime] += 1
else:
    frekans[kelime] = 1
```

Aynı iş, daha kısa yazım.

---

## Bölüm 7 — String işlemleri

### 7.1 Birleştirme

**Python:**

```python
isim = "Ali"
mesaj = f"Merhaba {isim}"
mesaj2 = "Merhaba " + isim
```

**TypeScript:**

```typescript
const isim = "Ali";
const mesaj = `Merhaba ${isim}`;
const mesaj2 = "Merhaba " + isim;
```

`${...}` = Python'daki `f"{...}"`.

### 7.2 Uzunluk ve erişim

| Python | TypeScript |
|---|---|
| `len(s)` | `s.length` |
| `s[0]` | `s[0]` |
| `s[-1]` | `s[s.length - 1]` |

### 7.3 Bölme ve birleştirme

| Python | TypeScript |
|---|---|
| `cumle.split()` | `cumle.split(" ")` |
| `"".join(liste)` | `liste.join("")` |

**Kelime listesi:**

```python
kelimeler = cumle.split()
```

```typescript
const kelimeler = cumle.split(" ");
```

### 7.4 Ters çevirme — palindrom için

**Python:**

```python
return s == s[::-1]
```

**TypeScript:**

```typescript
return metin === metin.split("").reverse().join("");
```

Adım adım:

1. `split("")` → her harfi ayır: `["k","a","y","a","k"]`
2. `reverse()` → ters çevir
3. `join("")` → tekrar string yap

### 7.5 Büyük/küçük harf

| Python | TypeScript |
|---|---|
| `s.upper()` | `s.toUpperCase()` |
| `s.lower()` | `s.toLowerCase()` |

---

## Bölüm 8 — Koşullar: if / else

### 8.1 Temel yapı

**Python** girinti ile blok belirler:

```python
if yas >= 18:
    print("Gecti")
else:
    print("Kaldi")
```

**TypeScript** süslü parantez kullanır:

```typescript
if (yas >= 18) {
    console.log("Gecti");
} else {
    console.log("Kaldi");
}
```

| Fark | Python | TypeScript |
|---|---|---|
| Blok | Girinti (4 boşluk) | `{ }` |
| Koşul parantezi | Gerek yok | `if (yas >= 18)` |
| elif | `elif` | `else if` |

### 8.2 elif / else if

**Python:**

```python
if not >= 85:
    print("Pekiyi")
elif not >= 70:
    print("Iyi")
elif not >= 50:
    print("Orta")
else:
    print("Kaldi")
```

**TypeScript:**

```typescript
if (not >= 85) {
    console.log("Pekiyi");
} else if (not >= 70) {
    console.log("Iyi");
} else if (not >= 50) {
    console.log("Orta");
} else {
    console.log("Kaldi");
}
```

### 8.3 Erken return

Fonksiyon içinde koşul sağlandığında hemen dönmek (Python'daki gibi):

**Python:**

```python
def asal_sayi_kontrolu(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

**TypeScript:**

```typescript
function asal_sayi_kontrolu(n: number): boolean {
    if (n < 2) {
        return false;
    }
    for (let i = 2; i <= Math.floor(Math.sqrt(n)); i++) {
        if (n % i === 0) {
            return false;
        }
    }
    return true;
}
```

### 8.4 truthy / falsy

Python'da `0`, `""`, `None`, `[]` false sayılır.

TypeScript'te `0`, `""`, `null`, `undefined`, `false` false sayılır.

**Dikkat:** Boş liste `[]` ve boş obje `{}` TypeScript'te **true** sayılır (Python'dan fark).

---

## Bölüm 9 — Döngüler

### 9.1 for — sayı aralığı

**Python:**

```python
for i in range(1, n + 1):
    sonuc *= i
```

**TypeScript:**

```typescript
for (let i = 1; i <= n; i++) {
    sonuc *= i;
}
```

Parçalar:

| Parça | Anlam |
|---|---|
| `let i = 1` | Başlangıç |
| `i <= n` | Devam koşulu |
| `i++` | Her turda i'yi 1 artır |

`range(1, n+1)` = `1`'den `n`'e kadar.

### 9.2 for — liste/dizi üzerinde

**Python:**

```python
for kelime in kelimeler:
    print(kelime)
```

**TypeScript:**

```typescript
for (const kelime of kelimeler) {
    console.log(kelime);
}
```

Bu, Python'daki `for x in liste` ile **aynı mantık**.

### 9.3 for — indeks ile (enumerate benzeri)

**Python:**

```python
for i, eleman in enumerate(liste):
    print(i, eleman)
```

**TypeScript:**

```typescript
for (let i = 0; i < liste.length; i++) {
    console.log(i, liste[i]);
}
```

veya:

```typescript
liste.forEach((eleman, i) => {
    console.log(i, eleman);
});
```

Başlangıçta `for (let i = 0; ...)` yeterli.

### 9.4 while

**Python:**

```python
while on_off != 1:
    secim = int(input("Secim: "))
    if secim == 4:
        on_off = 1
```

**TypeScript:**

```typescript
while (onOff !== 1) {
    // secim al (readline ile — CLI uygulamalarında)
    if (secim === 4) {
        onOff = 1;
    }
}
```

`week-03/cli_app.py` mantığı aynı; girdi için Node'da `readline` kullanılır.

### 9.5 break ve continue

| Python | TypeScript |
|---|---|
| `break` | `break` |
| `continue` | `continue` |

Döngüyü kır veya o turu atla — aynı.

---

## Bölüm 10 — Fonksiyonlar

### 10.1 Temel tanım

**Python:**

```python
def toplama(a, b):
    return a + b
```

**TypeScript:**

```typescript
function toplama(a: number, b: number): number {
    return a + b;
}
```

| Parça | Anlam |
|---|---|
| `function toplama` | Fonksiyon adı |
| `a: number, b: number` | Parametre tipleri |
| `: number` | Dönüş tipi |

### 10.2 Parametre ve return

```typescript
function palindrom_kontrolu(s: string): boolean {
    const metin = String(s);
    return metin === metin.split("").reverse().join("");
}
```

- `string` alır → `boolean` döndürür.
- `return` olmadan fonksiyon `undefined` döner (Python'daki `None` gibi).

### 10.3 Hata fırlatma

**Python:**

```python
if n < 0:
    raise ValueError("Negatif sayıların faktoriyeli yoktur.")
```

**TypeScript:**

```typescript
if (n < 0) {
    throw new Error("Negatif sayilarin faktoriyeli yoktur.");
}
```

### 10.4 Tam örnek — faktöriyel

**Python (`week-01/functions.py`):**

```python
def faktoriyel(n):
    if n < 0:
        raise ValueError("Negatif sayıların faktoriyeli yoktur.")
    sonuc = 1
    for i in range(1, n + 1):
        sonuc *= i
    return sonuc
```

**TypeScript (`week-05/src/functions.ts`):**

```typescript
function faktoriyel(n: number): number {
    if (n < 0) {
        throw new Error("Negatif sayilarin faktoriyeli yoktur.");
    }
    let sonuc = 1;
    for (let i = 1; i <= n; i++) {
        sonuc *= i;
    }
    return sonuc;
}
```

Algoritma **birebir aynı**. Fark sadece sözdizimi ve tipler.

### 10.5 Fonksiyon çağırma

```typescript
const sonuc = faktoriyel(5);
console.log(sonuc);  // 120
```

```python
sonuc = faktoriyel(5)
print(sonuc)
```

### 10.6 if __name__ == "__main__" karşılığı

Python'da test kodlarını ayırmak için:

```python
if __name__ == "__main__":
    print(faktoriyel(5))
```

TypeScript'te dosya sonunda doğrudan yazılır (dosyayı `node` ile çalıştırdığında çalışır):

```typescript
console.log("Faktoriyel (5):", faktoriyel(5));
```

veya:

```typescript
function main(): void {
    console.log(faktoriyel(5));
}
main();
```

---

## Bölüm 11 — Array — Python listesi

### 11.1 Tanımlama

**Python:**

```python
liste = [5, 1, 4, 1, 3, 5, 2]
bos = []
```

**TypeScript:**

```typescript
const liste: number[] = [5, 1, 4, 1, 3, 5, 2];
const bos: number[] = [];
```

### 11.2 Sık kullanılan işlemler

| İşlem | Python | TypeScript |
|---|---|---|
| Eleman ekle | `liste.append(x)` | `liste.push(x)` |
| Son elemanı çıkar | `liste.pop()` | `liste.pop()` |
| Uzunluk | `len(liste)` | `liste.length` |
| İçeriyor mu? | `x in liste` | `liste.includes(x)` |
| Dilim | `liste[1:3]` | `liste.slice(1, 3)` |
| Son eleman | `liste[-1]` | `liste[liste.length - 1]` |

### 11.3 Döngü ile işleme

```typescript
const sonuc: number[] = [];
for (const eleman of liste) {
    sonuc.push(eleman);
}
```

### 11.4 Generic tip — `<T>`

`duplicate_temizle` hem sayı hem string listesi kabul edebilir:

```typescript
function duplicate_temizle<T>(liste: T[]): T[] {
    // ...
}
```

`<T>` = "herhangi bir tip". Python'da gerek yok; TS'de tip güvenliği için kullanılır.

---

## Bölüm 12 — Object ve Record — Python dict

### 12.1 Tanımlama

**Python:**

```python
frekans = {}
frekans["python"] = 2
frekans["kolay"] = 3
```

**TypeScript:**

```typescript
const frekans: Record<string, number> = {};
frekans["python"] = 2;
frekans["kolay"] = 3;
```

`Record<string, number>` = "string anahtar, number değer" — Python `dict` gibi.

### 12.2 Erişim ve kontrol

| Python | TypeScript |
|---|---|
| `frekans["python"]` | `frekans["python"]` |
| `"python" in frekans` | `"python" in frekans` |
| `frekans.get("x", 0)` | `frekans["x"] ?? 0` |

### 12.3 Döngü — items()

**Python:**

```python
for k, v in frekans.items():
    print(k, v)
```

**TypeScript:**

```typescript
for (const [k, v] of Object.entries(frekans)) {
    console.log(k, v);
}
```

### 12.4 Kelime frekansı örneği

**Python:**

```python
def kelime_frekanslari(cumle):
    kelimeler = cumle.split()
    frekans = {}
    for kelime in kelimeler:
        if kelime in frekans:
            frekans[kelime] += 1
        else:
            frekans[kelime] = 1
    return frekans
```

**TypeScript:**

```typescript
function kelime_frekanslari(cumle: string): Record<string, number> {
    const kelimeler = cumle.split(" ");
    const frekans: Record<string, number> = {};
    for (const kelime of kelimeler) {
        frekans[kelime] = (frekans[kelime] ?? 0) + 1;
    }
    return frekans;
}
```

### 12.5 İç içe obje — ürün katalogu

**Python:**

```python
katalog = {
    101: {"isim": "Laptop", "fiyat": 15000, "stok": 7},
    102: {"isim": "Klavye", "fiyat": 350, "stok": 33},
}
```

**TypeScript (interface ile):**

```typescript
interface Urun {
    isim: string;
    fiyat: number;
    stok: number;
}

const katalog: Record<number, Urun> = {
    101: { isim: "Laptop", fiyat: 15000, stok: 7 },
    102: { isim: "Klavye", fiyat: 350, stok: 33 },
};
```

---

## Bölüm 13 — Set

### 13.1 Tanımlama ve kullanım

**Python:**

```python
gorulen = set()
gorulen.add(5)
if eleman not in gorulen:
    gorulen.add(eleman)
```

**TypeScript:**

```typescript
const gorulen = new Set<number>();
gorulen.add(5);
if (!gorulen.has(eleman)) {
    gorulen.add(eleman);
}
```

| Python | TypeScript |
|---|---|
| `set()` | `new Set()` |
| `.add(x)` | `.add(x)` |
| `x in s` | `s.has(x)` |
| `x not in s` | `!s.has(x)` |

### 13.2 Duplicate temizleme

**Python:**

```python
def duplicate_temizle(liste):
    gorulen = set()
    sonuc = []
    for eleman in liste:
        if eleman not in gorulen:
            gorulen.add(eleman)
            sonuc.append(eleman)
    return sonuc
```

**TypeScript:**

```typescript
function duplicate_temizle<T>(liste: T[]): T[] {
    const gorulen = new Set<T>();
    const sonuc: T[] = [];
    for (const eleman of liste) {
        if (!gorulen.has(eleman)) {
            gorulen.add(eleman);
            sonuc.push(eleman);
        }
    }
    return sonuc;
}
```

### 13.3 Kısa yol — Set spread

```typescript
function duplicate_temizle_set<T>(liste: T[]): T[] {
    return [...new Set(liste)];
}
```

Python karşılığı: `list(dict.fromkeys(liste))` — ilk geçiş sırasını korur.

**Dikkat:** `sorted(set(liste))` tekrarları siler ama **sırayı da değiştirir** (week-02'de öğrendiğin gibi).

---

## Bölüm 14 — interface ve type

### 14.1 interface nedir?

Objenin **şablonu**. Hangi alanlar olmalı, tipleri ne?

```typescript
interface Urun {
    isim: string;
    fiyat: number;
    stok: number;
}

const klavye: Urun = {
    isim: "Klavye",
    fiyat: 350,
    stok: 33,
};
```

Yanlış tip verirsen hata:

```typescript
const hatali: Urun = {
    isim: "Mouse",
    fiyat: "ucuz",  // ❌ string verdin, number bekliyor
    stok: 10,
};
```

Python'da dict ile serbest yazarsın; çalışma anında patlayabilir.

### 14.2 type alias

Basit tip isimlendirme:

```typescript
type Not = number;
type OgrenciAdi = string;

type FrekansTablosu = Record<string, number>;
```

`Record<string, number>` yerine `FrekansTablosu` yazabilirsin — daha okunur.

### 14.3 interface vs Record

| Durum | Kullan |
|---|---|
| Sabit alanlı obje (isim, fiyat, stok) | `interface Urun` |
| Dinamik key-value (kelime → sayı) | `Record<string, number>` |

---

## Bölüm 15 — Hata yönetimi

### 15.1 Hata fırlatma

```typescript
throw new Error("Aciklama mesaji");
```

```python
raise ValueError("Aciklama mesaji")
```

### 15.2 Hata yakalama

**Python:**

```python
try:
    sonuc = faktoriyel(-1)
except ValueError as e:
    print("Hata:", e)
```

**TypeScript:**

```typescript
try {
    const sonuc = faktoriyel(-1);
} catch (e) {
    console.log("Hata:", e);
}
```

### 15.3 Derleme hatası vs çalışma zamanı hatası

| Tür | Ne zaman? | Örnek |
|---|---|---|
| Derleme hatası | `npm run build` sırasında | `faktoriyel("abc")` — string verdin |
| Çalışma zamanı hatası | `node` çalıştırırken | `faktoriyel(-1)` — throw Error |

TypeScript'in avantajı: birçok hatayı **derleme** aşamasında yakalarsın.

---

## Bölüm 16 — Derleme ve çalıştırma

### 16.1 Adım adım

```bash
cd week-05
npm install          # ilk kez
npm run build        # src/*.ts → dist/*.js
npm run functions    # derle + çalıştır
```

### 16.2 package.json scripts

```json
"scripts": {
    "build": "tsc",
    "functions": "npm run build && node dist/functions.js",
    "data-structures": "npm run build && node dist/data-structures.js",
    "algorithms": "npm run build && node dist/algorithms.js"
}
```

| Komut | Ne yapar? |
|---|---|
| `npm run build` | Tüm `src/*.ts` dosyalarını derler |
| `npm run functions` | Derle + `functions.js` çalıştır |

### 16.3 tsconfig.json özeti

```json
"rootDir": "./src",   // kaynak dosyalar burada
"outDir": "./dist"    // derlenmiş JS buraya
```

### 16.4 Kritik kural

Kod değiştirdikten sonra **tekrar derle**.

```
src/functions.ts değişti  →  npm run build  →  dist/functions.js güncellendi  →  node çalıştır
```

Sadece `node dist/functions.js` dersen **eski** kod çalışır.

---

## Bölüm 17 — Gerçek örnekler — staj kodları

Bu bölümde `week-05/src/` dosyalarındaki fonksiyonları özetliyoruz.

### 17.1 functions.ts

| Fonksiyon | Girdi | Çıktı | Python dosyası |
|---|---|---|---|
| `faktoriyel(n)` | `number` | `number` | `week-01/functions.py` |
| `palindrom_kontrolu(s)` | `string` | `boolean` | `week-01/functions.py` |
| `asal_sayi_kontrolu(n)` | `number` | `boolean` | `week-01/functions.py` |

Çalıştır: `npm run functions`

### 17.2 data-structures.ts

| Fonksiyon | Girdi | Çıktı | Python dosyası |
|---|---|---|---|
| `kelime_frekanslari(cumle)` | `string` | `Record<string, number>` | `week-02/data_structures.py` |

Çalıştır: `npm run data-structures`

### 17.3 algorithms.ts

| Fonksiyon | Girdi | Çıktı | Python dosyası |
|---|---|---|---|
| `duplicate_temizle(liste)` | `T[]` | `T[]` | `week-02/algorithms.py` |
| `duplicate_temizle_set(liste)` | `T[]` | `T[]` | `week-02/algorithms.py` |

Çalıştır: `npm run algorithms`

### 17.4 Öğrenme aktivitesi

Her dosyayı aç, Python karşılığını bul, satır satır eşleştir:

1. Hangi Python satırı hangi TypeScript satırına denk?
2. Tip imzaları ne işe yarıyor?
3. `??`, `Set`, `Record` nerede kullanıldı?

---

## Bölüm 18 — Python vs TypeScript özeti

### 18.1 Sözdizimi tablosu

| Konu | Python | TypeScript |
|---|---|---|
| Yazdırma | `print(x)` | `console.log(x)` |
| Değişken | `x = 5` | `const x: number = 5` |
| Fonksiyon | `def f(n):` | `function f(n: number): number` |
| Koşul | `if x > 0:` | `if (x > 0) { }` |
| Döngü (liste) | `for x in liste` | `for (const x of liste)` |
| Döngü (sayı) | `for i in range(n)` | `for (let i = 0; i < n; i++)` |
| Liste | `liste = []` | `const liste: number[] = []` |
| Dict | `d = {}` | `const d: Record<string, number> = {}` |
| Set | `s = set()` | `const s = new Set()` |
| Hata | `raise ValueError` | `throw new Error` |
| Boş | `None` | `null` / `undefined` |
| Çalıştırma | `python3 dosya.py` | `npm run build` + `node dist/dosya.js` |

### 18.2 Artılar ve eksiler

**Python artıları:** Hızlı başlangıç, az kurulum, okunabilir syntax.

**Python eksileri:** Tip hataları çalışma anında çıkabilir.

**TypeScript artıları:** Hata yazarken yakalanır, büyük projede yapı net, web/Node ekosistemi.

**TypeScript eksileri:** Kurulum, derle+çalıştır iki adım, başlangıçta daha fazla kavram.

### 18.3 Aynı kalan şey

- Algoritma mantığı (döngü, koşul, set, dict).
- Problem çözme adımları.
- Fonksiyonlara bölme, test yazma.

**Fark çoğunlukla sözdizimi ve tip sistemi — mantık aynı.**

---

## Bölüm 19 — Sık yapılan hatalar

| Hata | Sebep | Çözüm |
|---|---|---|
| Eski çıktı geliyor | Derlemeden `node` çalıştırdın | `npm run build` sonra çalıştır |
| `Object is possibly undefined` | Strict tip kontrolü | `?? 0` veya `if` kontrolü |
| `==` ile beklenmedik sonuç | JavaScript davranışı | `===` kullan |
| `True` / `False` hatası | Python büyük harf | TS: `true` / `false` |
| Girinti hatası yok ama kod çalışmıyor | `{ }` unutuldu | Her `if`/`for` sonrası `{ }` |
| `print` çalışmıyor | Node'da print yok | `console.log` kullan |
| Her dosya için npm init | Yanlış anlama | Tek proje, çok `.ts` dosyası |

---

## Bölüm 20 — Kendi kendine test

Okumayı bitirdikten sonra cevapla (cevaplar bu dosyada):

1. TypeScript neden doğrudan çalışmaz? Hangi araç `.js` üretir?
2. `const` ve `let` farkı nedir? Faktöriyelde `sonuc` neden `let`?
3. `for (const kelime of kelimeler)` Python'da neye denk?
4. `Record<string, number>` Python'da ne?
5. `?? 0` operatörü ne yapar?
6. `npm run functions` hangi iki işi yapar?
7. `interface Urun` ne işe yarar?
8. `duplicate_temizle` ve `[...new Set(liste)]` sonuç aynı mı? `sorted(Set)` neden farklı?

**Pratik test:** `week-05/src/` altına `deneme.ts` yaz:

```typescript
function ciftleriTopla(liste: number[]): number {
    let toplam = 0;
    for (const sayi of liste) {
        if (sayi % 2 === 0) {
            toplam += sayi;
        }
    }
    return toplam;
}

console.log(ciftleriTopla([1, 2, 3, 4, 5])); // 6 beklenir
```

Derle ve çalıştır. Çalışıyorsa Bölüm 1–10'u anladın demektir.

---

## İlgili dosyalar

| Dosya | Ne için? |
|---|---|
| `week-05/src/*.ts` | Yazdığın TypeScript kodları |
| `week-05/README.md` | Hafta raporu |
| `cheatsheets/typescript.md` | Hızlı referans (kısa) |
| `week-01/functions.py` | Python karşılıkları |
| `week-02/data_structures.py` | Python karşılıkları |
| `week-02/algorithms.py` | Python karşılıkları |

---

> **Sonraki adım:** Mini ürün listesi CLI (`product-list.ts`) ve terminalden girdi (`readline`) — staj programının 5. hafta 4. görevi.
