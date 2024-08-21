package day06;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ÄõµåÆ®¸®_±è¿¹Âù {
	static int n;
	static int[][] board;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		board = new int[n][n];
		for(int i = 0; i<n; i++) {
			String s = br.readLine();
			for(int j = 0; j<n; j++) {
				board[i][j] = s.charAt(j)-'0';
			}
		}
		compress(0,0,n);
		System.out.println(sb);
		
	}
	static void compress(int x, int y,int size) {
		if(size == 1) {
			sb.append(board[x][y]);
			return;
		}
		int cur = board[x][y];
		for(int i = x; i<x+size; i++) {
			for(int j = y; j<y+size; j++) {
				if(cur != board[i][j]) {
					sb.append("(");
					compress(x, y, size/2);
					compress(x,y+size/2,size/2);
					compress(x+size/2,y,size/2);
					compress(x+size/2,y+size/2,size/2);
					sb.append(")");
					return;
				}
			}
		}
		sb.append(cur);
	}

}
