package day05;

import java.util.Scanner;

public class º≥≈¡πË¥ﬁ {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int ans = Integer.MAX_VALUE;
		for(int i = 0; i<=n/5; i++) {
			if((n - i*5) %3 == 0)
				ans = Math.min(ans, i+ (n - i*5)/3 );
		}
		if(ans== Integer.MAX_VALUE)
			System.out.println(-1);
		else
			System.out.println(ans);
	}

}
