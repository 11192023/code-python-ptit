from math import*
from collections import Counter 
from functools import cmp_to_key
# hàm main đề chạy chương trình trong python 
if __name__=="__main__":
    # t là số test case
    t=int(input())
    while t:
        n=input()
        n=n+'#'
        length=len(n)
        dem=1
        res=[]
        for i in range(1,len(n)):
            if n[i]==n[i-1]:
                dem+=1
            else:
                res.append(str(dem))
                res.append(n[i-1])
                dem=1
        print(''.join(res))
        t-=1