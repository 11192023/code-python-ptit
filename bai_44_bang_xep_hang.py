from math import *
from collections import Counter
from functools import cmp_to_key
# hàm main để chạy chương trình trong python
if __name__=="__main__":
    t=int(input())
    students=[]
    for i in range(t):
        name=input()
        correct,submit=map(int,input().split())
        students.append((name,correct,submit))
    students.sort(key= lambda x:(-x[1],x[2],x[0]))
    for i,student in enumerate(students,start=1):
        print(student[0],student[1],student[2])
