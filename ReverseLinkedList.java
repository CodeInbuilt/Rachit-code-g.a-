public class ReverseLinkedList {
   
    public static class ListNode {
        public int val;
        public ListNode next;

        public ListNode(int x) {
            val = x;
            next = null;
        }
    }

    
    public static ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;

        while (curr != null) {
            ListNode nextTemp = curr.next; 
            curr.next = prev;              
            prev = curr;                   
            curr = nextTemp;              
        }

        return prev; 
    }

   
    public static void main(String[] args) {
        
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);

       
        head = reverseList(head);

      
        ListNode curr = head;
        while (curr != null) {
            System.out.print(curr.val + " ");
            curr = curr.next;
        }
    }
}
