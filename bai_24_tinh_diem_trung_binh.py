from math import*
from collections import Counter
from functools import cmp_to_key
# hàm main để chạy chương trình trong python 
if __name__=="__main__":
    n=int(input())
    a=list(map(float,input().split()))
    max_number=max(a)
    min_number=min(a)
    a_more=[]
    for x in a:
        if x==max_number or x==min_number:
            continue
        a_more.append(x)
    sum=sum(a_more)
    average=round(sum/len(a_more),2)
    print(average)