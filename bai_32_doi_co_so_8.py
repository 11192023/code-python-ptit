from math import*
from functools import cmp_to_key
from collections import Counter
#hàm chuyển đổi
def check(s):
    sum=0
    dem=0
    for i in range(len(s)-1,-1,-1):
        if s[i]=='1':
            sum+=2**dem
        dem+=1
    return str(sum)

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
    result=''.join(result)
    result=result.split(',')
    ans=[]
    for x in result:
        ans.append(check(x))
    print(''.join(ans))



