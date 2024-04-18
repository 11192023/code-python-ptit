from math import*
from collections import Counter
from functools import cmp_to_key
# hàm main để chạy chương trình trong python
if __name__=="__main__":
    n=int(input())
    dict={}
    a=list(map(int,input().split()))
    for x in a:
        dict[x]=0
    for i in range(n):
        pivot=a[i]
        sum=0
        for i in range(n):
            if a[i]!=pivot:
                sum+=abs(a[i]-pivot)
        dict[pivot]=sum
    sum_of_walk=0
    element=0
    min_value=10**8
    for x,y in dict.items():
        if min_value>y:
            min_value=y
            element=x
            sum_of_walk=y
    print(sum_of_walk,element,sep=" ")


    

