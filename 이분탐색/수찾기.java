package src.이분탐색;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class 수찾기 {
    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        List<Integer> list = new ArrayList<>();
        for(int i= 0; i<n; i++){
            list.add(Integer.parseInt(st.nextToken()));
        }
        Collections.sort(list);
        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        List<Integer> num = new ArrayList<>();
        for(int i= 0; i<m; i++){
            num.add(Integer.parseInt(st.nextToken()));
        }
        for(int i = 0; i<m; i++){
            if(Collections.binarySearch(list,num.get(i))>=0){
                System.out.println("1");
            }else{
                System.out.println("0");
            }
        }

    }
//    public static int bisect(List<Integer> list, int num) {
//        int s = 0;
//        int e = list.size() - 1;
//        while (s <= e) {
//            int mid = (s + e) / 2;
//            if (list.get(mid) < num) {
//                s = mid + 1;
//            } else if (list.get(mid) > num) {
//                e = mid - 1;
//            } else {
//                return 1;
//            }
//        }
//        return 0;
//    }

}
