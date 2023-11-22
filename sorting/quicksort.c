#include <stdio.h>

/*
Pivot선택 방법에 따라 성능차이
1. 처음 or 끝 요소 선택
정렬된 배열에서 최악의 성능 O(n^2)

2. 중간 요소 선택
일반적으로 괜찮은 성능

3. 랜덤 요소 선택
일반적으로 괜찮은 성능

4. 처음,중간,끝의 중앙값 선택
최악의 경우에도 성능개선가능
하지만 중앙값을 계산하는 오버헤드가 약간 발생한다.

시간복잡도 : 
평균적으로 O(nlogn)
최악의 경우 O(n^2) -> 재귀를 n번 호출하므로
중앙값을 피벗으로 선택시 nlogn보장함

공간복잡도 : O(n)

불안정 정렬

*/
void swap(int *a, int *b)
{
    int temp;

    temp = *a;
    *a = *b;
    *b = temp;
}

int find_median(int *arr, int left, int right)
{
    int middle;

    middle = (left + right) / 2;
    if(arr[left] > arr[middle])
        swap(&arr[left], &arr[middle]);
    if(arr[left] > arr[right])
        swap(&arr[left], &arr[right]);
    if(arr[middle] > arr[right])
        swap(&arr[middle], &arr[right]);  
    return (middle);  
}

int partition(int *arr, int left, int right)
{
    int pivot_index = find_median(arr, left, right);
    int pivot = arr[pivot_index];
    int i = left;

    swap(&arr[pivot_index],&arr[right]);
    for(int j=left; j<right; j++)
    {
        if(arr[j] <= pivot)
        {
            swap(&arr[i],&arr[j]);
            i++;
        }
    }
    swap(&arr[i],&arr[right]);
    return (i);
}

void quick_sort(int *arr, int left, int right)
{
    int pivot;

    if(left >= right)
        return;
    pivot = partition(arr, left, right);
    printf("%d\n",pivot);
    quick_sort(arr, left, pivot - 1);
    quick_sort(arr, pivot + 1, right);
}


int main()
{
    int arr[10] = {5,2,1,3,8,7,9,4,6,0};
    quick_sort(arr,0,9);
    printf("check\n");

    for(int i=0;i<10;i++)
    {
        printf("%d",arr[i]);
    }
    return (0);
}
