from math import*
from collections import Counter
from functools import cmp_to_key
# hàm result
def result(n,m):
    a=[]
    max_value=-10**9
    min_value=10**9
    for i in range(n):
        b=list(map(int,input().split()))
        max_value=max(max_value,max(b))
        min_value=min(min_value,min(b))
        a.append(b)
    the_lucky_number=max_value-min_value
    print(the_lucky_number,end='\n')
    ok=0
    for i in range(n):
        for j in range(m):
            if a[i][j]==the_lucky_number:
                ok=1
                print("Vi tri [{0}][{1}]".format(i,j),end='\n')
    if ok==0:
        print("NOT FOUND")
# hàm main để chạy chương trình trong python 
if __name__=="__main__":
    n,m=map(int,input().split())
    result(n,m)
   


