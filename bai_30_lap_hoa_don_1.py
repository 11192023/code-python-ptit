from math import*
from collections import Counter
from functools import cmp_to_key
# class hóa đơn
class bill:
    def __init__ (self,code,name,index_old,index_new):
        self.code='KH'+format(code,'02d')
        self.name=name
        self.index_old=index_old
        self.index_new=index_new
        self.sum=0
    def get_phu_phi(self,index):
        if index>=0 and index<=50:
            return 2
        elif index>=51 and index<=100:
            return 3
        else:
            return 5
    def get_don_gia(self,index):
        if index>=0 and index<=50:
            return 100
        elif index>=51 and index<=100:
            return 150
        else:
            return 200
    def sum_water(self):
        index=self.index_new-self.index_old
        phu_phi=self.get_phu_phi(index)
        don_gia=self.get_don_gia(index)
        sum=int(index*don_gia)+((index*don_gia)*phu_phi)//100
        return sum 
    def print_t(self):
        self.sum=self.sum_water()
        print("{0} {1} {2}".format(self.code,self.name.title(),self.sum))
        
    
def cmp(a,b):
    tong_1,tong_2=a.sum_water(),b.sum_water()
    if tong_1>tong_2:
        return -1
    else:
        return 1
# hàm main để chạy chương trình trong python 
if __name__=="__main__":
    #khai báo số lượng hóa đơn
    n=int(input())
    a=[]
    for i in range(n):
        b=bill(i+1,input(),int(input()),int(input()))
        a.append(b)
    a.sort(key=cmp_to_key(cmp))
    for x in a:
        x.print_t()
        print('\n')
