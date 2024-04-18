from math import*
from collections import Counter
from functools import cmp_to_key
#hàm return the distance shorstest 
def the_shortest_distance(matrix,n,m):
    the_minium_distance={}
    the_minium_distance[(n-1,m-1)]=0
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if i ==n-1 and j==m-1:
                continue
            if i+1<=n-1 and i+1>=0:
                down=a[i][j]-a[]
# hàm main để chạy chương trình trong python
if __name__=="__main__":
    t=int(input())
    while(t):
        n,m=map(int,input().strip().split())
        matrix=[]
        for i in range(n):
            row=list(map(int,input().strip().split()))
            matrix.append(row)
