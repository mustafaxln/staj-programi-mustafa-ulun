# week-04: queries.sql dosyasindaki sorgulari shop.db uzerinde calistirir

import sqlite3
from pathlib import Path

# --- Dosya yollari ---
# __file__ = bu .py dosyasinin tam yolu
# .parent    = week-04 klasoru
KLASOR = Path(__file__).parent
DB_DOSYASI = KLASOR / "shop.db"
SORGULAR_DOSYASI = KLASOR / "queries.sql"

# Ekranda gosterilecek basliklar (her sorgu icin bir tane)
BASLIKLAR = [
    "1. En cok siparis veren kullanici",
    "2. En cok satilan urun",
    "3. Toplam siparis tutari",
    "4. Hic satilmayan urunler",
]


def main():
    # 1) Veritabanina baglan
    conn = sqlite3.connect(DB_DOSYASI)
    cursor = conn.cursor()

    # 2) queries.sql dosyasini oku
    with open(SORGULAR_DOSYASI, encoding="utf-8") as dosya:
        sql_metni = dosya.read()

    # 3) Her sorgu ; ile bittigi icin parcalara ayir
    sorgular = []
    for parca in sql_metni.split(";"):
        parca = parca.strip()
        if parca:
            sorgular.append(parca)

    # 4) Her sorguyu calistir ve sonucu yazdir
    for baslik, sorgu in zip(BASLIKLAR, sorgular):
        print("-" * 40)
        print(baslik)
        print("-" * 40)

        cursor.execute(sorgu)
        sonuclar = cursor.fetchall()

        if sonuclar:
            for satir in sonuclar:
                print(satir)
        else:
            print("(sonuc yok)")

        print()

    # 5) Baglantiyi kapat
    conn.close()


if __name__ == "__main__":
    main()
