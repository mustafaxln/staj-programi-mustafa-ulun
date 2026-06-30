function kelime_frekanslari(cumle: string): Record<string, number> {
    /**
     * Bir cumlede her kelimenin kac defa gectigini bulur.
     */
    const kelimeler = cumle.split(" ");
    const frekans: Record<string, number> = {};

    for (const kelime of kelimeler) {
        if (kelime in frekans) {
            frekans[kelime] = frekans[kelime]! + 1;
        } else {
            frekans[kelime] = 1;
        }
    }

    for (const [k, v] of Object.entries(frekans)) {
        console.log(`${JSON.stringify(k)}: ${v}`);
    }

    return frekans;
}

// --- Test ---

console.log("\n1. kelime_frekanslari testi");
const cumle1 =
    "python kolay ve python guclu bir dil kolay kolay oyrenilmez";
console.log("Test1:", kelime_frekanslari(cumle1));

const cumle2 = "merhaba dunya dunya merhaba";
console.log("Test2:", kelime_frekanslari(cumle2));
