""" Given an array of positive numbers, the task is to find the number of p
ossible contiguous subarrays having product less than a given number k."""

t=int(input())
for i in range(t):
    n,key=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    temp,count,res=0,0,1
    for j in range(n):
        for k in range(temp,n):
            res*=arr[k]
            if res>=key:
                res/=arr[k]
                break
        else:
            k=n
        count+=(k-j)
        res=(res/(arr[j]))
        temp=k
        if k-j==0:
            res=1
            temp=k+1
    print(count)