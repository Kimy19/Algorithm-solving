package day06;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Z_김예찬 {
	static int n,r,c;
	static int[][] board;
	static long count = 0, flag = 0;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		int size = (int)Math.pow(2, n);
		moveZ(r,c,size);
		if(count != 0)
			count--;
		System.out.println(count);
		
	}
	static void moveZ(int x, int y,int size) {
		if(size == 1) {
			count++;
			return;
		}
		//왼쪽위
		if(x<size/2 && y<size/2)
			moveZ(x,y,size/2);
		//오른쪽위
		else if(x<size/2 && y>=size/2) {
			count += size/2 * size/2;
			moveZ(x,y-size/2,size/2);
		}
		//왼쪽아래
		else if(x>=size/2 && y<size/2) {
			count += size/2 * size/2 *2;
			moveZ(x-size/2,y,size/2);
		}
		//오른쪽아래
		else if(x>=size/2 && y>=size/2) {
			count += size/2 * size/2 * 3;
			moveZ(x-size/2,y-size/2,size/2);
		}
	}
}

