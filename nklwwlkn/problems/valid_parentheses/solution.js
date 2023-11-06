/**
 * @param {string} s
 * @return {boolean}
 */


var isValid = function(s) {
    const stack = [];
    
    for (let i = 0; i < s.length; i++) {
        let val = s[i];
        if (val === "(") {
            stack.push(")")
        }
        
        else if (val === "{") {
            stack.push('}')
        }

        else if (val === "[") {
            stack.push(']')
        }

        else {
            if (stack.pop() !== val) {
                return false
            }    
        }
        
    }
    
    return stack.length === 0
};