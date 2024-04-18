from math import*
# hàm check
def check(n):
    sum=0
    tmp=n
    while n!=0:
        sum +=factorial(n%10)
        n//=10
    return sum==tmp
# hàm main để chạy chương trình trong python 
if __name__=="__main__":
    n=int(input())
    for _ in range(n):
        n=int(input())
        if check(n):
            print('Yes')
        else:
            print('No')
