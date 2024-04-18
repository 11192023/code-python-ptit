from math import *
from collections import Counter
from functools import cmp_to_key
# hàm main để chạy chương trình trong python
if __name__=="__main__":
    n=input()
    result=[]
    char=','
    dem=0
    for  i in range(len(n)-1,-1,-1):
        dem+=1
        result.append(n[i])
        if dem==3 and i !=0:
            result.append(char)
            dem=0
    result=result[::-1]
    print(''.join(result))
        

