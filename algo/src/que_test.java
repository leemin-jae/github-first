import java.util.LinkedList;
import java.util.Queue;

public class que_test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Queue q = new LinkedList();
		q.offer(1);
		q.offer(2);
		q.poll();
		q.offer(3);
		
		while(!q.isEmpty()) {
			System.out.println(q.peek());
			q.poll();
		}
	}

}
