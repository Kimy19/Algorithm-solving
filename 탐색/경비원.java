package src.기타;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 경비원 {
    static int[][] board;
    static int[] dx = {0,1,0,-1};
    static int[] dy = {1,0,-1,0};
    static int dir = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int c = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(br.readLine());
        board = new int[r+1][c+1];
        for(int i= 0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            int d = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());
            if(d == 1)
                board[0][j] = 1;
            else if(d==2)
                board[r][j] = 1;
            else if(d==3)
                board[j][0] = 1;
            else if(d==4)
                board[j][c] = 1;
        }
        st = new StringTokenizer(br.readLine());
        int d = Integer.parseInt(st.nextToken());
        int j = Integer.parseInt(st.nextToken());
        int[] start = new int[2];
        if(d == 1) {
            board[0][j] = -1;
            start[0] = 0;
            start[1] = j;
            dir = 0;
        }
        else if(d==2){
            board[r][j] = -1;
            start[0] = r;
            start[1] = j;
            dir = 2;
        }
        else if(d==3) {
            board[j][0] = -1;
            start[0] = j;
            start[1] = 0;
            dir = 3;
        }
        else if(d==4) {
            board[j][c] = -1;
            start[0] = j;
            start[1] = c;
            dir = 1;
        }
        int ans = 0;
        int count = 0;
        int x = start[0];
        int y = start[1];
        while(count < 2*(r+c)){
            int tx = x+dx[dir];
            int ty = y+dy[dir];
            if(tx<0 ||tx>r ||ty<0 ||ty>c){
                dir = (dir+1)%4;
                continue;
            }
            count++;
            x = tx;
            y = ty;
            if(board[x][y] == 1){
                ans+= Math.min(count, 2 * (r + c) - count);
//                System.out.println("ans"+ans+" count"+count);
            }
        }
        System.out.println(ans);
    }
}
