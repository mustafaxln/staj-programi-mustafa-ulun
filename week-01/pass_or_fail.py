# Kullanıcıdan iki not alalım
not1 = float(input("Birinci notu girin: "))
not2 = float(input("Ikinci notu girin: "))

# Notların ortalamasını hesaplayalım
ortalama = (not1 + not2) / 2

# Sonucu kontrol edelim
if ortalama >= 50:
    print("Geçtiniz! Ortalama:", ortalama)
else:
    print("Kaldınız. Ortalama:", ortalama)