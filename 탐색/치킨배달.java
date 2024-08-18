package src.완전탐색;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class 치킨배달 {
    static int n,m;
    static int[] numbers;
    static int ans = Integer.MAX_VALUE;
    static ArrayList<int[]> store = new ArrayList<>();
    static ArrayList<int[]> house = new ArrayList<>();

    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        numbers = new int[m];
        for(int i = 0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j<n; j++) {
                int temp = Integer.parseInt(st.nextToken());
                if(temp ==2)
                    store.add(new int[]{i,j});
                else if(temp == 1)
                    house.add(new int[]{i,j});
            }
        }
        combination(0,0);
        System.out.println(ans);
    }

    static void combination(int cnt, int start){
        if(cnt == m){
            int dist = 0;
            for(int i = 0; i<house.size(); i++){
                int min_dist = Integer.MAX_VALUE;
                for(int j = 0; j<numbers.length; j++){
                    int temp = Math.abs(store.get(numbers[j])[0] - house.get(i)[0])
                            +Math.abs(store.get(numbers[j])[1] - house.get(i)[1]);
                    min_dist = Math.min(min_dist,temp);
                }
                dist += min_dist;
            }
            ans = Math.min(ans,dist);
            return;
        }
        for(int i= start; i<store.size();i++){
            numbers[cnt] = i;
            combination(cnt+1,i+1);
        }
    }
}
