package day03;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 연구소 {
	static int n,m;
	static int ans;
	static int [] numbers = new int[3];
	static int [] dx = {1,-1,0,0};
	static int [] dy = {0,0,1,-1};
	static int [][] board;
	static ArrayList<int[]> virus = new ArrayList<>();
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		board = new int[n][m];
		for(int i = 0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j<m; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
				if(board[i][j] == 2)
					virus.add(new int[] {i,j});
			}
		}
		ans = 0;
		makeWall(0,0);
		System.out.println(ans);
	}
	static void makeWall(int cnt, int start) {
		if(cnt == 3) {
			checkSize();
			return;
		}
		for(int i = start; i<n*m; i++) {
			numbers[cnt] = i;
			makeWall(cnt+1, i+1);
		}
	}
	static void checkSize() {
		int [][] board_cp = board.clone();
		for(int i = 0; i<n; i++)
			board_cp[i] = board[i].clone();
		//벽세우기
		for(int i = 0; i<3; i++) {
			int x = numbers[i] / m;
			int y = numbers[i] % m;
			if(board_cp[x][y] != 0)
				return;
			board_cp[x][y] = 1;
		}
		//bfs
		Queue<int[]> q = new LinkedList<>();
		for(int[] v : virus) {
			q.add(v);
			while(!q.isEmpty()) {
				int [] p = q.poll();
				for(int dir = 0; dir<4; dir++) {
					int tx = p[0] + dx[dir];
					int ty = p[1] + dy[dir];
					if(tx<0 || tx>=n || ty<0 || ty>=m)
						continue;
					if(board_cp[tx][ty] != 0)
						continue;
					board_cp[tx][ty] = 2;
					q.add(new int[] {tx,ty});
				}
			}
		}
		int count = 0;
		for(int i = 0; i<n; i++) {
			for(int j = 0; j<m;j++) {
				if(board_cp[i][j] == 0)
					count++;
			}
		}
		ans = Math.max(ans, count);
	}
}
