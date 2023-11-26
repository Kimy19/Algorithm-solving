// 문제링크 https://school.programmers.co.kr/learn/courses/30/lessons/250136
#include <stdio.h>
#include <stdlib.h>

int dx[]={0,0,1,-1};
int dy[]={1,-1,0,0};
int visit[500][500] ={0,};
int max[500] ={0,};
int range[2]={500,-1};

int find_chunk(int **land, int x,int y,size_t land_rows, size_t land_cols)
{
    int count = 1;
    if(x<0 || x >= land_cols || y < 0 || y >= land_rows || visit[x][y] == 1)
        return (0);
    visit[x][y] = 1;
    if(land[y][x] != 1)
        return (0);
    //석유의 x좌표 범위 업데이트
    if(x<range[0])
        range[0] = x;
    if(x>range[1])
        range[1] = x;
    for (int i = 0; i<4; i++)
    {
        count +=find_chunk(land,x+dx[i],y+dy[i],land_rows,land_cols);
    }
    return count;
}

// land_rows는 2차원 배열 land의 행 길이, land_cols는 2차원 배열 land의 열 길이입니다.
int solution(int** land, size_t land_rows, size_t land_cols) {
    int answer = 0;
    int temp;
    
    for(int j = 0; j<land_rows;j++)
    {
        for(int i = 0; i<land_cols; i++)
        {
            range[0] = 500;
            range[1] = -1;
            temp =find_chunk(land,i,j,land_rows,land_cols);

            if(temp)
            {
                for(int k = range[0]; k<=range[1]; k++)
                    max[k] += temp;
                // printf("%d\n",temp);
            }

        }
    }
    for(int i = 0; i<land_cols; i++)
    {
        // printf("%d ",max[i]);
        if(max[i] > answer)
            answer = max[i];
    }
    // printf("\n%d",answer);
    return answer;
}
