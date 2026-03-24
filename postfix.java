import java.util.*;  

public class Postfix {
    public static int evaluatePostfix(String exp) {
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < exp.length(); i++) {
            char c = exp.charAt(i);

            if (Character.isDigit(c)) {
                stack.push(c - '0');  
            } else {
                int val1 = stack.pop();
                int val2 = stack.pop();

                switch (c) {
                    case '+':
                        stack.push(val2 + val1);
                        break;
                    case '-':
                        stack.push(val2 - val1);
                        break;
                    case '*':
                        stack.push(val2 * val1);
                        break;
                    case '/':
                        stack.push(val2 / val1);
                        break;
                }
            }
        }
        return stack.pop(); // final result
    }

    public static void main(String[] args) {
        String expr1 = "231*+9-"; // 2 + (3*1) - 9 = -4
        String expr2 = "123+*";   // 1 * (2+3) = 5

        System.out.println("Result: " + evaluatePostfix(expr1));
        System.out.println("Result: " + evaluatePostfix(expr2));
    }
}
