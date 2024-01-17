//백준 2606 :  https://www.acmicpc.net/problem/2606

#include <stdio.h>

int n;
int m;
int map[101][101]={0,};
int visit[101]={0,};


int find(int now)
{
    int count = 1;
    
    visit[now] = 1;
    for(int i = 1; i<=n; i++)
    {
        if(!visit[i] && map[now][i])
        {
            // printf("%d %d\n",now,i);
            count+=find(i);
        }
    }
    return count;
}
int main(void)
{
    freopen("../input.txt","r",stdin);
    scanf("%d",&n);
    scanf("%d",&m);

    for(int i = 0; i<m; i++)
    {
        int j,k;
        scanf("%d %d",&j,&k);
        map[j][k] = 1;
        map[k][j] = 1;
    }
    printf("%d",find(1)-1);

    return (0);
}