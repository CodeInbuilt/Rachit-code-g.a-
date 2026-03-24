import java.util.*;

public class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            
            if (ch == '[' || ch == '{' || ch == '(') {
                st.push(ch);
            } else {
               
                if (st.isEmpty()) {
                    return false;
                }

                char top = st.peek();
                if ((top == '[' && ch == ']') ||
                    (top == '(' && ch == ')') ||
                    (top == '{' && ch == '}')) {
                    st.pop();
                } else {
                    return false;
                }
            }
        }
        return st.isEmpty();
    }

    
    public static void main(String[] args) {
        Solution sol = new Solution();
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter brackets string: ");
        String input = sc.nextLine();
        if (sol.isValid(input)) {
            System.out.println("Balanced");
        } else {
            System.out.println("Not Balanced");
        }
        sc.close();
    }
}
