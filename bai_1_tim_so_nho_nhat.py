from math import*
from collections import Counter
from functools import cmp_to_key
# hàm main để chạy chương trình trong python
if __name__=="__main__":
    n=int(input())
    for _ in range(n):
        s=input()
        tmp=''
        for x in s:
            if x.isalpha():
                tmp+=' '
            else:
                tmp+=x
        s=(tmp.split())
        s=[int(x) for x in s]
        print(min(s))
        
