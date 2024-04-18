from math import *
from collections import Counter
from functools import cmp_to_key
# hàm so sánh
def get_name(dict):
    return dict["name"]
def get_correct(dict):
    return dict["correct"]
def get_submit(dict):
    return dict["submit"]
def cmp(a,b):
    name_1,name_2=get_name(a),get_name(b)
    correct1,correct2=get_correct(a),get_correct(b)
    submit1,submit2=get_submit(a),get_submit(b)
    if correct1!=correct2:
        if correct1>correct2:
            return -1
    else:
        if submit1!=submit2:
            if submit1<submit2:
                return -1
        else:
            if name_1<name_2:
                return -1
            else:
                return 1
# hàm main để chạy chương trình trong python
if __name__=="__main__":
    t=int(input())
    while t:
        a=[]
        for i in range(t):
            dict={}
            dict["name"]=input()
            dict["correct"],dict["submit"]=map(int,input().split())
            a.append(dict)
        a.sort(key=cmp_to_key(cmp))
        for x in a:
            print(x["name"],x["correct"],x["submit"],sep=" ")
        t-=1
