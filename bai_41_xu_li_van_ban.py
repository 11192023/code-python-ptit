from math import*
from collections import Counter
from functools import cmp_to_key
# hàm main để chạy chương trình trong python
if __name__=="__main__":
    n= """ky thi LAP TRINH ICPC PTIT  bat dau to chuc     tu     nam 2010. nhu vay, nam nay la          tron 10 nam!
    vay CO PHAI NAM NAY LA KY THI LAN THU 10?        khong phai! nam nay la KY THI LAN THU 11"""
    a=[]
    s=''
    for x in n:
        if x=='.' or x=='!' or x =='?':
            s=s.split()
            a.append(s)
            s=''
            continue
        s+=x
    if s!='':
        s=s.split()
        a.append(s)
    result=''
    for x in a:
        result=' '.join(x)
        result =result.lower()
        result =result.capitalize()
        print(result)
        
        
        