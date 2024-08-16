package day03;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 암호생성기 {
	static int[] num = new int[8];
	static int subValue;
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int front = 0;
		int min_cycle = Integer.MAX_VALUE;
		for(int tc = 1; tc<=10; tc++) {
			br.readLine();
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int i = 0; i<8; i++) {
				num[i] = Integer.parseInt(st.nextToken());
				min_cycle = Math.min(num[i]/15, min_cycle);
			}
			for(int i = 0; i<8; i++) {
				num[i] -= ((min_cycle-1) * 15);
			}
			subValue = 1;
			front = 0;
			while(true) {
				int flag = 0;
				for(int i = 0; i<8; i++) {
					front = (front+1) % 8;
					num[i] -= subValue;
					if(num[i]<=0) {
						num[i] = 0;
						flag = 1;
						break;
					}
					subValue++;
					if(subValue == 6)
						subValue = 1;
				}
				if(flag==1)
					break;
			}
			sb.append("#"+tc+" ");
			for(int i = 0; i<8; i++) {
				sb.append(num[(front+i)%8]+" ");
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}

}
