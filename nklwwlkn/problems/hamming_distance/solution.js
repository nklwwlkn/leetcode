/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var hammingDistance = function(x, y) {

    let numX = x.toString(2).split('');
    let numY = y.toString(2).split('');
    let counter = 0;
    let i = 0;


    if (numX.length < numY.length) {
        while(numX.length < numY.length) {
            numX.unshift('0');
        } 
    } else if (numX.length > numY.length) {
        while(numX.length > numY.length) {
            numY.unshift('0');
        } 
    } 

        while (i < numX.length) {
            if (numX[i] !== numY[i]) {
                counter++;
            }
            i++;
        }

    return counter;
};