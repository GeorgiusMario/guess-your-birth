print(10*"="+"-"+10*"=")
inputName = input("Input character = ")
import datetime as dt
print("please enter date, month, year")
date = int(input("date :"))
month = int(input("month :"))
year = int(input("year :"))
dateOfBirth = dt.date(year,month,date)#starting from last year
print(f"Your date of birth ?:{dateOfBirth}")
print(f"The day is ? : {dateOfBirth:%A}")
today = dt.date.today()
print(f"today\'s date = {today}")
days_old = today - dateOfBirth
years_old = days_old.days // 365# use floor devison total days 1th
monthOld_remaining = (days_old.days % 365) //30 # use floor devison total days 1 month
print(f"your age is = {years_old} years, {monthOld_remaining} month")
print(inputName , '=', years_old, "years" , monthOld_remaining, "mounth")

