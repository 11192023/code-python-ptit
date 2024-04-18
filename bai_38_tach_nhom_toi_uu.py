from math import*
from collections import Counter
from functools import cmp_to_key
# hàm main để chạy chương trình bằng python
if __name__=="__main__":
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    b=[]
    res=[]
    b.append(a[0])
    for i in range(1,n):
        if a[i]-a[i-1]<=k:
            b.append(a[i])
            if i==n-1:
                res.append(b)
        elif i==n-1:
            res.append(b)
            b=[]
            b.append(a[n-1])
            res.append(b)
        else:
            res.append(b)
            b=[]
            b.append(a[i])
    print(len(res))
    



