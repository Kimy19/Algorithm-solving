package src.bfs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 불 {
    public static void main(String[] args) throws IOException {
        int[] dx  = {1,-1,0,0};
        int[] dy  = {0,0,1,-1};

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        char[][] board = new char[n][m];
        int[][] visit = new int[n][m];
        int[][] fire = new int[n][m];

        Queue<int[]> q = new LinkedList<>();
        Queue<int[]> q_fire = new LinkedList<>();
        for(int i = 0; i<n; i++){
            String line = br.readLine();
            for(int j = 0; j<m;j++){
                board[i][j] = line.charAt(j);
                if(board[i][j] == 'J'){
                    q.add(new int[]{i,j});
                    visit[i][j] = 1;
                } else if (board[i][j] == 'F') {
                    q_fire.add(new int[]{i,j});
                    fire[i][j] = 1;
                }
            }
        }

        while(!q_fire.isEmpty()){
            int[] cur = q_fire.remove();
            for(int i = 0; i<4; i++){
                int x = cur[0] + dx[i];
                int y = cur[1] + dy[i];
                if(x<0 || x>=n || y<0 || y>=m)
                    continue;
                if(fire[x][y]>0 || board[x][y] =='#')
                    continue;
                fire[x][y] = fire[cur[0]][cur[1]] +1;
                q_fire.add(new int[]{x,y});
            }
        }
        while(!q.isEmpty()){
            int[] cur = q.remove();
            for(int i = 0; i<4; i++){
                int x = cur[0] + dx[i];
                int y = cur[1] + dy[i];
                if(x<0 || x>=n || y<0 || y>=m){
                    System.out.println(visit[cur[0]][cur[1]]);
                    return;
                }
                if(visit[x][y]>0 || board[x][y] =='#' || (fire[x][y]>0 &&fire[x][y]<=visit[cur[0]][cur[1]]+1))
                    continue;
                visit[x][y] = visit[cur[0]][cur[1]] +1;
                q.add(new int[]{x,y});
            }
        }
        System.out.println("IMPOSSIBLE");
    }
}
