package src;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 미로탐색 {
    public static void main(String args[]) throws IOException{
        int[] dx = {1,-1,0,0};
        int[] dy = {0,0,1,-1};

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int [][] board = new int[n][m];
        int [][] visit = new int[n][m];
        for(int i = 0; i<n; i++){
            String line = br.readLine();
            for(int j = 0; j<m; j++){
                board[i][j] = line.charAt(j) - '0';
            }
        }
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0,0});
        visit[0][0] = 1;
        while(!q.isEmpty()){
            int[] cur = q.remove();
            for(int i = 0; i<4; i++){
                int x = cur[0] + dx[i];
                int y = cur[1] + dy[i];
                if(x<0 || x>=n || y<0|| y>=m)
                    continue;
                if(visit[x][y]!= 0 || board[x][y] != 1)
                    continue;
                q.add(new int[]{x,y});
                visit[x][y] = visit[cur[0]][cur[1]]+1;
            }
        }
        System.out.println(visit[n-1][m-1]);

    }
}
