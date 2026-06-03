
def fibonacci(n):
    """n terimli Fibonacci dizisi üretir."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    dizi = [0, 1]
    while len(dizi) < n:
        dizi.append(dizi[-1] + dizi[-2])
    return dizi

def binary_search(liste, aranan):
    """Bir sıralı listede binary search ile aranan elemanın indeksini döndürür. Yoksa -1 döner."""
    sol = 0
    sag = len(liste) - 1
    while sol <= sag:
        orta = (sol + sag) // 2
        if liste[orta] == aranan:
            return orta
        elif liste[orta] < aranan:
            sol = orta + 1
        else:
            sag = orta - 1
    return -1

def liste_ters_cevir(liste):
    """Bir listenin tersini döndürür (kendi orjinalini değiştirmez)."""
    return liste[::-1]

def liste_reverse_ile_ters_cevir(liste):
    """
    Verilen listeyi reverse() ile ters çevirip döndürür. 
    """
    liste.reverse()
    return liste


def duplicate_temizle(liste):
    """Bir listedeki tekrar edenleri temizleyip, yeni bir liste döndürür (orjinal sıralamayı koruyacak şekilde)."""
    gorulen = set()
    sonuc = []
    for eleman in liste:
        if eleman not in gorulen:
            gorulen.add(eleman)
            sonuc.append(eleman)
    return sonuc


def duplicate_temizle_dict(liste):
    """
    dict.fromkeys ile tekrarlari temizler.
    Ilk gordugu sirayi korur; orijinal listeyi degistirmez.
    """
    return list(dict.fromkeys(liste))

def en_uzun_kelimeyi_bul(kelimeler):
    """Bir kelime listesindeki en uzun kelimeyi/kelimeleri döndürür (list olarak, birden fazla olabilir)."""
    if not kelimeler:
        return []
    max_uz = max(len(k) for k in kelimeler)
    return [k for k in kelimeler if len(k) == max_uz]


# Test kodları
if __name__ == "__main__":
    print("Fibonacci fonksiyonu testleri:")
    print("fibonacci(0):", fibonacci(0))
    print("fibonacci(1):", fibonacci(1))
    print("fibonacci(5):", fibonacci(5))
    print("fibonacci(10):", fibonacci(10))

    print("\nBinary search fonksiyonu testleri:")
    sirali = [1, 3, 5, 7, 9, 11, 13]
    print("Arama (7):", binary_search(sirali, 7))      # 3
    print("Arama (1):", binary_search(sirali, 1))      # 0
    print("Arama (13):", binary_search(sirali, 13))    # 6
    print("Arama (8):", binary_search(sirali, 8))      # -1

    print("\nListe ters cevirme — iki yontem karsilastirmasi (ek tekrar):")
    orijinal_slice = [10, 20, 30, 40]
    print("Slice [::-1] oncesi orijinal:", orijinal_slice)
    print("Slice ile ters:", liste_ters_cevir(orijinal_slice))
    print("Slice sonrasi orijinal degisti mi?:", orijinal_slice)  # degismez

    orijinal_reverse = [10, 20, 30, 40]
    print("\nreverse() oncesi orijinal:", orijinal_reverse)
    print("reverse() ile ters:", liste_reverse_ile_ters_cevir(orijinal_reverse))
    print("reverse() sonrasi orijinal (ayni liste nesnesi):", orijinal_reverse)  # yerinde degisti
    print("Fark: [::-1] yeni liste uretir; .reverse() girdigi listeyi kalici ters cevirir.")

    print("\nDuplicate temizleme — iki yontem karsilastirmasi (ek tekrar):")
    tekrarli = [5, 1, 4, 1, 3, 5, 2]
    print("Orijinal liste:", tekrarli)
    sonuc_dongu = duplicate_temizle(tekrarli)
    sonuc_dict = duplicate_temizle_dict(tekrarli)
    sonuc_sirali_set = sorted(set(tekrarli))
    print("Dongu + set (ilk gorulme sirasii):", sonuc_dongu)
    print("dict.fromkeys ile:", sonuc_dict)
    print("sorted(set()) ile (kucukten buyuge siralar):", sonuc_sirali_set)
    print("Orijinal liste degisti mi?:", tekrarli)
    print("Dongu ve dict.fromkeys ayni mi?:", sonuc_dongu == sonuc_dict)
    print("Ilk-sira yontemi ile sorted(set) ayni mi?:", sonuc_dongu == sonuc_sirali_set)
    print("Fark: dongu ve dict.fromkeys [5,1,4,3,2] gibi ilk gecis sirasini korur; "
          "sorted(set()) tekrarlari siler ama listeyi sayisal/alfabetik siraya ceker.")

    print("\nEn uzun kelimeyi bulma testleri:")
    kelimeler = ["elma", "armut", "mango", "karpuz", "kavun", "muz"]
    print("En uzun(lar):", en_uzun_kelimeyi_bul(kelimeler))   # ['karpuz']
    kelimeler2 = []
    print("Bos liste:", en_uzun_kelimeyi_bul(kelimeler2))     # []
    kelimeler3 = ["a", "ab", "abc", "abcd", "efgh", "xyz"]
    print("Birden fazla uzun:", en_uzun_kelimeyi_bul(kelimeler3))  # ['abcd', 'efgh']

