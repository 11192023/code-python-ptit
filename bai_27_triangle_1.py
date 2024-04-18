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
#class triangle
class triangle: 
    def __init__(self, x,y,x2,y2, x3,y3):
        self.x=x
        self.y=y
        self.x2=x2
        self.y2=y2
        self.x3=x3
        self.y3=y3
    def __str__(self):
        result1=round(sqrt(pow(self.x2-self.x,2)+pow(self.y2-self.y,2)),4)
        result2=round(sqrt(pow(self.x3-self.x2,2)+pow(self.y3-self.y2,2)),4)
        result3=round(sqrt(pow(self.x-self.x3,2)+pow(self.y-self.y3,2)),4)
        if result1+result2<=result3 or result2+result3<=result1 or result1+result3<=result2:
            return "INVALID"
        else:
            return str("{:.3f}".format(result1+result2+result3))

# hàm main để chạy chương trình trong python 
if __name__=="__main__":
    #t là số test case chương trình phải cần 
    t=int(input())
    while t:
        x,y,x2,y2,x3,y3=map(float,input().split())
        a =triangle(x,y,x2,y2,x3,y3)
        print(a)
        t-=1
result1=round(sqrt(pow(point_b.get_x()-point_a.get_x(),2)+pow(point_b.get_y()-point_a.get_y(),2)),4)
        result2=round(sqrt(pow(point_c.get_x()-point_b.get_x(),2)+pow(point_c.get_y()-point_b.get_y(),2)),4)
        result3=round(sqrt(pow(point_a.get_x()-point_c.get_x(),2)+pow(point_a.get_y()-point_c.get_y(),2)),4)
    
