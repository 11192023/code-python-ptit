from math import*
from collections import Counter
from functools import cmp_to_key
# hàm tổng
def sum(n):
    sum=1
    while n!=0:
        sum*=int(n%10)
        n//=10
    return sum
#hàm so sánh tổng chữ số 
def cmp(a,b):
    tong_1,tong_2=sum(a),sum(b)
    if tong_1!=tong_2:
        if tong_1<tong_2:
            return -1
        else:
            return 1
    else:
        return a-b
# hàm main để chạy chương trình trong python 

if __name__=="__main__":
    t=int(input())
    while t:
        n=int(input())
        a=list(map(int,input().split()))
        a.sort(key=cmp_to_key(cmp))
        for i in range(len(a)):
            if i==n-1:
                print(a[i])
                continue
            print(a[i],end=" ")
        t-=1