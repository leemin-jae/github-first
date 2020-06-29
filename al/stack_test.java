import java.util.Stack;

public class stack_test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Stack stack = new Stack();
		stack.push(7);
		stack.push(5);
		stack.push(4);
		stack.pop();
		stack.push(6);
		
		while(!stack.empty()) {
			System.out.print(stack.peek() + " ");
			stack.pop();
		}
		
		
		

	}

}
