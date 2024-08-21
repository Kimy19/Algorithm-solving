package day06;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 보호필름_김예찬 {
	static int d,w,k,ans;
	static int[][] board;
	static boolean[] isSelected, ABSelected;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		StringTokenizer st;
		for(int tc = 1; tc<=t; tc++) {
			st = new StringTokenizer(br.readLine());
			d = Integer.parseInt(st.nextToken());
			w = Integer.parseInt(st.nextToken());
			k = Integer.parseInt(st.nextToken());
			board = new int[d][w];
			isSelected = new boolean[d];
			ans = 0;
			for(int i = 0; i<d; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j = 0; j<w; j++) {
					board[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			if(!checkBoard(board)) {
				for(int i = 1; i<k; i++) {
					combination(0,i,0);
					if(ans != 0)
						break;
				}
				if(ans == 0)
					ans = k;
			}
			
			sb.append("#").append(tc).append(" "+ans+"\n");
		}
		System.out.println(sb);
	}
	
	static void combi_ab(int cnt, int r) {
		if(cnt == r) {
			fillBoard(r);
			return;
		}
		ABSelected[cnt] = true;
		combi_ab(cnt+1, r);
		ABSelected[cnt] = false;
		combi_ab(cnt+1, r);
	}
	static void combination(int cnt,int r, int start) {
		if(ans != 0)
			return;
		if(cnt == r) {
//			System.out.println(r);
			ABSelected = new boolean[r];
			combi_ab(0,r);
			return;
		}
		for(int i = start; i<d; i++) {
			isSelected[i] = true;
			combination(cnt+1, r, i+1);
			isSelected[i] = false;
		}
	}
	static void fillBoard(int r) {
		int [][]board_cp = new int[d][w];
		int index = 0;
		for(int i= 0; i<d;i++) {
			board_cp[i] = board[i].clone();
			if(!isSelected[i]) continue;
			if(ABSelected[index++]) {
				for(int j = 0; j<w;j++) {
					board_cp[i][j] = 1;
				}
			}
			else {
				for(int j = 0; j<w;j++) {
					board_cp[i][j] = 0;
				}
			}
		}
		if(checkBoard(board_cp))
			ans = r;
	}
	static boolean checkBoard(int [][] board) {
		if(k == 1)
			return true;
		for(int i = 0; i<w; i++) {
			int cur = board[0][i];
			int count = 1;
			int flag = 0;
			for(int j = 1; j<d; j++) {
				if(cur != board[j][i]) {
					cur = board[j][i];
					count = 1;
				}
				else {
					cur = board[j][i];
					count++;
					if(count >= k) {
						flag = 1;
						break;
					}
				}
			}
			if(flag != 1)
				return false;
		}
		return true;
	}

}
