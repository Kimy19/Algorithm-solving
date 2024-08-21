package day06;

import java.util.Scanner;

public class 현주가좋아하는제곱근놀이_김예찬 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		int t = sc.nextInt();
		for(int tc = 1; tc<=t; tc++) {
			long n = sc.nextLong();
			long count = 0;
			while(n != 2) {
				if(Math.round(Math.sqrt(n)) == Math.sqrt(n))
				{
					n = (long)Math.sqrt(n);
				}
				else {
					double near = Math.ceil(Math.sqrt(n));
//					System.out.println("near"+near);
					double powNear =  Math.pow(near,2);
//					System.out.println("powNear"+powNear);
					count+= powNear- n;
//					System.out.println(count);
					n = (long) near;
				}
				count++;
			}
			sb.append("#").append(tc).append(" "+count+"\n");
		}
		System.out.println(sb);
	}

}
