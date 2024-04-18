from math import*
from collections import Counter
from functools import cmp_to_key
# hàm main để chạy chương trình trong python 
if __name__=="__main__":
    # t là số test case
    t=int(input())
    while t:
        n=input()
        res=[]
        length=len(n)
        for i in range(len(n)):
            if n[i]>='1' and n[i]<='9':
                res.append(n[i-1]*int(n[i]))
        print(''.join(res))
        t-=1