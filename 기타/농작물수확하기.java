package day05;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 농작물수확하기 {

	static int n;
	static int ans;
	static int [][] board;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		StringTokenizer st;
		for(int tc = 1; tc<=t; tc++) {
			n = Integer.parseInt(br.readLine());
			board = new int[n][n];
			ans = 0;
			for(int i = 0; i<n; i++) {
				String s = br.readLine();
				for(int j = 0; j<n; j++) {
					board[i][j] = s.charAt(j) - '0';
				}
			}
			for(int i = 0; i<n; i++) {
				for(int j = Math.abs(n/2-i); j<=n-1- Math.abs(i-n/2); j++) {
					ans += board[i][j];
				}
			}
			sb.append("#").append(tc).append(" "+ans+"\n");
		}
		System.out.println(sb);
	}

}
