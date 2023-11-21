/*
비료두개 존재
최근에 준 비료 연속적으로 사용시 성능이 k만큼 감소
화분의 개수 n개일때 최대 성능구하기
*/

#include <stdio.h>
#include <string.h>

int n = 5;
int k = 2;
int f[2][100]={
	{3,5,8,1},
	{7,1,3,5}
};

int greedy()
{
	int n1, n2;
	int flag;
	int max = 0;
	int ans = 0;

	for(int i = 0; i<2; i++)
	{
		ans = f[i][0];
		flag = i;
		for(int j = 1; j< 4; j++)
		{
			n1 = f[0][j];
			n2 = f[1][j];
			if(flag == 0)
				n1 -= k;
			else
				n2 -= k;
			if(n1 < n2)
			{
				flag = 1;
				ans += n2;
			}
			else
			{
				flag = 0;
				ans += n1;
			}
		}
		if(max < ans)
			max = ans;
	}
	return max;	
}


int main(void)
{
	printf("%d",greedy());
	return 0;
}
