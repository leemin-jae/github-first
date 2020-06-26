package test;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class B_1157 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String array  = br.readLine().toUpperCase();
		int max = -1;
		char result = '?';
		int num[] = new int[26];
		int a;
		for(int i =0  ; i< array.length() ; i++) {
			a = array.charAt(i);
			num[a-65]++;
			if(max < num[a-65]) {
				max = num[a-65];
				result = (char) a;
			}
			else if(max == num[a-65])
				result = '?';
		}
		bw.write(result);
		
		bw.flush();
		bw.close();
	}

}
