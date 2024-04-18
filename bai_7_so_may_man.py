from math import*
from collections import Counter
from functools import cmp_to_key
# hàm main để chạy chương trình trong python 
if __name__=="__main__":
    n=input()
    count_four=0
    count_seven=0
    for x in n:
        if x =='4':
            count_four+=1
        elif x=='7':
            count_seven+=1
    sum=count_four + count_seven
    if sum==4 or sum ==7:
        print("YES")
    else:
        print("NO")
    