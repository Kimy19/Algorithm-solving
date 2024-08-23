package day08;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 상호의배틀필드 {

	static int n,m,x,y,cur_dir;
	static char[] command;
	static char[][] board;
	static int[] dx = {-1,1,0,0};
	static int[] dy = {0,0,-1,1};
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		for(int tc = 1; tc<=t; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
			board = new char[n][m];

			for(int i = 0; i<n; i++) {
				String s = br.readLine();
				board[i] = s.toCharArray();
			}
			int flag = 0;
			for(int i = 0; i<n; i++) {
				for(int j = 0; j<m; j++) {
					if(board[i][j] == '^') {
						cur_dir = 0; 
						flag = 1;
					}
					else if(board[i][j] == 'v') {
						cur_dir = 1; 
						flag = 1;
					}
					else if(board[i][j] == '<') {
						cur_dir = 2; 
						flag = 1;
					}
					else if(board[i][j] == '>') {
						cur_dir = 3; 
						flag = 1;
					}
					if(flag == 1) {
						x = i;
						y = j;
						board[i][j] = '.';
						break;
					}
				}
				if(flag== 1)
					break;
			}
			br.readLine();
			command = br.readLine().toCharArray();
			for(int i =0; i<command.length; i++) {
				if(command[i] == 'U') {
					move(0);
				}
				else if(command[i] == 'D') {
					move(1);
				}
				else if(command[i] == 'L') {
					move(2);
				}
				else if(command[i] == 'R') {
					move(3);
				}
				else if(command[i] == 'S') {
					shoot();
				}
				
			}
			if(cur_dir == 0)
				board[x][y] = '^';
			else if(cur_dir == 1)
				board[x][y] = 'v';
			else if(cur_dir == 2)
				board[x][y] = '<';
			else if(cur_dir == 3)
				board[x][y] = '>';
			sb.append("#"+tc+" ");
			for(int i = 0; i<n;i++) {
				for(int j = 0; j<m;j++) {
					sb.append(board[i][j]);
				}
				sb.append("\n");
			}
		}
		System.out.println(sb);
	}
	static void move(int dir){
		cur_dir = dir;
		int tx = x+dx[dir];
		int ty = y+dy[dir];
		if(tx<0 || tx>=n || ty<0 || ty>=m)
			return;
		if(board[tx][ty]!='.')
			return;
		x = tx;
		y = ty;
	}
	static void shoot() {
		int tx = x;
		int ty = y;
		while(true) {
			tx += dx[cur_dir];
			ty += dy[cur_dir];
			if(tx<0 || tx>=n || ty<0 || ty>=m || board[tx][ty]=='#')
				return;
			if(board[tx][ty]=='*') {
				board[tx][ty] = '.';
				return;
			}
		}
	}
}
