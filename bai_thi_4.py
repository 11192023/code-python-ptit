from collections import Counter
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
def count_unique_armstrong(result):
    dict=list(dict(Counter(result).items))
    return (len(dict))
def max_frquent_armstrong(result):
    dict=list(dict(Counter(result).items))
    max=-10**9
    res=0
    for x,y in dict:
        if y>max:
            res=x
    return res

if __name__=="__main__":
    s=input()
    for x in s:
        if x.isalpha():
            s.replace(x,' ')
    s=s.strip()
    s=s.split
    count=0
    result=[]
    for x in s:
        if check(int(x)):
            count+=1
            result.append(int(s))
    print(count)
    count_unique_armstrong(result)
    max1=max_frquent_armstrong(result)
    print(max1)