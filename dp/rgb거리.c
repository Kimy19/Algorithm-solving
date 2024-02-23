//[백준 1149 rgb거리] https://www.acmicpc.net/problem/2293

#include <stdio.h>

int n;
int color[1000][3];
int dp[1000][3];

int getmin(int i, int j)
{
	int flag=0;
	int min;
	for(int k =0; k<3; k++)
	{
		if(k != j)
		{
			if(!flag)
			{	
				min = dp[i][k];
				flag = 1;
			}
			else
			{ 
				if(dp[i][k] < min)
					min = dp[i][k];
			}
		}
	}
	return (min);
}

int main()
{
	freopen("../input.txt","r",stdin);

	scanf("%d",&n);
	for(int i = 0; i<n; i++)
	{
		scanf("%d %d %d",&color[i][0],&color[i][1],&color[i][2]);
	}

	for(int i = 0; i<3; i++)
		dp[0][i] = color[0][i];

	for(int i = 1; i<n; i++)
	{
		for(int j = 0; j<3; j++)
		{
			int min = getmin(i-1,j);
			dp[i][j] = min + color[i][j];
		}
	}

	int min;
	for(int i =0; i<3; i++)
	{
		if(i == 0)
			min = dp[n-1][i];
		else if(dp[n-1][i] < min)
			min = dp[n-1][i];
	}
	printf("%d",min);
}