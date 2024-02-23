//

#include <stdio.h>

#define INF 999

int v,e;
int start;
int map[20001][20001];
int dist[20001];
int visited[20001] = {0,};

int get_next_node()
{
	int min_dist = INF;
	int min_idx = start;

	for(int i = 1 ; i<=v; i++)
	{
		if(visited[i])
			continue;
		if(dist[i] < min_dist)
		{
			min_dist = dist[i];
			min_idx = i;
		}
	}
	return (min_idx);
}

//Dijkstra
void find_shortest()
{
	for(int i = 1; i<= v; i++)
		dist[i] = map[start][i];
	dist[start] = 0;
	visited[start] = 1;
	for(int i = 0; i< v-1; i++)
	{
		int new_node = get_next_node();
		visited[new_node] = 1;

		for(int j = 1; j<=v; j++)
		{
			if(visited[j] == 1)
				continue;
			if(dist[j] > dist[new_node] + map[new_node][j])
				dist[j] = dist[new_node] + map[new_node][j];
		}
	}
}

int main(void)
{
	int index = 0;

	freopen("../input.txt","r",stdin);

	scanf("%d %d",&v,&e);
	scanf("%d",&start);
	for(int i = 1; i<=v; i++)
	{
		for(int j = 1; j<=v; j++)
		{
			map[i][j] = (i == j) ? 0 : INF;
		}
	}

	for(int i = 0; i<e; i++)
	{
		int t1,t2,w;
		scanf("%d %d %d", &t1,&t2,&w);
        if (map[t1][t2] > w)
            map[t1][t2] = w;
	}
	find_shortest();
	for(int i = 1; i<=v; i++)
	{
		if(dist[i] == INF)
			printf("INF\n");
		else
			printf("%d\n",dist[i]);
	}
	return (0);
}