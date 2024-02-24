#include <stdio.h>

int n;
int dp[1000];
int num[1000];

int find_max(int index)
{
	int max = 0;
	for(int i = 0; i<index; i++)
	{
		if(num[index]> num[i])
		{
			if(max<dp[i])
				max = dp[i];
		}
	}
	return (max);
}

int main()
{
	int max = 1;
	freopen("../input.txt","r",stdin);

	scanf("%d",&n);
	for(int i = 0; i<n; i++)
		scanf("%d",&num[i]);
	
	dp[0] = 1;
	for(int i = 1; i<n; i++)
	{
		dp[i]=find_max(i)+1;
		if(max<dp[i])
			max = dp[i];

	}
	printf("%d",max);
}