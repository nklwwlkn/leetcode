/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
    let current = head;
    let i = 0;
    let j = 0;

    while (current) {
        i++;
        current = current.next;
    }


    if (i % 2 === 0) {
        current = head;
        while (j !== (i / 2)) {
            current = current.next;
            j++;
        }
    } else {
        current = head;
        while (j !== Math.floor(i / 2)) {
            current = current.next;
            j++;
        }
    }
    return current
};