//softeer[HSAT 7회 정기 코딩 인증평가 기출] https://softeer.ai/practice/6246
#include <stdio.h>

int n,m;
int map[4][4];
int p[16][2];
int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};
int visit[4][4];


int find(int x, int y, int count)
{
	int num = 0;

	if (x < 0 || x >= n|| y < 0 || y >= n || map[x][y] || visit[x][y])
		return (0);

	visit[x][y] = 1;
	if(x == p[count][0] && y == p[count][1])
		count++;
	if(count == m)
	{
		visit[x][y] = 0;
		return (1);
	}

	for (int i = 0; i < 4; i++)
	{
		num += find(x+dx[i],y+dy[i],count);
	}
	visit[x][y] = 0;
	return (num);

}

int main(void)
{
	freopen("input.txt","r",stdin);
	scanf("%d %d",&n,&m);
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			scanf("%d ",&map[i][j]);
		}
	}
	for (int i = 0; i < m; i++)
	{
		int temp1, temp2;
		scanf("%d %d", &temp1, &temp2);
		p[i][0] = temp1 - 1;
		p[i][1] = temp2 - 1;
	}

	printf("%d",find(p[0][0],p[0][1],0));

	return (0);
}