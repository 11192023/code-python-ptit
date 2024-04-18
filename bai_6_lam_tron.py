from math import*
from collections import Counter
from functools import cmp_to_key
# hàm round để làm tròn số
def round(n):
    n=str(n)
    a=[]
    for x in n:
        a.append(x)
    if len(a)==1:
        res=''.join(a)
        return res
    rem=0
    res=[]
    for i in range(len(a)-1,-1,-1):
        if int(a[i])+rem>=5 and i !=0:
            res.append(str(0))
            rem=1
        elif i==0:
            res.append(str(int(a[i])+rem))
        else:
            res.append(str(0))
            rem=0
        res=res[::-1]
        result=int(''.join(res))
    return result
# hàm main để chạy chương trình trong python 
if __name__=="__main__":
    t=int(input())
    while t:
        n=int(input())
        result=round(n)
        print(result)
        t-=1
