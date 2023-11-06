/**
 * @param {string} S
 * @return {number[]}
 */
var diStringMatch = function(S) {
    let arr = [];
    let increasePointer = 0;
    let decreasePointer = S.length;
    let i = 0;
    let tracker;

    while (i <= S.length) {
        if (S[i] === 'I') {
            arr.push(increasePointer);
            increasePointer++;
            tracker = increasePointer;
        } else if (S[i] === 'D') {
            arr.push(decreasePointer);
            decreasePointer--;
            tracker = decreasePointer;
        } else if (i === S.length) arr.push(tracker);
        i++;
    }

    return arr;
};