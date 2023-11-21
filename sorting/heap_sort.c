void	swap(int *arr, int a, int b)
{
	int	temp;

	temp = arr[a];
	arr[a] = arr[b];
	arr[b] = temp;
}

/*
첫노드의 인덱스는 0
now와 자식노드들을 비교하며 
now가 올바른 위치에 오도록 힙구성 
*/
void	heapify(int *arr, int n, int now)
{
	int p = now;
	int left = p * 2 + 1;
	int right = p * 2 + 2;

	if (left < n && arr[p] < arr[left])
		p = left;
	if (right < n && arr[p] < arr[right])
		p = right;
	if (p != now)
	{
		swap(arr, p, now);
		heapify(arr, n, p);
	}
}

void	heap_sort(int *arr, int n)
{
	//배열을 힙구조로 만든다.
	for (int i = (n - 1) / 2; i >= 0; i--)
	{
		heapify(arr, n, i);
	}
	//최대값을 가져오면서 다시 힙구조 구성
	for (int i = n - 1; i > 0; i--)
	{
		swap(arr, 0, i);
		heapify(arr, i, 0);
	}
}

#include <stdio.h>

int main(void)
{
	int arr[]= {1,4,7,2,5,8,3,6,9,0};

	heap_sort(arr,10);
	for(int i = 0; i < 10; i++)
		printf("i: %d ,%d\n",i,arr[i]);
}
