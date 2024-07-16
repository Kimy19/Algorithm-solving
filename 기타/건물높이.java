
import java.util.Scanner;

public class Main{
public static void main(String[] args) throws Exception{
	// 코드를 작성해주세요.
	int[] dx = {-1,-1,-1,0,0,1,1,1};
	int[] dy = {-1,0,1,-1,1,-1,0,1};
	
	
	Scanner sc = new Scanner(System.in);
	
	System.out.print("숫자를 입력하세요 : ");
	int t = sc.nextInt();
	sc.nextLine();
	
	for(int i = 0; i < t; i++) {
		int n = sc.nextInt();
		sc.nextLine(); // 추가: 남아 있는 공백 라인 소비
		
		char[][] board = new char[n][n];
		
		for (int j = 0; j < n; j++) {
			String line = sc.nextLine();
			board[j] = line.replace(" ", "").toCharArray();
		}
		
		int ans = 0;
		for(int r = 0; r < n; r++) {
			for(int c = 0; c < n; c++) {
				if (board[r][c] == 'G')
					continue;
				boolean nearGreen = false;
				int count = 0;
				for(int dir = 0; dir < 8; dir++) {
					int tx = r + dx[dir];
					int ty = c + dy[dir];
					if (tx < 0 || tx >= n || ty < 0 || ty >= n)
						continue;
					if (board[tx][ty] == 'G') {
						nearGreen = true;
						break;
					}
				}
				if (nearGreen) {
					ans = Math.max(ans,2) ;
				} 
				else {
					for(int k = 0; k<n; k++) {
						if(k==r)
							continue;
						if(board[k][c] == 'B')
							count++;
					}
					for(int k = 0; k<n; k++) {
						if(k==c)
							continue;
						if(board[r][k] == 'B')
							count++;
					}
					ans = Math.max(ans, count+1);
				}
			}
		}
		System.out.printf("#%d %d\n", i + 1, ans); 
	
	sc.close();
}
}
