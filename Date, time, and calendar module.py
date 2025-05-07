from datetime import date, time, datetime
import random
import time
#calling the today:
# function class of date:
today = date.today()
now = datetime.now()

print(f"Todays date is {today}")
print(f"Todays time is {now}")

# Random date and time:

def getRandomDate(starDate, endDate):
    print("Printing random date between", starDate, "and", endDate)
    randomgen = random.random()
    date_format = '%d/%m/%Y'
    starttime = time.mktime(time.strptime(starDate, date_format))
    endtime = time.mktime(time.strptime(endDate, date_format))
    randomtime = starttime + randomgen * (endtime - starttime)
    randomdate = time.strftime(date_format, time.localtime(randomtime))
    return randomdate

print("Random date = ", getRandomDate("1/1/2026", "12/12/2040"))

# trip expendeture:
def hotelcost(nights):
    return 140*nights

# define a function named plane ride cost:
def planeridecost(city):
    if "charlotte" == city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pittsburg" == city:
        return 222
    elif "Los Angles" == city:
        return 475

#define a function named rental car cost:
def rentalcarcost(days):
    if days >= 7:
        return 40*days - 50
    elif days >= 3:
        return 40*days - 20
    else:
        return 40 * days

# define a function called trip cost:
def tripcost(city, days, spendingmoney):
    return rentalcarcost(days) + hotelcost(days) + planeridecost(city) + spendingmoney

print("Cost of car rental: ", rentalcarcost(6))
print("Cost of plane ride: ", planeridecost("Los Angles"))
print("Cost of hotel room: ", hotelcost(7))   
print("   Total tripcost=  ", tripcost("Los Angles", 7,500))
print("Tampa, tripcost=  ", tripcost("Tampa", 6,500))