# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:39:25 2019

@author: DongXiaoning
"""
total_month=0
semi_annual_raise=0.07
r=0.04
portion_down_payment=0.25
total_cost=1000000
goal_months=36
current_savings=0

annual_salary=float(input('Enter the starting salary:'))
month_salary=annual_salary/12
down_payment=total_cost*portion_down_payment

bisearch_head=0
bisearch_tail=10000
bisearch_middle=(bisearch_head+bisearch_tail)/2
portion_saved=bisearch_middle/float(10000)
month_return=0
count=0
total_month=0
while True:
    current_savings=0
    month_salary=annual_salary/12
    for i in range(goal_months):
        month_return=current_savings*r/12
        month_salary_saved=month_salary*portion_saved
        month_total_saved=month_salary_saved+month_return
        current_savings+=month_total_saved
        total_month+=1
        if total_month!=0 and total_month % 6 ==0:
            month_salary=month_salary*(1+semi_annual_raise)
    #print(current_savings)

    if current_savings<down_payment-100:
        bisearch_head=bisearch_middle            
    elif current_savings>down_payment+100:
        bisearch_tail=bisearch_middle
    bisearch_middle=(bisearch_head+bisearch_tail)/2
    portion_saved=bisearch_middle/float(10000)        
       
    count+=1
    if current_savings<=down_payment+100 and current_savings>=down_payment-100:
        print('''Steps in bisection search:''',count)
        print('''Best savings rate:''',portion_saved)
        break
    elif count>15:#log2(10000)
        print('''It is not possible to pay the down payment in three years.''')
        break



