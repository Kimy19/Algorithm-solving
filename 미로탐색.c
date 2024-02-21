#include <stdio.h>
#define MAX 9999999

int map[101][101];
int n,m;
int dx[4]={1,-1,0,0};
int dy[4]={0,0,1,-1};
int visit[101][101]={0,};
int distance = MAX;

int isValid(int x, int y)
{
    if(x <= 0 || x > n || y <= 0 || y > m)
        return (0);
    return (1);
}
	
void dfs(int row, int col,int count)
{
    printf("row:%d col:%d\n",row,col);
    visit[row][col] = 1;
    if(row == n && col == m)
    {
        if(distance > count)
            distance = count;
        printf("%d",count);
        return ;
    }
    for(int i = 0; i<4; i++)
    {
        if(isValid(row+dx[i], col+dy[i]) && !visit[row+dx[i]][col+dy[i]] && map[row+dx[i]][col+dy[i]])
        {
            dfs(row+dx[i], col+dy[i], count+1);
            visit[row+dx[i]][col+dy[i]] = 0;
        }
    }
}

int main()
{
	freopen("input.txt","r",stdin);
    scanf("%d %d",&n,&m);

    for(int i = 1; i<=n; i++)
    {
        for(int j = 1; j<=m; j++)
        {
            scanf("%d",&map[i][j]);
        }
    }
    dfs(1,1,1);
    printf("%d",distance);
}