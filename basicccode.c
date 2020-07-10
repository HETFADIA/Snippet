#include<stdio.h>
#include<string.h>
#include <stdlib.h>
#include <math.h>
#define lld long long int
int cmpfunc (const void * a, const void * b);
int dcmpfunc (const void * a, const void * b);
lld max(lld num1, lld num2);
lld min(lld num1, lld num2);
// lld * arr = (lld*)malloc(n * sizeof(lld)); 
void sequence(){
    lld n;
    lld sum=0;
    scanf("%llu",&n);
    lld * arr = (lld*)malloc(n * sizeof(lld)); 
    for(lld i=0;i<n;i++){
        scanf("%llu",&arr[i]);

    }
    for(lld i=0;i<n-1;i++){
        sum+=abs(arr[i]-arr[i+1])-1;
    }
    printf("%llu\n",sum);
}
int main(){
    lld t;
    scanf("%llu",&t);
    while(t--){
        sequence();
    }
    
}
int cmpfunc (const void * a, const void * b) {
   return ( *(lld*)a - *(lld*)b );
}
int dcmpfunc (const void * a, const void * b) {
   return -( *(lld*)a - *(lld*)b );
}
lld max(lld num1, lld num2)
{
    return (num1 > num2 ) ? num1 : num2;
}
lld min(lld num1, lld num2) 
{
    return (num1 > num2 ) ? num2 : num1;
}
