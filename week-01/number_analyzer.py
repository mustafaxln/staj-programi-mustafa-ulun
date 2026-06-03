# Kullanıcıdan 5 sayı alıp bunların toplamını, ortalamasını, en büyük ve en küçük değerini bulan program

sayilar = []

for i in range(1, 6):
    sayi = float(input(f"{i}. sayiyi girin: "))
    sayilar.append(sayi)

toplam = sum(sayilar)
ortalama = toplam / len(sayilar)
en_buyuk = max(sayilar)
en_kucuk = min(sayilar)

print("Toplam:", toplam)
print("Ortalama:", ortalama)
print("En buyuk:", en_buyuk)
print("En kucuk:", en_kucuk)