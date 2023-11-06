/**
 * @param {number} n
 * @return {number[]}
 */
var sumZero = function(n) {
    let arr = [];
    let num;
    if (n % 2 === 0) {
        num = n / 2;
         while (0 < num) {
         arr.push(num);
         arr.push(-num);
         num--
    } 
    } else {

         num = Math.floor(n/2);
        arr.push(0);
        while (0 < num) {
         arr.push(num);
         arr.push(-num);
         num--
    }
    }
     
    
    return arr
   
};