from math import*
from collections import Counter
from functools import cmp_to_key
# hàm main để chạy chương trình trong python 
if __name__=="__main__":
    n=input()
    char=n[-3:].lower()
    if char=='.py':
        print("yes")
    else:
        print("no")
    