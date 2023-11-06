/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const hashMap = {};
    
    for (let str of strs) {
        let hash = getHash(str)
        let group = hashMap[hash] || []
        
        group.push(str)
        
        hashMap[hash] = group
    }
    
    return [...Object.values(hashMap)]
    
};

function getHash(word) {
    const frequency = new Array(26).fill(0);
    
    for (char of word) {
        const charIndex = getCharIndex(char);
        
        frequency[charIndex]++
    }
    
    return buildHash(frequency)
    
}
    
function getCharIndex(char) {
    return char.charCodeAt(0) - 'a'.charCodeAt(0)
}

function buildHash(frequency) {
    return frequency.map((charFrequency) => `#${charFrequency}`).join('')
}