function Counter(arr: Array<any>) {
    let obj = {}

    arr.forEach(val => obj[val]= (obj[val] || 0) + 1);

    return obj
}

function isAnagram(s: string, t: string): boolean {
    if (s.length !== t.length) return false
    
    const counterS = Counter(s.split(''));
    const counterT = Counter(t.split(''));

    for (let prop in counterS) {
        if (counterT[prop] !== counterS[prop]) {
            return false
        }
    }

    return true
};