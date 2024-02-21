//[백준 2775 부녀회장이 될테야] https://www.acmicpc.net/problem/2775


#include <stdio.h>

int t,k,n;
int dp[15][15];

int main()
{
	freopen("../input.txt","r",stdin);
    scanf("%d",&t);

    for(int a=0; a<t; a++)
    {
        scanf("%d",&k);
        scanf("%d",&n);
    
        printf("%d %d\n",k,n);
        for(int i=0; i<15; i++)
            dp[0][i] = i;
        
        for(int i=1; i<=k; i++)
        {
            for(int j=1; j<=n; j++)
            {
                dp[i][j] = dp[i][j-1] + dp[i-1][j];
            }
        }
        printf("%d\n",dp[k][n]);
    }

}