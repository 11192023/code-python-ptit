from math import *
from collections import Counter
from functools import cmp_to_key
# hàm main để chạy chương trình trong python 
if __name__=="__main__":
    # t là số lượng test case
    t=int(input())
    while t:
        n=input()
        first=(n[:2])
        last=(n[-2:])
        if first==last:
            print("YES")
        else:
            print("NO")
        t-=1
    
        