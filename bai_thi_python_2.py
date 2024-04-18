from math import*
# hàm main để chạy chương trình trong python
if __name__=="__main__":
    s=input()
    dict={}
    leather='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dem=25
    for x in leather:
        dict[x]=leather[dem]
        dem-=1
    fresh=''
    for x in s:
        fresh+=x.upper()
    print(fresh)
    result=''
    for x in fresh:    
        if x>='65' and x<='90':
            result+=dict[x]
        else:
            result+=x
    print(result)
#Sinh vien PTIT D21


