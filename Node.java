
class Stack {
    
    private class Node {
        int data;
        Node next;

        Node(int value) {
            data = value;
            next = null;
        }
    }

    private Node top; 

    
    public Stack() {
        top = null;
    }

    
    public void push(int value) {
        Node newNode = new Node(value);
        newNode.next = top; 
        top = newNode;      
        System.out.println(value + " pushed to stack");
    }

    
    public int pop() {
        if (isEmpty()) {
            System.out.println("Stack Underflow! Cannot pop.");
            return -1; 
        }
        int popped = top.data;
        top = top.next; 
        return popped;
    }

    
    public int peek() {
        if (isEmpty()) {
            System.out.println("Stack is empty!");
            return -1; 
        }
        return top.data;
    }

    
    public boolean isEmpty() {
        return top == null;
    }

   
    public void display() {
        if (isEmpty()) {
            System.out.println("Stack is empty!");
            return;
        }
        Node temp = top;
        System.out.print("Stack elements: ");
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }

    
    public static void main(String[] args) {
        Stack stack = new Stack();
        stack.push(10);
        stack.push(20);
        stack.push(30);

        stack.display();

        System.out.println("Top element is: " + stack.peek());
        System.out.println(stack.pop() + " popped from stack");
        stack.display();
        System.out.println("Is stack empty? " + stack.isEmpty());
    }
}
