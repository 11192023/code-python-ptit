from math import*
from collections import Counter
from functools import cmp_to_key
# hàm main để chạy chương trình trong python
def __isprime(n):
    if n<2:
        return False
    for i in range(2,isqrt(n)+1):
        if n% i==0:
            return False
    return True
def check_topic(n):
    for i in range(len(n)):
        if __isprime(i) != __isprime(int(n[i])):
            return False
    return True
if __name__=="__main__":
    t=int(input())
    while t:
        n=input()
        if check_topic(n):
            print("YES")
        else:
            print("NO")
        t-=1