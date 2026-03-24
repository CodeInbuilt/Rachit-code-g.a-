public class CircularQueue {
    private int[] queue;   
    private int front;     
    private int rear;      
    private int size;      
    private int count;     

    
    public CircularQueue(int size) {
        this.size = size;
        queue = new int[size];
        front = 0;
        rear = -1;
        count = 0;
    }

    
    public void enqueue(int value) {
        if (isFull()) {
            System.out.println("Queue is full! Cannot enqueue " + value);
            return;
        }
        rear = (rear + 1) % size;
        queue[rear] = value;
        count++;
        System.out.println(value + " enqueued.");
    }

    
    public int dequeue() {
        if (isEmpty()) {
            System.out.println("Queue is empty! Cannot dequeue.");
            return -1;
        }
        int removed = queue[front];
        front = (front + 1) % size;
        count--;
        System.out.println(removed + " dequeued.");
        return removed;
    }

    
    public int front() {
        if (isEmpty()) {
            System.out.println("Queue is empty!");
            return -1;
        }
        return queue[front];
    }

    // Peek rear element
    public int rear() {
        if (isEmpty()) {
            System.out.println("Queue is empty!");
            return -1;
        }
        return queue[rear];
    }

    
    public boolean isEmpty() {
        return count == 0;
    }

    
    public boolean isFull() {
        return count == size;
    }

    
    public void display() {
        if (isEmpty()) {
            System.out.println("Queue is empty!");
            return;
        }
        System.out.print("Queue elements: ");
        for (int i = 0; i < count; i++) {
            System.out.print(queue[(front + i) % size] + " ");
        }
        System.out.println();
    }

    
    public static void main(String[] args) {
        CircularQueue cq = new CircularQueue(5);

        cq.enqueue(10);
        cq.enqueue(20);
        cq.enqueue(30);
        cq.enqueue(40);
        cq.display();

        System.out.println("Front element: " + cq.front());
        System.out.println("Rear element: " + cq.rear());

        cq.dequeue();
        cq.enqueue(50);
        cq.enqueue(60);  
        cq.display();
    }
}
