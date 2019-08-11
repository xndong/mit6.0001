# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:25:43 2019

@author: DongXiaoning
"""

total_month=0
portion_down_payment=0.25
current_savings=0
r=0.04
annual_salary=float(input("The starting annual salary:"))
portion_saved=float(input('The portion salary to be saved:'))
total_cost=float(input('''The cost of your dream home:'''))
semi_annual_raise=float(input('The semi-annual salary raise:'))

month_salary=annual_salary/12
down_payment=total_cost*portion_down_payment

while  current_savings<down_payment:
    month_return=current_savings*r/12
    month_salary_saved=month_salary*portion_saved
    month_total_saved=month_salary_saved+month_return
    current_savings+=month_total_saved
    total_month+=1
    if total_month % 6 ==0:
        month_salary=month_salary*(1+semi_annual_raise)
print('You need to cost: '+str(total_month)+' months to buy the house')
