#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* solution(const char* number, int k) {
    int len = strlen(number);
	int size = len - k;
	char *answer = (char *)malloc(sizeof(char) * (size + 1));

	for (int i = 0; i< len ; i++)
	{
		answer[i] = number[i];
	}
	
	for(int i = 0; i<k; i++)
	{
	//제거할 부분 찾기
		int j = 0;
		for(j = 0; j<len -1; j++)
		{
			if(answer[j]<answer[j+1])
				break;
		}
		
	//문자열 옮기기
		while(j<len)
			{
				answer[j] = answer[j+1];
				j++;
			}
        answer[j] = '\0';
		len--;

	}
    return answer;
}
