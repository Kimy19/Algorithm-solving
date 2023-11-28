//프로그래머스 <큰 수 만들기> https://school.programmers.co.kr/learn/courses/30/lessons/42883
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* solution(const char* number, int k) {
    int len = strlen(number);
    int remain = len - k;

    char* answer = (char*)malloc(remain + 1);
    int top = -1;

    for (int i = 0; i < len; i++) {
        while (top != -1 && number[i] > answer[top] && k > 0) {
            // 현재 숫자가 스택의 top에 있는 숫자보다 크면서 아직 제거 가능한 횟수가 남아있으면
            // 스택의 top에 있는 숫자를 제거
            top--;
            k--;
        }

        // 현재 숫자를 스택에 추가
        answer[++top] = number[i];
    }

    // remain만큼의 길이로 answer 문자열 생성
    answer[remain] = '\0';

    return answer;
}
