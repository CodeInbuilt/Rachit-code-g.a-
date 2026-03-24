class Stack {
    private int[] arr;   
    private int top;     
    private int capacity; 

    
    public Stack(int size) {
        arr = new int[size];
        capacity = size;
        top = -1;
    }

    
    public void push(int item) {
        if (top == capacity - 1) {
            System.out.println("Stack Overflow! Cannot push " + item);
            return;
        }
        arr[++top] = item;
        System.out.println(item + " pushed to stack.");
    }

    
    public int pop() {
        if (isEmpty()) {
            System.out.println("Stack Underflow! Cannot pop.");
            return -1;
        }
        return arr[top--];
    }

    
    public int peek() {
        if (isEmpty()) {
            System.out.println("Stack is empty! Nothing to peek.");
            return -1;
        }
        return arr[top];
    }

  
    public boolean isEmpty() {
        return top == -1;
    }

   
    public void display() {
        if (isEmpty()) {
            System.out.println("Stack is empty.");
            return;
        }
        System.out.print("Stack (top → bottom): ");
        for (int i = top; i >= 0; i--) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

   
    public static void main(String[] args) {
        Stack stack = new Stack(5);

        stack.push(10);
        stack.push(20);
        stack.push(30);
        stack.display();

        System.out.println("Peek: " + stack.peek());
        System.out.println("Pop: " + stack.pop());
        stack.display();
        System.out.println("Is Empty? " + stack.isEmpty());
    }
}
