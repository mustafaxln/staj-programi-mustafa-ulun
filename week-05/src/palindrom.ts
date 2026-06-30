function palindrom(str: string): boolean {
    return str === str.split('').reverse().join('');
}

console.log(palindrom('kayak'));
console.log(palindrom('hello'));
console.log(palindrom('madam'));
console.log(palindrom('racecar'));
console.log(palindrom('noon'));