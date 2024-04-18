from math import*
from collections import Counter
from functools import cmp_to_key
#hàm đưa về ma trận vuông theo yêu cầu đề bài
def change_sqare_matrix(n,m,matrix):
    count_remove=abs(n-m)
    if n>m:
        i=0
        for _ in range(count_remove):
            matrix.pop(i)
            i+=1
    elif n<m:
        for row in matrix:
            i=1
            for _ in range(count_remove):
                row.pop(i)
                i+=1
            i=1
    return matrix
# hàm main để chạy chương trình trong python
if __name__=="__main__":
    n,m=map(int,input().split())
    matrix=[]
    for i in range(n):
        row =list(map(int ,input().split()))
        matrix.append(row)
    result=change_sqare_matrix(n,m,matrix)
    for row in result:
        print(' '.join(map(str ,row)))
