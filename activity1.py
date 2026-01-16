from datetime import date , time , datetime

today = date.today()
now = datetime.now()

print("today is:", today)
print ("right now is:", now)


print("\ndate components: ", today.year,today.month,today.day)
