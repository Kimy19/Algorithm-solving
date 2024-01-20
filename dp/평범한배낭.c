//백준 https://www.acmicpc.net/problem/12865
//2차원 배열 dp

#include <stdio.h>

int n;
int k;
int w[101];
int v[101];
int dp[100001][101] = {0,};

int main()
{
    int max = 0;

    freopen("../input.txt","r",stdin);
    scanf("%d %d",&n, &k);

    for(int i = 1; i<=n; i++)
    {
        scanf("%d %d",&w[i],&v[i]);
    }
    for(int i = 1; i<=k; i++)
    {
        for (int j = 1; j<=n;j++)
        {
        
            if(i-w[j] >= 0 && dp[i][j-1] < dp[i-w[j]][j-1] + v[j])
                dp[i][j] = dp[i-w[j]][j-1] + v[j];
            else
                dp[i][j] = dp[i][j-1];            
            if(dp[i][j] >max){
                max = dp[i][j];}
        }
    }
    printf("%d",max);
}