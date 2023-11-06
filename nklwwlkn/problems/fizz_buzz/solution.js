/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    let resultArr = [];
    let i = 1;

    while (i <= n) {
        if (i % 5 === 0 && i % 3 === 0) {
            resultArr.push("FizzBuzz");
        } else if (i % 5 === 0) {
            resultArr.push("Buzz");
        } else if (i % 3 === 0) {
            resultArr.push("Fizz");
        } else {
            resultArr.push(`${i}`);  
        }
     
        i++;
    }    
    return resultArr;
};
