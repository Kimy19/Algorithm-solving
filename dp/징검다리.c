#include <stdio.h>

int n;
int h[3001];
int dp[3001];

int main()
{
    freopen("../input.txt","r",stdin);

    scanf("%d",&n);
    for(int i = 0; i<n; i++)
    {
        dp[i] = 1; 
        scanf("%d",&h[i]);
    }
    
    for(int i = 0; i<n-1; i++)
    {
        for(int j = i+1; j<n;j++)
        {
            if(h[i]<h[j])
                dp[j] = dp[j]+1 < dp[i] ? dp[i]: dp[j]+1;
        }
    }
    int max = 0;
    for(int i = 0; i<n; i++)
        if(max<dp[i])
            max = dp[i];
    printf("%d",max);
}