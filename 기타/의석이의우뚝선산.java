package day05;

import java.io.IOException;
import java.util.Scanner;
import java.util.StringTokenizer;

public class 의석이의우뚝선산 {

	static int n;
	static int ans;
	static int [] h;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
//		int t = sc.nextInt();
		int t = 1;
		for(int tc = 1; tc<=t; tc++) {
			n = sc.nextInt();
			h = new int[n];
			ans = 0;
			for(int i = 0; i<n; i++)
				h[i] = sc.nextInt();
			
			int up_count=0;
			int down_count=0;
			int prev = h[0];
			int i = 1;
			while(i<n) {
				while(i<n && prev > h[i]) {
					prev = h[i];
					i++;
				}
				while(i<n && prev < h[i]) {
					prev = h[i];
					up_count++;
					i++;
				}
				while(i<n && prev >h[i]) {
					prev = h[i];
					down_count++;
					i++;
				}
				System.out.println(up_count+" "+down_count);
				ans += up_count*down_count;
				up_count = 0;
				down_count = 0;
			}
			sb.append("#").append(tc).append(" "+ans+"\n");
		}
		System.out.println(sb);
	}

}
