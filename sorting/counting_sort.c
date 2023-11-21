#include <stdio.h>
#include <stdlib.h>

void countingSort(int arr[], int n) {
    // 입력 배열에서 최댓값 찾기
    int max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    // 카운팅 배열을 최댓값 크기만큼 생성하고 0으로 초기화
    int *count = (int *)calloc(max, sizeof(int));

    // 입력 배열에서 각 요소의 개수 세기
    for (int i = 0; i < n; i++) {
        count[arr[i]]++;
    }

    // 정렬된 배열을 만들기 위한 인덱스 변수
    int sortedIndex = 0;

    // 카운팅 배열을 사용하여 정렬된 배열 생성
    for (int i = 0; i <= max; i++) {
        while (count[i] > 0) {
            arr[sortedIndex] = i;
            sortedIndex++;
            count[i]--;
        }
    }

    // 동적 할당한 메모리 해제
    free(count);
}

int main() {
    int arr[] = {4, 2, 2, 8, 3, 3, 1};
    int n = sizeof(arr) / sizeof(arr[0]);

    countingSort(arr, n);

    printf("정렬된 배열: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}