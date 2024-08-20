package day05;

import java.io.BufferedReader;
import java.io.IOError;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 장훈이의높은선반 {
	static int n;
	static int ans, b;
	static int [] h;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		StringTokenizer st;
		for(int tc = 1; tc<=t; tc++) {
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			h = new int[n];
			ans = Integer.MAX_VALUE;
			st = new StringTokenizer(br.readLine());
			for(int i = 0; i<n; i++)
				h[i] = Integer.parseInt(st.nextToken());
			for(int i = 1; i<=n;i++)
				combination(0,i,0,0);
			sb.append("#").append(tc).append(" "+ans+"\n");
		}
		System.out.println(sb);
	}
	static void combination(int cnt, int r, int sum, int start) {
		if(cnt == r)
		{
			if(sum>=b)
				ans = Math.min(ans, Math.abs(sum-b));
			return;
		}
		for(int i = start; i<n; i++) {
			combination(cnt+1,r,sum+h[i],i+1);
		}
	}

}
