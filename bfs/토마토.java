package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Tomato {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		int[] dx = {1,-1,0,0};
		int[] dy = {0,0,1,-1};
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int m = Integer.parseInt(st.nextToken()); 
		int n = Integer.parseInt(st.nextToken()); 
		
		int[][] board = new int[n][m];
		int[][] visit = new int[n][m];
		
		Queue<int[]> q = new LinkedList<>(); 
		for(int i = 0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j<m; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
				if(board[i][j] == 1) {
					q.add(new int[] {i,j});
					visit[i][j] = 1;
				}
			}
		}
		while(!q.isEmpty()) {
			int[] cur = q.remove();
			for(int i = 0; i<4; i++) {
				int x = cur[0] + dx[i];
				int y = cur[1] + dy[i];
				
				if(x<0 || x>=n || y<0 || y>=m)
					continue;
				if(board[x][y] != 0 || visit[x][y] > 0)
					continue;
				visit[x][y] = visit[cur[0]][cur[1]] + 1;
				q.add(new int[] {x,y});
			}
		}
		int max = visit[0][0]-1;
		for(int i = 0; i<n; i++) {
			for(int j =0; j<m; j++) {
				if(max<visit[i][j])
					max = visit[i][j] - 1;
				if(visit[i][j] == 0 && board[i][j] == 0) {
					max = -1;
					break;
				}
			}
			if(max==-1)
				break;
		}
		System.out.println(max);
	}

}
