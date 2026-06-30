// Terminalden kullanici girdisi almak icin readline modulu (Python'daki input() karsiligi)
import readline = require("node:readline/promises");
// stdin ve stdout erisimi icin process modulu
import process = require("node:process");

// Ana program fonksiyonu — async cunku input beklemek zaman alir
async function main(): Promise<void> {
    // Cikis kontrolu — Python'daki on_off = 0 ile ayni (0 = devam, 1 = cik)
    let onOff = 0;
    // Urunleri tutan bos liste — Python'daki gorevler = [] gibi
    const urunler: string[] = [];

    // readline arayuzunu olustur: klavyeden oku, ekrana yaz
    const rl = readline.createInterface({
        input: process.stdin,   // klavye girisi
        output: process.stdout, // ekran ciktisi
    });

    // Cikis secilene kadar dongu — Python: while on_off != 1
    while (onOff !== 1) {
        console.log("--------------------------------");       // ayirici cizgi
        console.log("--- Mini Urun Listesi ---");             // baslik
        console.log("1. Urun ekle");                         // menu secenek 1
        console.log("2. Urunleri listele");                  // menu secenek 2
        console.log("3. Urun sil");                          // menu secenek 3
        console.log("4. Cikis");                             // menu secenek 4
        console.log("--------------------------------");       // ayirici cizgi

        // Kullanicidan secim al ve sayiya cevir — Python: secim = int(input(...))
        const secim = Number(await rl.question("Seciminizi yapin: "));

        if (secim === 4) {
            onOff = 1;                                         // cikis — Python: on_off = 1
        } else if (secim === 1) {
            const urun = await rl.question("Urunu girin: ");   // urun adi sor — Python: input(...)
            urunler.push(urun);                                // listeye ekle — Python: append
        } else if (secim === 2) {
            if (urunler.length === 0) {                        // liste bos mu — Python: gorevler == []
                console.log("--------------------------------");
                console.log("Urunler yok");
                console.log("--------------------------------");
            } else {
                console.log("--------------------------------");
                for (const urun of urunler) {                  // her urunu gez — Python: for gorev in gorevler
                    console.log(`${urunler.indexOf(urun) + 1}. ${urun}`); // numara + urun yazdir
                }
                console.log("--------------------------------");
            }
        } else if (secim === 3) {
            if (urunler.length === 0) {                        // silinecek urun yok
                console.log("--------------------------------");
                console.log("Urunler yok");
                console.log("--------------------------------");
            } else {
                const urun = await rl.question("Silinecek urunun numarasini girin: "); // hangi sira silinecek
                if (Number(urun) > urunler.length) {           // gecersiz numara — Python: int(gorev) > len(...)
                    console.log("--------------------------------");
                    console.log("Urun bulunamadi");
                    console.log("--------------------------------");
                } else {
                    urunler.splice(Number(urun) - 1, 1);       // o siradaki urunu sil — Python: pop(...)
                    console.log("--------------------------------");
                    console.log("Urun silindi");
                    console.log("--------------------------------");
                }
            }
        }
    }

    rl.close();                                                // readline arayuzunu kapat
    console.log("Program sonlandirildi");                      // Python'daki son print
}

main();                                                        // programi baslat
