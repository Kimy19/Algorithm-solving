//[softeer lv.2] https://softeer.ai/practice/6280
#include <stdio.h>
#include <math.h>

int N;
int dp[15] = {0,};

int main(void)
{
   scanf("%d",&N);

   dp[0] = 2;
   for(int i = 1; i<=N; i++)
       dp[i] = dp[i-1] + (int)pow(2,i-1);

   printf("%d",dp[N] * dp[N]);
  
   return (0);
}