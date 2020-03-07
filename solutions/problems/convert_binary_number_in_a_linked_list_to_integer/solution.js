/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {number}
 */
var getDecimalValue = function(head) {
    let arr = [];
    let current = head;

    while (current) {
        arr.push(current.val)
        current = current.next;
    }

   return parseInt(arr.map(String).join(''), 2)
};