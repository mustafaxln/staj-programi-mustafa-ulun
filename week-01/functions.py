def toplama(a, b):
    """
    İki sayının toplamını döndürür.
    """
    return a + b

def faktoriyel(n):
    """
    n sayısının faktoriyelini hesaplar.
    n >= 0 olmalıdır.
    """
    if n < 0:
        raise ValueError("Negatif sayıların faktoriyeli yoktur.")
    sonuc = 1
    for i in range(1, n + 1):
        sonuc *= i
    return sonuc

def palindrom_kontrolu(s):
    """
    Verilen stringin palindrom olup olmadığını kontrol eder.
    """
    s = str(s)
    return s == s[::-1]

def asal_sayi_kontrolu(n):
    """
    n sayısının asal olup olmadığını kontrol eder.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def liste_ortalamasi(liste):
    """
    Verilen listenin aritmetik ortalamasını hesaplar.
    Liste boşsa None döndürür.
    """
    if not liste:
        return None
    return sum(liste) / len(liste)

# --- Fonksiyonları test eden kodlar ---

if __name__ == "__main__":
    # toplama fonksiyonu testi
    print("Toplama (3, 5):", toplama(3, 5))  # 8

    # faktoriyel fonksiyonu testi
    print("Faktoriyel (5):", faktoriyel(5))  # 120
    # print("Faktoriyel (-1):", faktoriyel(-1))  # Hata verecek

    # palindrom kontrol fonksiyonu testi
    print("Palindrom kontrolü ('kayak'):", palindrom_kontrolu("kayak"))  # True
    print("Palindrom kontrolü ('python'):", palindrom_kontrolu("python"))  # False

    # asal sayı kontrolü testi
    print("Asal sayı kontrolü (7):", asal_sayi_kontrolu(7))  # True
    print("Asal sayı kontrolü (10):", asal_sayi_kontrolu(10))  # False

    # liste ortalaması testi
    print("Liste ortalaması ([1,2,3,4,5]):", liste_ortalamasi([1,2,3,4,5]))  # 3.0
    print("Liste ortalaması ([]):", liste_ortalamasi([]))  # None