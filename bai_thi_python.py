from math import*
from collections import Counter
from functools import cmp_to_key
#hàm tính giá cước
def taxi_bill(sp,wt):
    wt=int(wt)
    the_wait_price=wt*1000
    the_total_money=0
    if sp<1:
        the_total_money=20000
    elif sp<=30:
        the_total_money=sp*15000
    else:
        the_remaning_km=float(sp-30)
        if the_remaning_km<1:
            the_total_money=30*15000+20000
        elif the_remaning_km<=30:
            the_total_money=30*15000+the_remaning_km*12500
    the_total_money=the_total_money+the_wait_price
    return int(the_total_money)
# hàm main để chạy chương trình trong python 
if __name__=="__main__":
    sp,wt=map(float,input().split())
    the_total_money=taxi_bill(sp,wt)
    print(the_total_money)
    #0.8 0
    #1.5 0
    #1.0 1