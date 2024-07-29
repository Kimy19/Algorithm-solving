package src.이분탐색;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 숫자카드2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] list = new int[n];
        for (int i = 0; i < n; i++) {
            list[i] = Integer.parseInt(st.nextToken());
        }
        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        int[] nums = new int[m];
        for (int i = 0; i < m; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(list);
        StringBuilder sb = new StringBuilder();
        List<Integer> ans = new ArrayList<>();
        for(int i=0; i<m; i++){
            int left_index = bisect_left(list,nums[i]);
            int right_index = bisect_right(list,nums[i]);

            sb.append(right_index-left_index).append(" ");
        }
        System.out.println(sb);
    }

    static int bisect_left(int[] list, int num){
        int s = 0;
        int e = list.length;
        while(s<e){
            int mid = (s+e)/2;
            if (list[mid] < num){
                s = mid+1;
            }
            else{
                e = mid;
            }
        }
        return s;
    }

    static int bisect_right(int[] list, int num){
        int s = 0;
        int e = list.length;
        while (s<e){
            int mid = (s+e) / 2;
            if (list[mid] <= num){
                s = mid+1;
            }else{
                e = mid;
            }
        }
        return s;
    }
}
