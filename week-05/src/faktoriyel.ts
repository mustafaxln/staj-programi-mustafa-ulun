function faktoriyel(n: number): number {
    
    if (n < 0) {
        throw new Error("Negatif sayilarin faktoriyeli yoktur.");
    }

    let sonuc = 1;
    for (let i = 1; i <= n; i++) {
        sonuc *= i;
    }

    return sonuc;   

}

console.log(faktoriyel(5)); // 120