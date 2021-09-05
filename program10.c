/* Given an array in such a way that the elements stored in array are in increasing order initially and then after reaching to a peak element , elements stored are in decreasing order. Find the highest element.
Note: A[i] != A[i+1] */
#include<stdio.h>
int main()
{
	int n, l, max;
	scanf("%d", &n);
	for(int i = 1; i<=n; i++)
	{
	    scanf("%d", &l);
	    int arr[l];
	    for(int i = 0; i<l; i++)
	    {
	        scanf("%d", &arr[i]);
	    }
	    max = arr[0];
	    for(int i =0; i<l; i++)
	    {
	        if(max<arr[i])
	        max = arr[i];
	    }
	    printf("%d\n", max);
	}
	return 0;
}