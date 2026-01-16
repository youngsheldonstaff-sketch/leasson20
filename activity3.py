def hotelcost (nights):
    return nights *140


def planecost (city):
    if "chorlete" == city:
        return 183
    elif "tampa" == city:
        return 220
    elif "pittsburg" == city:
        return 222
    elif "los angeles" == city:
        return 475
    

def rentalcarcost (days):
    if days >= 7:
        return days*40 - 50
    elif days>=3:
        return days*40 - 20
    else:
        return 40*days
    

def tripcost (city,days,spendingmoney):
    totalcost = planecost(city) + hotelcost(days) + rentalcarcost(days) + spendingmoney
    return totalcost

print("cost of car rental   ", rentalcarcost(10))
print("cost of hotel stay   ", hotelcost(5))
print("cost of plane ticket ", planecost("tampa"))
print("total trip cost      ", tripcost("tampa",5,600))