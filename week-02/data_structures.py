
# 1. Liste icinde arama yapan program
def arama_yap(liste, aranan):
    """Bir listenin icinde aranan eleman var mi, varsa indexini dondurur."""
    for i, eleman in enumerate(liste):
        if eleman == aranan:
            print(f"{aranan} bulundu! (Index: {i})")
            return i
    print(f"{aranan} listede yok.")
    return -1

# Ornek kullanim
# arama_yap([1, 3, 5, 7, 9], 5)

# 2. Liste icinde tekrar eden elemanlari bulan program
def tekrar_edenleri_bul(liste):
    """Bir liste icinde tekrar eden elemanlari bulup, liste olarak dondurur."""
    gorulen = set()
    tekrar_edenler = set()
    for eleman in liste:
        if eleman in gorulen:
            tekrar_edenler.add(eleman)
        else:
            gorulen.add(eleman)
    print("Tekrar edenler:", list(tekrar_edenler))
    return list(tekrar_edenler)

# Ornek kullanim
# tekrar_edenleri_bul([1,2,3,2,4,5,1,6,7,3,8,5])

# 3. Bir cumledeki kelime frekanslarini hesaplayan program
def kelime_frekanslari(cumle):
    """Bir cumlede her kelimenin kac defa gectigini bulur."""
    kelimeler = cumle.split()
    frekans = {}
    for kelime in kelimeler:
        if kelime in frekans:
            frekans[kelime] += 1
        else:
            frekans[kelime] = 1
    for k, v in frekans.items():
        print(f"{k!r}: {v}")
    return frekans

# Ornek kullanim
# kelime_frekanslari("python kolay ve python guclu bir dil kolay kolay oyrenilmez")

# 4. Bir ogrenci listesi icinde en yuksek notu alan ogrenciyi bulan program
def en_yuksek_notu_bulan(ogrenciler):
    """
    ogrenciler: [('Ali', 75), ('Veli', 82), ...]
    En yuksek notu alan ogrenciyi (isim ve not ile birlikte) dondurur.
    """
    if not ogrenciler:
        print("Ogrenci listesi bos!")
        return None
    en_yuksek = ogrenciler[0]
    for ogrenci in ogrenciler[1:]:
        if ogrenci[1] > en_yuksek[1]:
            en_yuksek = ogrenci
    print(f"En yuksek notu alan: {en_yuksek[0]} (Notu: {en_yuksek[1]})")
    return en_yuksek

# Ornek kullanim
# en_yuksek_notu_bulan([('Ahmet', 70), ('Ayse', 90), ('Mehmet', 85)])

# 5. Dict kullanarak mini bir urun katalogu (ID -> urun bilgisi) yapisi kurmak
def urun_katalogu_olustur():
    """
    Ürün katalogunu bir dict olarak olusturur.
    Anahtar: urun id (int veya string)
    Deger: urun ozelliklerini tutan dict
    """
    katalog = {
        101: {"isim": "Laptop", "fiyat": 15000, "stok": 7},
        102: {"isim": "Klavye", "fiyat": 350, "stok": 33},
        103: {"isim": "Mouse", "fiyat": 200, "stok": 42},
        104: {"isim": "Monitor", "fiyat": 2400, "stok": 9},
        105: {"isim": "USB Bellek", "fiyat": 120, "stok": 61},
    }
    print("Urun katalogu hazirlandi:")
    for uid, bilgi in katalog.items():
        print(f"ID: {uid} | Isim: {bilgi['isim']} | Fiyat: {bilgi['fiyat']} TL | Stok: {bilgi['stok']}")
    return katalog

# Ornek kullanim
# katalog = urun_katalogu_olustur()


# Fonksiyonlari test eden kodlar

if __name__ == "__main__":

    print("1. arama_yap fonksiyonu testleri")
    liste1 = [3, 8, 6, 1, 5]
    print("Test1:", arama_yap(liste1, 6))    # 6 bulundu! (Index: 2), return 2
    print("Test2:", arama_yap(liste1, 10))   # 10 listede yok., return -1
    liste2 = ['elma', 'armut', 'kiraz']
    print("Test3:", arama_yap(liste2, 'armut'))  # armut bulundu! (Index: 1), return 1
    print("Test4:", arama_yap(liste2, 'muz'))    # muz listede yok., return -1

    print("\n2. tekrar_edenleri_bul fonksiyonu testleri")
    print("Test1:", tekrar_edenleri_bul([1, 2, 3, 2, 4, 5, 1, 6, 7, 3, 8, 5]))  # Ciktilar: 1,2,3,5 (sira fark edebilir)
    print("Test2:", tekrar_edenleri_bul(['a', 'b', 'c', 'b', 'a', 'd']))  # Ciktilar: a, b

    print("\n3. kelime_frekanslari fonksiyonu testleri")
    cumle1 = "python kolay ve python guclu bir dil kolay kolay oyrenilmez"
    print("Test1:", kelime_frekanslari(cumle1))
    cumle2 = "merhaba dunya dunya merhaba"
    print("Test2:", kelime_frekanslari(cumle2))

    print("\n4. en_yuksek_notu_bulan fonksiyonu testleri")
    ogrenciler1 = [('Ahmet', 70), ('Ayse', 90), ('Mehmet', 85)]
    print("Test1:", en_yuksek_notu_bulan(ogrenciler1))  # Ayse, 90
    ogrenciler2 = [('Ali', 75)]
    print("Test2:", en_yuksek_notu_bulan(ogrenciler2))  # Ali, 75
    ogrenciler3 = []
    print("Test3:", en_yuksek_notu_bulan(ogrenciler3))  # None, bos uyarisi

    print("\n5. urun_katalogu_olustur fonksiyonu testleri")
    katalog = urun_katalogu_olustur()  # fonksiyon zaten içerde print ediyor

    # Ek: katalog içinden bir ürünün bilgisine ulaşma örneği
    ornek_id = 102
    if ornek_id in katalog:
        urun = katalog[ornek_id]
        print(f"\nID {ornek_id} urunu: Isim: {urun['isim']}, Fiyat: {urun['fiyat']} TL, Stok: {urun['stok']}")
    else:
        print(f"\nID {ornek_id} urunu katalogda yok.")

    


