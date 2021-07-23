n=int(input())
# f=[]
# for i in range(n+1):
#     f.append(1)
a=1
b=1


for i in range(2,n+1):
    # f[i]=(f[i-1]+f[i-2])%10
    a,b=(a+b)%10,a

print(b)
