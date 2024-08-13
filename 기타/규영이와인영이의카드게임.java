package basic.algo;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 규영이와인영이의카드게임 {

	static boolean[] isUsed = new boolean[19];
	static int[] card1 = new int[9];//주어진 규영이 카드
	static int[] card2 = new int[9];//인영이 카드
	static int winCnt;
	static int loseCnt;
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int t = Integer.parseInt(br.readLine());
		//파싱
		for(int tc = 0; tc<t; tc++) {
			st = new StringTokenizer(br.readLine());
			isUsed = new boolean[19];
			winCnt = 0;
			loseCnt = 0;
			for(int j = 0; j<9; j++) {
				card1[j] = Integer.parseInt(st.nextToken());
				isUsed[card1[j]] = true;
			}
			permutation(0);		
			System.out.printf("#%d %d %d\n",tc+1, winCnt, loseCnt);
		}	
	}
	
	static void permutation(int cnt) {
		if(cnt == 9) {
			checkResult();
//			System.out.println(Arrays.toString(card2));
			return;
		}
		for(int i = 1; i<19; i++) {
			if(isUsed[i])
				continue;
			isUsed[i] = true;
			card2[cnt] = i;
			permutation(cnt+1);
			isUsed[i] = false;
		}
	}
	
	static void checkResult() {
		int [] score = new int[2];
		
		for(int i = 0; i<9; i++) {
			if(card1[i] < card2[i])
				score[1] += card1[i] + card2[i];
			else if(card1[i] > card2[i])
				score[0] += card1[i] + card2[i];
		}
		if(score[0]>score[1])
			winCnt++;
		else
			loseCnt++;

	}

}
