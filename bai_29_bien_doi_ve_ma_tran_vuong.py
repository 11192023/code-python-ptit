from math import*
from collections import Counter
from functools import cmp_to_key
# hàm main để chạy chương trình trong python 
if __name__=="__main__":
    n,m=map(int ,input().split())
    a=[]
    a.append(' ')
    for i in range (1,n+1):
        b=[]
        b.append('+')
        b=b+list(map(int,input().split()))
        a.append(b)
    ans=abs(n-m)
    if n>m:
        dem=0
        ok=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if i%2==1 and dem<2:
                    dem+=1
                    ok=1
                    break
                print(a[i][j],end=' ')
                ok=0
            if ok !=1:
                print()
    elif n<m:
        dem=0
        ok=0
        b=[]
        ans1=0
        for i in range (ans):
            ans1=ans1+2
            b.append(ans1)
        for i in range(1,n+1):
            for j in range(1,m+1):
                if j in b:
                    continue
                print(a[i][j],end=' ')
            print()
    else:
        for i in range(1,n+1):
            for j in range(1,m+1):
                print(a[i][j],end=' ')
            print()




        
