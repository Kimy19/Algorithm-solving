//baekjoon 1926
package src;

import java.util.*;

public class Main {
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,1,-1};
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] board = new int[n][m];
        int[][] visit = new int[n][m];

        for(int i = 0; i<n;i++){
            for(int j = 0; j<m;j++){
                board[i][j] = sc.nextInt();
            }
        }
        int count = 0;
        List<Integer> sizeList = new ArrayList<>();
        sizeList.add(0);

        for(int r = 0; r < n; r++){
            for(int c = 0; c<m; c++){
                if(visit[r][c] == 1)
                    continue;
                visit[r][c] = 1;
                if(board[r][c]!= 1)
                    continue;
                Queue<int[]> q= new LinkedList<>();
                q.offer(new int[]{r,c});
                count++;
                int size = 1;
                while(!q.isEmpty()){
                    int[] cur = q.poll();
                    for(int i = 0; i<4; i++){
                        int x = cur[0] + dx[i];
                        int y = cur[1] + dy[i];
                        if(x<0 || x>=n || y<0 || y>=m)
                            continue;
                        if(visit[x][y] == 1 || board[x][y]!= 1)
                            continue;
                        visit[x][y] = 1;
                        q.offer(new int[]{x,y});
                        size++;
                    }
                }
                sizeList.add(size);
            }

        }
        System.out.println(count);
        System.out.println(Collections.max(sizeList));

    }
}