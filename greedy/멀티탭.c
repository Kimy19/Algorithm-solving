//백준 멀티텝 스케쥴링 https://www.acmicpc.net/problem/1700

#include <stdio.h>

int n,k;
int schedule[101];
int plug[101]= {0,};
int now = 0;

int find_last(int index)
{
    int out_index = -1;
    int max = 0;

    for(int i =1; i<=k;i++)
    {
        if(!plug[i])
            continue;
        for(int j = index; j<k; j++)
        {
            if(schedule[j] == i)
            {
                // printf("!! i:%d schedulr[j]:%d\n",i,schedule[j]);

                if(max < j)
                {
                    max = j;
                    out_index = i;
                }
                break;
            }
            if(j == k-1)
            {
                out_index = i;
                // printf("here %d",out_index);
                return (out_index);
            }
        }
    }
    return (out_index);
}

int main()
{
    int count = 0;

	freopen("input.txt","r",stdin);
    scanf("%d %d",&n,&k);
    for(int i = 0; i<k; i++)
    {
        scanf("%d ",&schedule[i]);
    }

    for (int i = 0; i<k; i++)
    {
        if(plug[schedule[i]])
            continue;
        else if(now < n && !plug[schedule[i]])
        {
            plug[schedule[i]] = 1;
            now++;
            continue;
        }
        // printf("i %d schedule[i]: %d \n",i,schedule[i]);
        
        int out_index = find_last(i);
        // printf("out %d \n",out_index);
        plug[out_index] =0;
        plug[schedule[i]] = 1;
        count++;
    }
    printf("%d",count);
}