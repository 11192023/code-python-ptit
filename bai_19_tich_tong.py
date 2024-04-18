from math import* 
from functools import cmp_to_key
from collections import Counter
# hàm main để chạy chương trình trong python
if __name__=="__main__":
    t=int(input())
    while t:
        n=input()
        sum_odd=0
        product_even=1
        ok=1
        for i in range(len(n)):
            if i%2==0:
                sum_odd+=int(n[i])
            else:
                if int(n[i])!=0:
                    product_even*=int(n[i])
                    ok=0
        if ok==1:
            product_even =0
        print("{0} {1}".format(sum_odd,product_even))
        t-=1