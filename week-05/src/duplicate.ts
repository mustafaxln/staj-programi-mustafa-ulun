function duplicate (list: number[]): number[] {

    
    let sonuc: number[] = [];

    for (let item of list) {
        if (!sonuc.includes(item)) {
            sonuc.push(item);
        }
        
    }
    return sonuc;
}

console.log(duplicate([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]));
console.log(duplicate([1, 1, 1, 1, 1]));
console.log(duplicate([1, 2, 3, 4, 5]));
console.log(duplicate([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]));
console.log(duplicate([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]));