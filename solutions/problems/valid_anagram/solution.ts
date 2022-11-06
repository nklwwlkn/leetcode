
function isAnagram(s: string, t: string): boolean {
    if (s.length !== t.length) return false
    
    const counterS = {};
    const counterT = {};
    
    for (let i = 0; i < s.length; i++) {
        counterS[s[i]] = (counterS[s[i]] || 0) + 1;
        counterT[t[i]] = (counterT[t[i]] || 0) + 1;
    }
    
    for (let prop in counterS) {
        if (counterT[prop] !== counterS[prop]) {
            return false
        }
    }

    return true
};