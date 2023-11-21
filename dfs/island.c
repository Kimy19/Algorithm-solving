//dfs 알고리즘
//섬의 개수와 크기 구하기

#include <stdio.h>
#include <string.h>

int visit[5][5] ={0,};
int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,1,-1};

int map[5][5] = {
	{1, 0, 0, 1, 1},
	{1, 1, 1, 1, 0},
	{0, 0, 0, 1, 0},
	{1, 1, 1, 0, 0},
	{0, 0, 1, 1, 0}
};

int	dfs(int x, int y)
{
	int size = 1;

	if(x < 0 || x >= 5 || y < 0 || y >= 5 || map[x][y] == 0 || visit[x][y] == 1)
		return (0);
	visit[x][y] = 1;
	for (int i = 0; i < 4; i++)
	{
		size += dfs(x + dx[i], y + dy[i]);
	}
	return (size);
}


int cmp(int *a,int *b)
{
	if (*(int*)a < *(int*)b)
		return -1;
	else if (*(int*)a > *(int*)b)
		return 1;
	return 0;
}

int main(void)
{
	int count = 0;
	int temp;
	int	size[25];

	memset(size, -1, sizeof(int) * 25);

	freopen("../input.txt","r",stdin);

	for (int i = 0; i < 5; i++)
	{
		for (int j = 0; j < 5; j++)
		{
			temp = dfs(i, j);
			if (temp > 0)
				size[count++] = temp;
		}
	}
	int i = 0;
	while(i<25)
	{
		if(size[i] != -1)
			printf("group%d size%d\n",i+1,size[i]);
		i++;
	}
	qsort(size, count, sizeof(int), cmp);
	i = 0;
	while(i<count)
	{
		printf("group%d size%d\n",i+1,size[i]);
		i++;
	}

}