//baekjoon 10808
package src;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int[] count = new int[26];
        int[] count = new int['z'-'a'+1];
        for(int i=0; i<s.length(); i++){
            count[s.charAt(i)-'a']++;
        }
        for(int i= 0; i<26; i++){
            System.out.print(count[i]+" ");
        }
    }
}