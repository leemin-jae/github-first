package test;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class B_2675 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int a = Integer.parseInt(br.readLine().trim());
		
		for(int p = 0 ; p < a; p++) {
			String [] array  = br.readLine().split(" ");
			int r = Integer.parseInt(array[0]);
			for(int i = 0 ; i < array[1].length(); i++) {
				for(int j =0; j <r ; j++) {
					bw.write(array[1].charAt(i));
				}
			}
			bw.write("\n");
		}
		
		bw.flush();
		bw.close();
	}

}
