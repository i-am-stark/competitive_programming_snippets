/* Ugly numbers are numbers whose only prime factors are 2, 3 or 5. 
The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers.
By convention, 1 is included. Write a program to find Nth Ugly Number. */

#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);
    while(t--){
        long n;
        long t2, t3, t5, c = 1, flag, mn;
        scanf("%d", &n);
        long arr[n];
        arr[0] = 1;
        long i = 0;
        long j = 0;
        long k = 0;
        while(c<n){
            t2 = arr[i]*2;
            t3 = arr[j]*3;
            t5 = arr[k]*5;
            mn =  (t2 < t3) ? ((t2<t5)?t2 :t5) : ((t5<t3) ? t5: t3);
            arr[c] = mn;
            c++;
            
            if(mn == t2)
                i+=1;
            if(mn == t3)
                j+=1;
            if(mn == t5)
                k+=1;
        }    
        long res = arr[n-1];
        printf("%ld\n", res);
    }
	return 0;
}