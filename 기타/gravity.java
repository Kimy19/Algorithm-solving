package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Gravity {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[] h = new int[n];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i = 0; i<n;i++) {
			h[i] = Integer.parseInt(st.nextToken());
		}
		int max = 0;
		for(int i = 0; i<n;i++){
			int cur = h[i];
			int count = 0;
			for(int j = i; j<n; j++) {
				if(cur <= h[j]) {
					cur = h[j];
					continue;
				}
				count++;
			}
			if(max<count)
				max = count;
		}
		System.out.println(max);
	}
}
