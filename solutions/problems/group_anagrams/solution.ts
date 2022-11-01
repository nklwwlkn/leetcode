function groupAnagrams(strs: string[]): string[][] {
    if (strs.length === 1) return [strs]
    
    const map = new Map();
    
    for (let word of strs) {
        let sortedWord = word.split('').sort().join('')
        
        if (!map.has(sortedWord)) {
            map.set(sortedWord, [word])
        } else {
            map.get(sortedWord).push(word)
        }
        
    }
    
       return [...map.values()]
};