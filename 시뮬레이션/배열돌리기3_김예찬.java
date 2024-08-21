package day06;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 배열돌리기3_김예찬 {
	static int[][] board,new_board;
	static int n,m,r;
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		board = new int[n][m];
		for(int i = 0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j<m; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		st = new StringTokenizer(br.readLine());
		ArrayList<Integer> type = new ArrayList<>();
		while(st.hasMoreTokens())
			type.add(Integer.parseInt(st.nextToken()));
		
		for(int k = 0; k< type.size(); k++) {
			if(type.get(k) == 1)
				up_down_reverse();
			else if(type.get(k)==2)
				left_right_reverse();
			else if(type.get(k)==3)
				right_turn();
			else if(type.get(k)==4)
				left_turn();
			else if(type.get(k)==5)
				sub_right_turn();
			else if(type.get(k)==6)
				sub_left_turn();
		}
		
		for(int i = 0; i<n; i++) {
			for(int j = 0; j<m;j++)
				sb.append(board[i][j]+" ");
			sb.append("\n");
		}
		System.out.println(sb);
	}
	//1
	static void up_down_reverse() {
		int temp;
		for(int i = 0; i<n/2; i++) {
			for(int j = 0; j<m; j++) {
				temp = board[i][j];
				board[i][j] = board[n-i-1][j];
				board[n-i-1][j] = temp;
			}
		}
	}
	static void left_right_reverse() {
		//2
		int temp;
		for(int i = 0; i<n; i++) {
			for(int j = 0; j<m/2; j++) {
				temp = board[i][j];
				board[i][j] = board[i][m-j-1];
				board[i][m-j-1] = temp;
			}
		}
	}
	static void right_turn() {
		//3
		new_board = new int[m][n];
		for(int i = 0; i<n; i++) {
			for(int j = 0; j<m; j++) {
				new_board[j][n-i-1] = board[i][j];
			}
		}
		board = new_board;
		int temp = n;
		n = m;
		m = temp;
	}
	static void left_turn() {
		//4
		new_board = new int[m][n];
		for(int i = 0; i<n; i++) {
			for(int j = 0; j<m; j++) {
				new_board[m-j-1][i] = board[i][j];
			}
		}
		board = new_board;
		int temp = n;
		n = m;
		m = temp;
	}
	static void sub_right_turn() {
		//5
		new_board = new int[n][m];
		
		int [][] s = {{0,0},{0,m/2},{n/2,m/2},{n/2,0}};
		int [] dx = {0,n/2,0,-n/2};
		int [] dy = {m/2,0,-m/2,0};
		for(int dir = 0; dir<4; dir++) {
			for(int i = s[dir][0]; i<s[dir][0]+ n/2; i++) {
				for(int j = s[dir][1]; j<s[dir][1]+m/2; j++) {
					new_board[i+dx[dir]][j+dy[dir]] = board[i][j];
				}
			}
		}
		board = new_board;
	}
	static void sub_left_turn() {
		//6
		new_board = new int[n][m];
		
		int [][] s = {{0,0},{0,m/2},{n/2,m/2},{n/2,0}};
		int [] dx = {n/2, 0, -n/2, 0,};
		int [] dy = {0, -m/2, 0, m/2};
		for(int dir = 0; dir<4; dir++) {
			for(int i = s[dir][0]; i<s[dir][0]+ n/2; i++) {
				for(int j = s[dir][1]; j<s[dir][1]+m/2; j++) {
					new_board[i+dx[dir]][j+dy[dir]] = board[i][j];
				}
			}
		}
		board = new_board;
	}
}
