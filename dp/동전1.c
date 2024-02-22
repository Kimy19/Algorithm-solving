#include <stdio.h>

int n,k;
int num[101];
int dp[10001]={0,};

int main()
{
	freopen("../input.txt","r",stdin);
	scanf("%d %d",&n,&k);
	for(int i =1; i<=n; i++)
	{
		scanf("%d",&num[i]);
	}
	
	dp[0] = 1;
	for(int i = 1; i<=n; i++)
	{
		for(int j = 1; j<=k; j++)
		{
			if(j-num[i] < 0)
				continue;
			dp[j] += dp[j-num[i]];
		}
	}
	
	printf("%d",dp[k]);
}
