package day08;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 최적경로 {
	static int[][] board, dist;
	static int[] route;
	static boolean[] isUsed;
	static int n, ans;
	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		int t = Integer.parseInt(br.readLine());
		for(int tc = 1; tc<=t; tc++) {
			n = Integer.parseInt(br.readLine())+2;
			board = new int[n][2];
			st = new StringTokenizer(br.readLine());
			for(int i =0; i<n; i++) {
				board[i][0] = Integer.parseInt(st.nextToken());
				board[i][1] = Integer.parseInt(st.nextToken());
			}
			
			//모든 정점 거리계산
			dist = new int[n][n];
			for(int i = 0; i<n;i++) {
				for(int j = i+1; j<n;j++) {
					int d = Math.abs(board[i][0]-board[j][0]) + Math.abs(board[i][1]-board[j][1]);
					dist[i][j] = d;
					dist[j][i] = d;
				}
			}
			route = new int[n];
			isUsed = new boolean[n];
			isUsed[0] = true;
			route[0] = 0;
			ans = Integer.MAX_VALUE;
			permutation(1);
			sb.append("#"+tc+" "+ans+"\n");
		}
		System.out.println(sb);
	}
	static void permutation(int cnt) {
		if(cnt == n-1) {
			route[cnt] = 1;
			int sum = 0;
			for(int i = 0; i<n-1; i++) {
				sum+= dist[route[i]][route[i+1]];
			}
			if(sum < ans)
				ans = sum;
			return;
		}
		for(int i = 2; i<n; i++) {
			if(isUsed[i])
				continue;
			isUsed[i] = true;
			route[cnt] = i;
			permutation(cnt+1);
			isUsed[i] = false;
		}
	}

}
