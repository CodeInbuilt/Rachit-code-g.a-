
class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}


class Queue {
    private Node front, rear;

    
    public Queue() {
        this.front = this.rear = null;
    }

    
    public void enqueue(int item) {
        Node newNode = new Node(item);

       
        if (rear == null) {
            front = rear = newNode;
            return;
        }

       
        rear.next = newNode;
        rear = newNode;
    }

    
    public int dequeue() {
        if (front == null) {
            System.out.println("Queue Underflow! Cannot dequeue.");
            return -1;
        }

        int value = front.data;
        front = front.next;

       
        if (front == null) {
            rear = null;
        }

        return value;
    }

    
    public int front() {
        if (front == null) {
            System.out.println("Queue is empty.");
            return -1;
        }
        return front.data;
    }

    
    public boolean isEmpty() {
        return front == null;
    }
}


public class Main {
    public static void main(String[] args) {
        Queue q = new Queue();

        q.enqueue(10);
        q.enqueue(20);
        q.enqueue(30);

        System.out.println("Front element: " + q.front());   
        System.out.println("Dequeued: " + q.dequeue());      
        System.out.println("Front element after dequeue: " + q.front()); 
        System.out.println("Is queue empty? " + q.isEmpty()); 

        q.dequeue();
        q.dequeue();
        System.out.println("Is queue empty after removing all? " + q.isEmpty()); 
    }
}
