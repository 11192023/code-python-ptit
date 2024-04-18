from math import*
from collections import Counter
from functools import cmp_to_key
# hàm main để chạy chương trình trong python
if __name__=="__main__":
    s=input()
    t=int(input())
    a=[]
    result=''
    if len(s)%2==0:
        dem=0
        for x in s:
            dem+=1
            if dem<=2:
                result=x+result
                if dem==2:
                    a.append(int(result[::-1]))
                    result=''
                    dem=0
        dict=list(dict(Counter(a)).items())
        dict.sort()
        ok=0
        for x,y in dict:
            if y>=t:
                ok=1
                print(x,y,sep=" ")
        if ok==0:
            print("NOT FOUND")
    else:
        dem=0
        for i in range(len(s)-1):
            dem+=1
            if dem<=2:
                result=s[i]+result
                if dem==2:
                    a.append(int(result[::-1]))
                    result=''
                    dem=0
        dict=list(dict(Counter(a)).items())
        dict.sort()
        ok=0
        for x,y in dict:
            if y>=t:
                print(x,y,sep=" ")
                ok=1
        if ok==0:
            print("NOT FOUND")






        
        
    