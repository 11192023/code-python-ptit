from math import*
from functools import cmp_to_key
from collections import Counter
# class point 
class point: 
    def __init__(self, x,y):
        self.x=x
        self.y=y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
def distance(x,y,z,k):
     result1=round(sqrt(pow(z-x,2)+pow(k-y,2)),4)
     return result1
#class triangle
class triangle: 
    def __init__(self, point_a,point_b,point_c):
        self.point_a=point_a
        self.point_b=point_b
        self.point_c=point_c
    def __str__(self):
        distance_1=distance(point.get_x(self.point_a),point.get_y(self.point_a), point.get_x(self.point_c),point.get_y(self.point_c))
        distance_2=distance(point.get_x(self.point_b), point.get_y(self.point_b),point.get_x(self.point_a),point.get_y(self.point_a))
        distance_3=distance( point.get_x(self.point_c),point.get_y(self.point_c), point.get_x(self.point_b), point.get_y(self.point_b))
        if float(distance_1)+float(distance_2)<=float(distance_3) or float(distance_2)+float(distance_3)<=float(distance_1) or float(distance_1)+float(distance_3)<=float(distance_2):
            return "INVALID"
        else:
            result=0.25*(sqrt((distance_1+distance_2+distance_3)*(distance_1+distance_2-distance_3)*(distance_2+distance_3-distance_1)*(distance_3+distance_1-distance_2)))
            return (str("{:.2f}".format(result)))

# hàm main để chạy chương trình trong python 
if __name__=="__main__":
    #t là số test case chương trình phải cần 
    t=int(input())
    while t:
        x,y,x2,y2,x3,y3=map(float,input().split())
        point_1=point(x,y)
        point_2=point(x2,y2)
        point_3=point(x3,y3)
        result=triangle(point_1,point_2,point_3)
        print(result,end='\n')
        t-=1

    
