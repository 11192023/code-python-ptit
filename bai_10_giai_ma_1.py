from math import*
from collections import Counter 
from functools import cmp_to_key
# hàm main đề chạy chương trình trong python 
if __name__=="__main__":
    # t là số test case
    t=int(input())
    while t:
        n=input()
        cnt=[0]*256
        for x in n:
            cnt[ord(x)]+=1
        res=[]
        for i in range(256):
            if cnt[i]!=0:
                res.append(str(cnt[i]))
                res.append(chr(i))
        print(''.join(res))
        t-=1