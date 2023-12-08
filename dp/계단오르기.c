//[백준 계단오르기] https://www.acmicpc.net/problem/2579
#include <stdio.h>

int n;
int step[301];
int dp[301];

int max(int a, int b)
{
    return a>b?a:b;
}

int main(void)
{
    //freopen("../input.txt","r",stdin);
    scanf("%d",&n);
    for(int i = 0; i<n; i++)
    {
        scanf("%d", &step[i]);
    }
    dp[0] = step[0];
    dp[1] = step[0]+step[1];
    dp[2] = max(step[0]+step[2],step[1]+step[2]);

    for(int i = 3; i<n; i++)
    {
        dp[i] = max(dp[i-2] + step[i], dp[i-3] + step[i-1] + step[i]);
    }
    printf("%d",dp[n-1]);

    return (0);
}