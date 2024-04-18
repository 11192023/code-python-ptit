from math import*
from collections import Counter
from functools import cmp_to_key
#hàm main để chạy chương trình trong python
if __name__=="__main__":
    n,m=map(int,input().split())
    a=set(list(map(str,input().split())))
    b=set(list(map(str,input().split())))
    intersection=list(a.intersection(b))
    intersection.sort()
    a_b=list(a.difference(b))
    a_b.sort()
    b_a=list(b.difference(a))
    b_a.sort()

    print(' '.join(intersection))
    print(' '.join(a_b))
    print(' '.join(b_a))