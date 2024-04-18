from math import*
from collections import Counter
from functools import cmp_to_key
# hàm main để chạy chương trình trong python
if __name__=="__main__":
    while True :
        a=list(input().split())
        a[0]=int(a[0])
        length=len(a)
        if len(a)==1:
            break
        k=a[0]
        n=a[1]
        if k==0:
            break
        first='ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
        p=[]
        for x in first:
            p.append(x)
        s=[]
        dem=0
        for x in n:
            s.append(p[(p.index(x)+k)%28])
        s=''.join(s)
        s=s[::-1]
        print(s)

        
