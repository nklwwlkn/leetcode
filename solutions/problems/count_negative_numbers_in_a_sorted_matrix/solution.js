/**
 * @param {number[][]} grid
 * @return {number}
 */
var countNegatives = function(grid) {
    let counter = 0;
    let resultArr = [];

    let flat = arr => {
    if (arr.length <= 0) return arr;

    for (let i = 0; i < arr.length; i++) {
        resultArr.push(...arr[i]);
        return flat(arr.slice(1));
    }
}
    flat(grid);

     resultArr.forEach(el => {
        if (el < 0) {
           counter++;
        }
    });

    return counter;
};
