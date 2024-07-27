import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 숨바꼭질 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        // Time array initialization
        int[] time = new int[200000];
        for (int i = 0; i < 200000; i++) {
            time[i] = -1;
        }

        // BFS setup
        Queue<Integer> q = new LinkedList<>();
        q.add(n);
        time[n] = 0;

        if (n == k) {
            System.out.println(0);
            return;
        }

        while (!q.isEmpty()) {
            int cur = q.poll();
            for (int i = 0; i < 3; i++) {
                int x;
                if (i == 0) {
                    x = cur + 1;
                } else if (i == 1) {
                    x = cur - 1;
                } else {
                    x = cur * 2;
                }

                if (x == k) {
                    System.out.println(time[cur] + 1);
                    return;
                }

                if (x < 0 || x >= 200000 || time[x] != -1) {
                    continue;
                }

                time[x] = time[cur] + 1;
                q.add(x);
            }
        }
    }
}
