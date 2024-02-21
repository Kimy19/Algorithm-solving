//[백준 문자열폭발 9935] https://www.acmicpc.net/problem/9935

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char str[1000001];
    char explosion[37]; // 최대 길이 36
    char result[1000001];

    freopen("./input.txt","r",stdin);

    scanf("%s", str);

    // 폭발 문자열 입력
    scanf("%s", explosion);

    int len_str = strlen(str);
    int len_explosion = strlen(explosion);
    int result_index = 0;

    for (int i = 0; i < len_str; i++) {
        result[result_index++] = str[i];

        if (result_index >= len_explosion && strncmp(&result[result_index - len_explosion], explosion, len_explosion) == 0) {
            // 폭발 문자열을 찾으면 결과에서 제거
            result_index -= len_explosion;
        }
    }
    // 남은 문자열 출력
    if (result_index == 0) {
        printf("FRULA\n");
    } else {
        result[result_index] = '\0';
        printf("%s\n", result);
    }

    return 0;
}
