function asal (n: number): boolean {

    if(n < 2){
        return false;
    }

    for(let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0){
            return false;
        }
    }

    return true;
}

console.log(asal(17));
console.log(asal(25));
