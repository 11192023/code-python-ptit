from math import *
from collections import Counter
from functools import cmp_to_key
# hàm check số ip
def isdigit(x):
    if x>='0' and x<='9':
        return True
    return False
def check(n):
    ques=n.split('.')
    if len(ques)!=4:
        return False
    for x in ques:
        if not isdigit(x) or not 0<=int(x)<=255:
            return False
    return True
# hàm main để chạy chương trình trong python 
if __name__=="__main__":
    t=int(input())
    while t:
        n=input()
        if check(n):
            print("YES")
        else:
            print("NO")
        t-=1
            
        
        