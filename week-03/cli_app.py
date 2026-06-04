on_off = 0
gorevler = []

while on_off != 1:
    print("--------------------------------")
    print("--- CLI Uygulamasi ---")
    print("1. Gorev ekle")
    print("2. Gorevleri listele")
    print("3. Gorev sil")
    print("4. Cikis")
    print("--------------------------------")
    secim = int (input("Seciminizi yapin: "))
    if secim == 4:
        on_off = 1
    elif secim == 1:
        gorev = input("Gorevi girin: ")
        gorevler.append(gorev)
    elif secim == 2:
        if gorevler == []:
            print("--------------------------------")
            print("Gorevler yok")
            print("--------------------------------")
        else:
            print("--------------------------------")
            for gorev in gorevler:
                print(f"{gorevler.index(gorev) + 1}. {gorev}")
            print("--------------------------------")
    elif secim == 3:
        if gorevler == []:
            print("--------------------------------")
            print("Gorevler yok")
            print("--------------------------------")
        else:
            gorev = input("Silinecek gorevin numarasini girin: ")
            if int(gorev) > len(gorevler):
                print("--------------------------------")
                print("Gorev bulunamadi")
                print("--------------------------------")
            else:
                gorevler.pop(int(gorev) - 1)
                print("--------------------------------")
                print("Gorev silindi")
                print("--------------------------------")

print("Program sonlandirildi")



