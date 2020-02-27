/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */


let twoSum = (arr, target) => {
    if (arr.length === 2) return [0,1]

    for (let i = 0; i < arr.length; i++) {
        for (let j = i + 1; j < arr.length; j++) {
            if ((arr[i] + arr[j]) === target) {
                return [i,j];
            } 
        }
    }

}
