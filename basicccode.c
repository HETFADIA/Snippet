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
    lld a=4;
    lld *b=&a;
    printf("%lld",*b);

}
int main(){
    lld t;
    scanf("%lld",&t);
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
