city = input("enter your city name")
temp = float(input("enter todays temprature"))
if temp > 35:
    print("warning: it is very hot today")
if temp > 25:
    print("great day today. go out")
if temp > 35:
    print("dont go outside")
elif temp > 25:
    print("great day today")
elif temp > 15:
    print("cold today")
else:
    print("weather is cold. stay warm")
import datetime
import calendar
now = datetime.datetime.now()# date and time now
print("city" ,city)
print("time",now)
print(calendar.calendar,("now.year"))