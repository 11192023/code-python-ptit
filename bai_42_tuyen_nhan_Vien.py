from math import*
from collections import Counter
from functools import cmp_to_key
def return_correct_point(point):
    tmp=[]
    for x in point:
        tmp.append(x)
    if len(tmp)==1:
        return float(''.join(tmp))
    if len(tmp)==3:
        res=[]
        for i in range(len(tmp)):
            if i==2:
                res.append('.')
                res.append(tmp[i])
                break
            res.append(tmp[i])
        return float(''.join(res))
    if len(tmp)==2:
        res=[]
        for i in range(len(tmp)):
            if i==1:
                res.append('.')
                res.append(tmp[i])
                break
            res.append(tmp[i])
        return float(''.join(res))
#hàm class
class employee:
    def __init__(self,code,name,test,practice):
        self.code='TS'+format(code,'02d')
        self.name=name
        self.test=test
        self.practice=practice
        self.sum_a=0.00
    def _get_result_(self,point):
        if point<5:
            return "TRUOT"
        elif point>=5 and point<8:
            return "CAN NHAC"
        elif point>=8 and point<=9.5:
            return "DAT"
        else:
            return "XUAT SAC"
    def sum_average(self):
        sum=(round((self.practice+self.test)/2,2))
        self.sum_a=sum
        return self.sum_a
    def __str__(self):
        self.sum_average()
        result=self._get_result_(self.sum_a)
        result2=str('{:.2f}'.format(self.sum_a))
        return ('{0} {1} {2} {3}'.format(self.code,self.name.title(),result2,result))

def cmp(employee1,employee2):
    sum_1,sum_2=employee.sum_average(employee1),employee.sum_average(employee2)
    if sum_1>sum_2:
        return -1
    else:
        return 1
#hàm main đề chạy chương trình bằng python
if __name__=="__main__":
    t=int(input())
    a=[]
    for i in range(t):
        name=input()
        test=str((input()))
        practice=str((input()))
        if '.' not in test:
            test=test.strip()
            test=return_correct_point(test)
        else:
            test=float(test)
        if '.' not in practice:
            practice=practice.strip()
            practice =return_correct_point(practice)
        else:
            practice=float(practice)
        employees=employee(i+1,name,test,practice)
        a.append(employees)
    a.sort(key=cmp_to_key(cmp))
    for x in a:
        print(x)
        

        

        
