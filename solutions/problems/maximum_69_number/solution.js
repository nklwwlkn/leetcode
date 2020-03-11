/**
 * @param {number} num
 * @return {number}
 */
var maximum69Number  = function(num) {
    for (let val of String(num)) {
        if (val === '6') {
            num = String(num).replace(val, '9');
            break;
        }
    }
    return Number(num);
};