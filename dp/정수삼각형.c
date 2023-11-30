//백준 정수삼각형 https://www.acmicpc.net/problem/1932

#include <stdio.h>

int n;
int map[500][500];
int dp[500][500];

int f_max(int a, int b)
{
	if(a<b)
		return (b);
	else 
		return (a);
}

int main(void)
{
	int index = 0;

	freopen("../input.txt","r",stdin);
	scanf("%d",&n);
	for(int i = 0; i < n; i++)
	{
		for(int j = 0; j<i+1; j++)
			{
				scanf("%d ",&map[i][j]);
			}
	}
	//bottom-up
	dp[0][0] = map[0][0];
	for(int i = 1; i < n; i++)
	{
		for(int j = 0; j<i+1; j++)
			{
				if(j == 0)
				{
					dp[i][j] = dp[i-1][j] + map[i][j];
					continue;
				}

				if(dp[i-1][j-1] < dp[i-1][j])
					dp[i][j] = dp[i-1][j]+ map[i][j];
				else
					dp[i][j] = dp[i-1][j-1]+ map[i][j];
			}
	}
	int max = 0;
	for(int i = 0; i< n; i++)
	{
		if(max < dp[n-1][i])
			max = dp[n-1][i];
	}
	printf("%d",max);

	//top-down
	for(int i = n-2; i>=0; i--)
	{
		for(int j = 0; j<=i; j++)
		{
			map[i][j] += f_max(map[i+1][j],map[i+1][j+1]);
		}
	}
	printf("\n%d",map[0][0]);
	return (0);
}