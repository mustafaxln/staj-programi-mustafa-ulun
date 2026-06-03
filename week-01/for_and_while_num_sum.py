# Kullanıcıdan 10 sayı alıp bir listeye ekleyelim
sayilar = []
for i in range(1, 11):
    sayi = float(input(f"{i}. sayiyi girin: "))
    sayilar.append(sayi)

# For döngüsü ile listedeki elemanları toplayalım
sum_for = 0
for n in sayilar:
    sum_for += n
print("For döngüsüyle toplam:", sum_for)

# While döngüsü ile listedeki elemanları toplayalım
sum_while = 0
i = 0
while i < len(sayilar):
    sum_while += sayilar[i]
    i += 1
print("While döngüsüyle toplam:", sum_while)