class Queue {
    private int[] arr;
    private int front, rear, size, capacity;

    
    public Queue(int capacity) {
        this.capacity = capacity;
        arr = new int[capacity];
        front = 0;
        rear = -1;
        size = 0;
    }

   
    public void enqueue(int x) {
        if (size == capacity) {
            System.out.println("Queue Overflow! Cannot enqueue " + x);
            return;
        }
        rear = (rear + 1) % capacity;  
        arr[rear] = x;
        size++;
    }

   
    public int dequeue() {
        if (isEmpty()) {
            System.out.println("Queue Underflow! Cannot dequeue");
            return -1;
        }
        int item = arr[front];
        front = (front + 1) % capacity;
        size--;
        return item;
    }

    
    public int front() {
        if (isEmpty()) {
            System.out.println("Queue is empty");
            return -1;
        }
        return arr[front];
    }

    
    public boolean isEmpty() {
        return size == 0;
    }

    
    public int size() {
        return size;
    }
}


public class QueueDemo {
    public static void main(String[] args) {
        Queue q = new Queue(5);

        q.enqueue(10);
        q.enqueue(20);
        q.enqueue(30);

        System.out.println("Front element: " + q.front()); 
        System.out.println("Dequeued: " + q.dequeue());     
        System.out.println("Front element: " + q.front());  
        System.out.println("Is empty? " + q.isEmpty());     

        q.enqueue(40);
        q.enqueue(50);
        q.enqueue(60);
        q.enqueue(70); 
    }
}
