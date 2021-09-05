""" Given two sorted arrays arr1[] of size N and arr2[] of size M. Each array 
is sorted in non-decreasing order. Merge the two arrays into one sorted array
in non-decreasing order without using any extra space."""

for t in range(int(input())):
    numarr = list(map(int, input().split()))
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    i = numarr[0] - 1
    j = 0
    while(True):
        if(i>0 and j<numarr[1]):
            if(arr1[i]>arr2[j]):
                arr1[i], arr2[j] = arr2[j], arr1[i]
        else:
            break
        i -= 1
        j += 1
    arr1.sort()
    arr2.sort()
    for x in arr1:
        print(x, end=' ')
    for x in arr2:
        print(x, end=' ')
    print()