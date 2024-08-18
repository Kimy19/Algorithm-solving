package src.완전탐색;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class 프로세서연결하기 {
    static int n;
    static int[] dx ={-1,1,0,0};
    static int[] dy ={0,0,1,-1};
    static int[][] board;
    static int ans = Integer.MAX_VALUE;
    static int max_core_size = 0;
    static StringBuilder sb = new StringBuilder();
    static ArrayList<int[]> core = new ArrayList<>();
    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for(int tc = 1; tc<=t; tc++ ){
            n = Integer.parseInt(br.readLine());
            board = new int[n][n];
            core = new ArrayList<>();
            for(int i = 0; i<n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for(int j = 0; j<n; j++){
                    board[i][j] = Integer.parseInt(st.nextToken());
                    if(board[i][j] == 1){
                        if(i == 0 || i == n-1 || j == 0 || j== n-1)
                            continue;
                        core.add(new int[]{i,j});
                    }
                }
            }
            ans = Integer.MAX_VALUE;
            max_core_size = 0;
            permutation(0,0, 0);
            sb.append("#"+tc+" "+ans+"\n");
        }
        System.out.println(sb);
    }
    static void permutation(int cnt, int len, int core_size){
        if(cnt == core.size()){
            if(core_size > max_core_size){
                max_core_size = core_size;
                ans = len;
            }
            else if(core_size == max_core_size)
                ans = Math.min(ans,len);
            return;
        }
        for(int i =0; i<4; i++){
            int x = core.get(cnt)[0];
            int y = core.get(cnt)[1];
            int size = 0;
            int flag = 0;
            while(true){
                x += dx[i];
                y += dy[i];
                if(x<0 || x>=n || y<0 || y>=n){
                    break;
                }
                if(board[x][y] == 1 || board[x][y] == -1){
                    x += dx[i] *-1;
                    y += dy[i] *-1;
                    while(board[x][y] != 1){
                        board[x][y] = 0;
                        x += dx[i] *-1;
                        y += dy[i] *-1;
                    }
                    flag = 1;
                    break;
                }
                board[x][y] = -1;
                size++;
            }
            if(flag ==1)
                permutation(cnt+1,len, core_size);
            else {
                permutation(cnt + 1, len+size, core_size+1);
                x += dx[i] * -1;
                y += dy[i] * -1;
                while (board[x][y] != 1) {
                    board[x][y] = 0;
                    x += dx[i] * -1;
                    y += dy[i] * -1;
                }
            }

        }
    }
}
