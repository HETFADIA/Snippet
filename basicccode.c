#include<stdio.h>
#include<string.h>
#include <stdlib.h>
#include <limits.h> 
#include <math.h>
#define lld long long int
int cmpfunc (const void * a, const void * b);
int dcmpfunc (const void * a, const void * b);
lld max(lld num1, lld num2);
lld min(lld num1, lld num2);
lld sumofdigits(lld n);
struct Node {  
    int data;  
    struct Node* next;  
    struct Node* prev;  
}; 
// lld * arr = (lld*)malloc(n * sizeof(lld)); 
void sequence(){
    lld n;
    scanf("%lld",&n);
    lld arr1[n];
    lld arr2[n];
    for(lld i=0;i<n;i++){
        scanf("%lld",&arr1[i]);
        scanf("%lld",&arr2[i]);
    }
    lld a=0,b=0;
    for(lld i=0;i<n;i++){
        if(sumofdigits(arr1[i])>sumofdigits(arr2[i])){
            a++;
        }
        else if(sumofdigits(arr1[i])<sumofdigits(arr2[i])){
            b++;
        }
        else{
            a++;
            b++;
        }
    }
    a=4;
    lld *b=&a;
    printf("%lld",*b);
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
lld sumofdigits(lld n){
    lld ans=0;
    while(n>0){
        ans+=n%10;
        n/=10;
    }
    return ans;
}
