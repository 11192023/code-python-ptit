from math import*
from collections import Counter
from functools import cmp_to_key
# hàm main để chạy chương trình trong python
def check_reverse_number(n):
    n=str(n)
    if len(n)==1:
        return False
    elif n==n[::-1]:
        return True
    return False

if __name__=="__main__":
    t=int(input())
    while t:
        n=(input())
        sum_n=0
        for x in n:
            sum_n+=int(x)
        if check_reverse_number(sum_n)==1:
            print("YES")
        else:
            print("NO")
        t-=1
