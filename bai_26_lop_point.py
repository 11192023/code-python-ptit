from math import*
from functools import cmp_to_key
from collections import Counter
# class point 
class point: 
    def __init__(self, x,y,z,k):
        self.x=x
        self.y=y
        self.z=z
        self.k=k
    def __str__(self):
        result=round(sqrt(pow(self.z-self.x,2)+pow(self.k-self.y,2)),4)
        result="{:.4f}".format(result)
        return str(result)

# hàm main để chạy chương trình trong python 
if __name__=="__main__":
    #t là số test case chương trình phải cần 
    t=int(input())
    while t:
        x,y,z,k=map(float,input().split())
        a =point(x,y,z,k)
        print(a)
        t-=1

    
