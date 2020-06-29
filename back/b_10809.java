package test;

import java.util.Scanner;

public class b_10809 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		
		int a[] = new int[26];
		for(int i = 0 ; i< a.length;i++) {
			a[i] = -1;
		}
		String k = scan.next();
		for(int i = 0; i < k.length(); i++) {
			char ch = k.charAt(i);
			int ch2 = ch;
			int ch3 = ch-97;
			if(a[ch3] == -1)
				a[ch3] = i;
		}
		for(int i =0; i< a.length;i++) {
			System.out.print(a[i] +" ");
		}
	}

}
