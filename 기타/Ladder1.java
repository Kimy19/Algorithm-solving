package basic.algo;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Ladder1 {
	static int[] dx = {-1, 0, 0};
	static int[] dy = {0, 1, -1};
	static int[][] board;
	static int dir = 0;
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int end = 0;
		for(int tc = 0; tc<10; tc++) {
			int t = Integer.parseInt(br.readLine());
			board = new int[100][100];
			for(int i = 0; i<100; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j = 0; j<100; j++) {
					board[i][j] = Integer.parseInt(st.nextToken());
					if(board[i][j] == 2)
						end = j;
				}
			}
			int x = 98;
			int y = end;
			while(x != 0) {
				//왼쪽 또는 오른쪽으로 가는중
				if(dir != 0) {
					int tx = x+dx[dir];
					int ty = y+dy[dir];
					if(tx<0 || tx>=100 || ty<0 || ty>=100)
					{
						dir = 0;
						x-= 1;
						continue;
					}
					if(board[tx][ty] == 0) {
						dir = 0;
						x-= 1;
						continue;
					}
					x = tx;
					y = ty;
				}
				//위로 가는중
				else if(dir == 0 ) {
					for(int i = 1; i<=2; i++) {
						int tx = x+dx[i];
						int ty = y+dy[i];
						if(tx<0 || tx>=100 || ty<0 || ty>=100)
							continue;
						if(board[tx][ty] == 0)
							continue;
						dir = i;
						x = tx;
						y = ty;
						break;
					}
					if(dir == 0)
						x -= 1;
				}
//				System.out.println(x+" "+y);
			}
			System.out.printf("\n#%d %d\n",tc+1,y);
		}
	}
}
