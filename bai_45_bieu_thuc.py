from math import *
from collections import Counter
from functools import cmp_to_key
# khởi tạo stack
class stack: 
    def __init__(self):
        self.items=[]
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
# hàm đếm thứ tự trong của các dấu ngoặc
def count_order(expression):
    item=stack()
    order=[]
    dem=0
    for i,char in enumerate(expression):
        if char =='(':
            dem+=1
            stack.push(item,i)
            order.append(str(dem))
        elif char ==')':
            if stack.size(item)==1:
                order.append(str(stack.size(item)))
                continue
            order.append(str(dem))
            stack.pop(item)
            dem-=1
    return order
# hàm main để chạy chương trình trong python 
if __name__ =="__main__":
    t=int(input())
    while t:
        expression=input().strip()
        result=count_order(expression)
        print(' '.join(result))
        t-=1
