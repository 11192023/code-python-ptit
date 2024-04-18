from math import*
from collections import Counter
from functools import cmp_to_key
# hàm isprime để kiểm tra số nguyên tố
def __isprime(n):
    if n<2:
        return False
    for i in range(2,isqrt(n)+1):
        if n% i==0:
            return False
    return True
#hàm ngược
def check1(n):
    res=0
    while n!=0:
        res=res*10+n%10
        n//=10
    return res
# hàm check số emirp
def check(n):
    if __isprime(n)==False:
        return False
    tmp=n
    res=0
    while n!=0:
        res=res*10+n%10
        n//=10
    if res==tmp:
        return False
    else:
        if __isprime(res):
            return True
        else:
            return False
# hàm main để chạy chương trình trong python 
if __name__=="__main__":
    t=int(input())
    while t:
        element=int(input())
        a=[]
        for i in range(12,element+1):
            if check(i) and check1(i)<=element:
              if i and check1(i) not in a:
                  a.append(i)
                  a.append(check1(i))
        for x in a:
            print(x,end=' ')
        print('\n')
        t-=1
    



        

        