from math import*
def check(n):
    sum=0
    tmp_1=n
    tmp=n
    dem=0
    while tmp_1!=0:
        dem+=1
        tmp_1//=10
    while n!=0:
        sum+=pow(n%10,dem)
        n//=10

    if tmp==sum:
        return True 
    else:
        return False
def list_armstrong(n):
    for i in range(n+1):
        if check(i):
            print(i,end=" ")
def save(path,n):
    f=open("output_1.txt",'w')
    for i in range(n+1):
        if check(i):
            f.write(i)
    f.close()
if __name__=="__main__":
    n=int(input())
    
    
    