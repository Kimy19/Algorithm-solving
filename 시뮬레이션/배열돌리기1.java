package day05;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 배열돌리기1 {
	static int[][] board;
	static int[] dx = {1,0,-1,0};
	static int[] dy = {0,1,0,-1};
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int r = Integer.parseInt(st.nextToken());
		board = new int[n][m];
		for(int i = 0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j<m; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		int k = Math.min(n, m);
		int [][] num = new int[k/2][];
		for(int i = 0; i<k/2; i++) {
			num[i] = new int[(n+m-4*(i+1)) * 2 + 4];
		}
		
		//board의 값 1차원 배열에 저장
		boolean [][] visited = new boolean[n][m];
		for(int i = 0; i<k/2; i++) {
			int x = i;
			int y = i;
			int idx = 0;
			int dir = 0;
			visited[x][y] = true;
			num[i][idx++] = board[x][y];
			while(!(x==i && y==i+1)) {
				int tx = x+dx[dir];
				int ty = y+dy[dir];
				if(tx<0 || tx>=n || ty<0|| ty>=m || visited[tx][ty]) {
					dir++;
					continue;
				}
				visited[tx][ty] = true;
				num[i][idx++] = board[tx][ty];
				x = tx;
				y = ty;
			}
		}

		//1차원 배열 r만큼 index이동
		int[][] new_num = new int[k/2][];
		for(int i = 0; i<k/2;i++) {
			new_num[i] = new int[num[i].length];
			for(int j = 0; j<num[i].length;j++) {
				int index = (j+r) % num[i].length;
				new_num[i][index] = num[i][j];
			}
		}	
		
		//다시 board에 저장
		visited = new boolean[n][m];
		for(int i = 0; i<k/2; i++) {
			int x = i;
			int y = i;
			int idx = 0;
			int dir = 0;
			visited[x][y] = true;
			board[x][y] = new_num[i][idx++];
			while(!(x==i && y==i+1)) {
				int tx = x+dx[dir];
				int ty = y+dy[dir];
				if(tx<0 || tx>=n || ty<0|| ty>=m || visited[tx][ty]) {
					dir++;
					continue;
				}
				visited[tx][ty] = true;
				board[tx][ty] = new_num[i][idx++];
				x = tx;
				y = ty;
			}
		}
		
		//결과 출력
		for(int i =0; i<n; i++) {
			for(int j = 0; j<m; j++) {
				sb.append(board[i][j]+" ");
			}
			sb.append("\n");
		}
		System.out.println(sb);		
	}

}
