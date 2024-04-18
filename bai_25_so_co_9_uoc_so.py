from math import*
from collections import Counter
from functools import cmp_to_key
#kiem tra so nguyen to
def __isprime(n):
    if n<2:
        return False
    for i in range(2,isqrt(n)+1):
        if n% i==0:
            return False
    return True
# phân tích thừa số nguyên to 
def analyze(n):
    sum_uoc=1
    prime=[2,3,5,7,11,13]
    for x in prime:
            if n%x==0:
                cnt=0
                while n%x==0:
                    cnt+=1
                    n//=x
                sum_uoc*=(cnt+1)
    cnt=0
    if n>1:
        cnt+=1
        sum_uoc*=(cnt+1)
    if sum_uoc==9:
        return True 
    else:
        return False

            
# hàm main để chạy chuong trình trong python
if __name__=="__main__":
    n=int(input())

    ans=0
    for i in range(2,n):
        if __isprime(i)==0 :
            if analyze(i):
                ans+=1
    print(ans)
            
    