# Hafta 01 — Python Temelleri

## Ne yaptım

Python ile temel programlama alıştırmaları yaptım:

| Dosya | Açıklama |
|---|---|
| `hello.py` | İlk "Hello, world!" programı |
| `age_check.py` | Yaş kontrolü (`if/else`) |
| `odd_or_even.py` | Tek/çift sayı kontrolü |
| `pass_or_fail.py` | Not ortalaması ile geçti/kaldı |
| `calculator.py` | Dört işlem hesap makinesi |
| `number_analyzer.py` | 5 sayının toplam, ortalama, min/max analizi |
| `for_and_while_num_sum.py` | `for` ve `while` ile liste toplama |
| `functions.py` | Toplama, faktöriyel, palindrom, asal sayı, liste ortalaması fonksiyonları |

## Nasıl çalıştırılır

Python 3 yüklü olmalı. Terminalde `week-01` klasörüne girip dosyayı çalıştırın:

```bash
cd week-01
python3 hello.py
python3 age_check.py
python3 calculator.py
python3 functions.py
```

`input()` kullanan programlar sizden değer girmenizi bekler; `functions.py` doğrudan test çıktısı üretir.

## Ne öğrendim

- Değişken tanımlama, `print()` ve `input()` kullanımı
- `int` / `float` dönüşümü ve temel aritmetik
- `if`, `elif`, `else` ile koşullu dallanma
- `for` ve `while` döngüleri, listeler (`append`, `sum`, `max`, `min`)
- Fonksiyon tanımlama, `return`, docstring ve `if __name__ == "__main__"`
- Sıfıra bölme gibi basit hata kontrolü

## Nerede takıldım

- `input()` her zaman string döndürür; sayısal işlemler için `int()` / `float()` dönüşümü gerekir
- `elif` zincirinde koşul sırası ve girinti (indentation) hataları
- `for` ile `while` arasındaki fark; indeks takibi (`i += 1`)
- Palindrom kontrolünde `s[::-1]` dilimleme sözdizimi
- Asal sayı algoritmasında `range(2, int(n ** 0.5) + 1)` mantığı
