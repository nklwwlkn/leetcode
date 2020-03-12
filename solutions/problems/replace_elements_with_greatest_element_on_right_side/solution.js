/**
 * @param {number[]} arr
 * @return {number[]}
 */
var replaceElements = function(arr) {
    let i = arr.length - 1;
    

    while (i - 1 > 0) {
             if (arr[i] > arr[i-1]) {
              arr[i - 1] = arr[i]
            } 
            i--;
    }
    arr.shift();
    arr.push(-1)

    return arr
        
};