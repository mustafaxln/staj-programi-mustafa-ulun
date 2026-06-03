# Kullanicidan iki sayi alip toplama, cikarma, carpma, bolme yapan program

# Kullanıcıdan iki sayıyı al
sayi1 = float(input("Birinci sayiyi girin: "))
sayi2 = float(input("Ikinci sayiyi girin: "))

# İslem secimi
print("Yapmak istediginiz islemi secin:")
print("1. Toplama (+)")
print("2. Cikarma (-)")
print("3. Carpma (*)")
print("4. Bolme (/)")

secim = input("Seciminiz (1/2/3/4): ")

if secim == '1' or secim == '+':
    sonuc = sayi1 + sayi2
    print("Toplam:", sonuc)
elif secim == '2' or secim == '-':
    sonuc = sayi1 - sayi2
    print("Fark:", sonuc)
elif secim == '3' or secim == '*':
    sonuc = sayi1 * sayi2
    print("Carpim:", sonuc)
elif secim == '4' or secim == '/':
    if sayi2 != 0:
        sonuc = sayi1 / sayi2
        print("Bolum:", sonuc)
    else:
        print("Bir sayi sifira bolunemez!")
else:
    print("Hatali secim yaptiniz!")