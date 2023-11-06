/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle = function(moves) {
    let obj = {'ver' : 0, 'sides' : 0};

    if (moves.length % 2 === 1) return false;

    for (let val of moves) {
        if (val === "U") {
            obj['ver'] = (obj['ver'] | 0) + 1;
        } else if (val === 'D') {
            obj['ver'] = (obj['ver'] | 0) - 1;    
        } else if (val === 'R') {
            obj['sides'] = (obj['sides'] | 0) + 1;
        } else if (val === 'L') {
            obj['sides'] = (obj['sides'] | 0) - 1;
        }
    }

   return obj['ver'] === 0 && obj['sides'] === 0
};