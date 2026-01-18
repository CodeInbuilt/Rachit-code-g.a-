// Definition for singly-linked list.
public class ListNode {
    int val;
    ListNode next;

    ListNode() {} // default constructor

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class Solution {

    // Iterative method to reverse a singly linked list
    public ListNode reverseListIterative(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;

        while (curr != null) {
            ListNode nextTemp = curr.next; // temporarily store next
            curr.next = prev;              // reverse the link
            prev = curr;                   // move prev forward
            curr = nextTemp;               // move curr forward
        }

        return prev; // new head of reversed list
    }

    // Recursive method to reverse a singly linked list
    public ListNode reverseListRecursive(ListNode head) {
        if (head == null || head.next == null)
            return head;

        ListNode newHead = reverseListRecursive(head.next);
        head.next.next = head;
        head.next = null;

        return newHead;
    }

    // Utility method to print the list
    public void printList(ListNode head) {
        System.out.print("[");
        while (head != null) {
            System.out.print(head.val);
            if (head.next != null) System.out.print(", ");
            head = head.next;
        }
        System.out.println("]");
    }

    // Example usage
    public static void main(String[] args) {
        Solution sol = new Solution();

        // Create list: [1, 2, 3, 4, 5]
        ListNode head = new ListNode(1,
                            new ListNode(2,
                            new ListNode(3,
                            new ListNode(4,
                            new ListNode(5)))));

        System.out.print("Original List: ");
        sol.printList(head);

        // Reverse using iterative method
        ListNode reversedIterative = sol.reverseListIterative(head);
        System.out.print("Reversed List (Iterative): ");
        sol.printList(reversedIterative);

        // Recreate list for recursive reversal
        head = new ListNode(1,
               new ListNode(2,
               new ListNode(3,
               new ListNode(4,
               new ListNode(5)))));

        // Reverse using recursive method
        ListNode reversedRecursive = sol.reverseListRecursive(head);
        System.out.print("Reversed List (Recursive): ");
        sol.printList(reversedRecursive);
    }
}
