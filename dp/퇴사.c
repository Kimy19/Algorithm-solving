#include <stdio.h>

int n;
int t[15];
int p[15];
int dp[16] = {0,};
int dp2[16] = {0,};

int max(int a, int b)
{
	if(a>b)
		return (a);
	else 
		return (b);
}

int main(void)
{
	int N;
	freopen("input.txt","r",stdin);
	scanf("%d",&n);

	for (int i = 0; i < n; i++)
	{
		scanf("%d %d",&t[i],&p[i]);
		printf("%d %d\n",t[i],p[i]);
	}

	/*
	DP bottom-up
	*/
	for(int i = 0; i < n; i++)
	{
		for(int j = i + t[i]; j<=n; j++)
		{
			if(dp[j] < dp[i] + p[i])
				dp[j] = dp[i] + p[i];
		}
	}
	printf("%d ",dp[n]);

	/*
	DP top-down
	*/

	for(int i = n-1; i>= 0; i--)
	{
		if (i + t[i] > n)
			dp2[i] = dp2[i + 1];
		else
			dp2[i] = max(dp2[i+1], p[i] + dp2[i + t[i]]);
	}
	printf("\n%d",dp2[0]);
	return (0);
}