from math import*
from collections import Counter
from functools import cmp_to_key
# hàm main để chạy chương trình trong python 
def check_the_position(n):
    for i in range(1,len(n)-1):
        if int(n[i-1])<int(n[i]) and int(n[i])>int(n[i+1]):
            return i
        if int(n[i-1])==int(n[i]) or int(n[i])==int(n[i+1]):
            return -1
    return -1
def increase(first):
    for i in range(len(first)-1):
        if int(first[i])>int(first[i+1]):
            return False
    return True
def decrease(second):
    for i in range(len(second)-1):
        if int(second[i])<int(second[i+1]):
            return False
    return True     
if __name__=="__main__":
    t=int(input())
    while t:
        n=input()
        pos=check_the_position(n)
        if pos ==-1:
            print("NO")
        else:
            first=n[:pos+1]
            second=n[pos:]
            if increase(first) and decrease(second):
                print("YES")
            else:
                print("NO")
        t-=1
