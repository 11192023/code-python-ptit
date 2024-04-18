from math import *
from collections import Counter
from functools import cmp_to_key
# hàm main để chạy chương trình trong python
if __name__=="__main__":
    t=int(input())
    while t:
        n=input()
        opposite=n[::-1]
        if gcd(int(n),int(opposite))==1:
            print("YES")
        else:
            print("NO")
        t-=1
        
