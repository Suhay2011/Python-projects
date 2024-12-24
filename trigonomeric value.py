from datetime import date , time ,datetime

#calling the today
#function of date class
today = date.today()
now = datetime.now()
print("Today's date is" , today)
print("/nCurrent Date and Time is" ,now)

#printing date's components
print("/nDate components", today.year  ,today.month ,today.day)