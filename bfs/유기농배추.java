import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException{
        // TODO Auto-generated method stub
        int[] dx = {1,-1,0,0};
        int[] dy = {0,0,1,-1};
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for(int l = 0; l<t; l++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m =  Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            int[][] board = new int[n][m];
            List<int[]> start = new ArrayList<>();
            for(int i = 0; i<k;i++) {
                st = new StringTokenizer(br.readLine());
                int r = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());
                board[r][c] = 1;
                start.add(new int[] {r,c});
            }
            Queue<int[]> q = new LinkedList<>();
            int[][] visit = new int[n][m];
            int count = 0;
            for(int i=0; i<start.size();i++) {
                int r = start.get(i)[0];
                int c = start.get(i)[1];
                if(visit[r][c] != 0)
                    continue;
                q.add(new int[] {start.get(i)[0],start.get(i)[1]});
                visit[r][c] = 1;
                count++;
                while(!q.isEmpty()) {
                    int[] cur = q.remove();
                    for(int j = 0; j<4; j++) {
                        int x = cur[0] + dx[j];
                        int y = cur[1] + dy[j];
                        if (x<0 || x>=n || y<0 || y>=m)
                            continue;
                        if(visit[x][y] != 0 || board[x][y] != 1)
                            continue;
                        visit[x][y] = 1;
                        q.add(new int[] {x,y});
                    }
                }
            }
            sb.append(count).append('\n');
        }
        System.out.println(sb);
    }

}
