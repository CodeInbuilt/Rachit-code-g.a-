class CycleListNode {
    int val;
    CycleListNode next;

    CycleListNode(int x) {
        val = x;
        next = null;
    }
}

public class DetectCycle {
    public static boolean hasCycle(CycleListNode head) {
        if (head == null || head.next == null) {
            return false;
        }

        CycleListNode slow = head;
        CycleListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;          // move slow by 1
            fast = fast.next.next;     // move fast by 2

            if (slow == fast) {        // cycle detected
                return true;
            }
        }

        return false; // no cycle
    }

    public static void main(String[] args) {
        // Create a linked list with a cycle
        CycleListNode head = new CycleListNode(1);
        head.next = new CycleListNode(2);
        head.next.next = new CycleListNode(3);
        head.next.next.next = head; // creates a cycle

        System.out.println(hasCycle(head)); // Expected: true
        System.out.println("Head value: " + head.val);
    }
}
