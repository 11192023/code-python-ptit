from math import*
from collections import Counter
from functools import cmp_to_key
# hàm chuẩn hóa thời gian 
def tran_date(s):
    if s[2]!='/':
        s='0'+s
    if s[5]!='/':
        s=s[:3]+'0'+s[3:]
    return s
def return_day_of_month(month,year):
    month_init=month
    year_init=year
    year_init=int(year_init)
    if month=='01' or month =='03' or month=='05' or month=='07' or month =='08' or month=='10' or month =='12':
        return 31
    elif month=='04' or month =='06' or month =='09' or month =="11":
        return 30
    else:
        if year_init%400==0:
            return 29
        elif year_init%4==0 and year_init %100!=0:
            return 29
        else:
            return 28
def return_day_of_year(year):
    if int(year)%400==0:
        return 366
    elif int(year)%4==0 and int(year)%100!=0:
        return 366
    else:
        return 365
# hàm class
class customers:
    def __init__(self,code ,name,the_number_room,receive_room_date,pay_room_date,extra_money_service):
        self.code ="KH"+format(code,'02d')
        self.name=name 
        self.the_number_room=the_number_room
        self.receive_room_date=tran_date(receive_room_date)
        self.pay_room_date=tran_date(pay_room_date)
        self.extra_money_service=extra_money_service
    def get_day(date):
        day=date[0:2]
        return day
    def get_month(date):
        month=date[3:5]
        return month 
    def get_year(date):
        year=date[6:]
        return year
    def get_price(self):
        floor=self.the_number_room[0:1]
        if floor=='1':
            return 25
        elif floor=='2':
            return 34
        elif floor=='3':
            return 50
        else:
            return 80
    def return_the_floor(self):
        the_floor=self.the_number_room[:1]
        return the_floor
    def return_day_live(self):
        day_1=int(self.get_day(self.receive_room_date))
        month_1=int(self.get_month(self.receive_room_date))
        year_1=int(self.get_year(self.receive_room_date))
        day_2=int(self.get_day(self.receive_room_date))
        month_2=int(self.get_month(self.receive_room_date))
        year_2=int(self.get_year(self.receive_room_date))
        if year_1==year_2:
            number_day_of_the_first_month=return_day_of_month(month_1,year_1)
            the_remaning_day=number_day_of_the_first_month-day_1
            the_total_day=0
            if month_1==month_2:
                the_total_day=day_2-day_1
            else:
                for i in range(month_1+1,month_2):
                    the_remaning_day+=return_day_of_month(i,year_1)
                the_total_day=the_remaning_day+day_2
            return the_total_day
        else:
            the_number_of_year_1=return_day_of_year(year_1)
            the_number_of_year_2=return_day_of_year(year_2)
            the_day_to_month_1=0
            

            

                    
                






# hàm main để chạy chương trình trong python
if __name__=="__main__":
