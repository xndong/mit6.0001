# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 13:09:31 2019

@author: DongXiaoning
"""

#we will use funtion, 文档化函数,assert,类型检查,recursive function, three kinds of assignment

def month_salary_from_annual(annual_salary):
    'We assert the annual_salary is an interger and we do not need to cast it to float'
    assert isinstance(annual_salary,int),'Wrong type, annual_salary is not an interger'
    return annual_salary/12
    

def middle(start,end):
    'we caculate the middle value of start and end'
    assert isinstance(start,int),"Wrong type number"
    assert isinstance(end,int),'Wrong type number'
    middlevalue=(start+end)//2
    return middlevalue


def bisearch(head,target,tail,steps):
    "This is a naive bisearch function"
    if steps>20:
        print("It is not possible to pay the down payment in three years.")
        return #recursive function's end condition
    steps+=1
    midvalue=middle(head,tail)
    portion_saved=midvalue/float(10000)
    current_savings=compute_current_saving(0,portion_saved,month_salary)
    if current_savings>target+100:
        bisearch(head,target,midvalue,steps)
    elif current_savings<target-100:
        bisearch(midvalue,target,tail,steps)
    else:
        print("Best savings rate:",portion_saved)
        print("Steps in bisection search",steps)
        return midvalue  #recursive function's end condition

def compute_current_saving(current_savings,portion_saved,month_salary,goal_months=36,semi_annual_raise=0.07):
    total_month=0
    for i in range(goal_months):
        month_return=current_savings*r/12
        month_salary_saved=month_salary*portion_saved
        month_total_saved=month_salary_saved+month_return
        current_savings+=month_total_saved
        total_month+=1
        if total_month!=0 and total_month % 6 ==0:
            month_salary=month_salary*(1+semi_annual_raise)
    return current_savings

def comput_down_payment(total_cost,portion_down_payment):
    down_payment=total_cost*portion_down_payment
    assert type(down_payment)==float,"Argument wrong type."
    return down_payment


semi_annual_raise,r,portion_down_payment=0.07,0.04,0.25
total_cost,goal_months=1000000,36
current_saving=0
total_month=0
steps=0

annual_salary=int(input("Enter the starting salary:"))
month_salary=month_salary_from_annual(annual_salary)
down_payment=comput_down_payment(total_cost,portion_down_payment)
bisearch(0,down_payment,10000,steps)
    








