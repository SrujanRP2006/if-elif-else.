age = int(input("enter the age of the person>> "))
if age < 12:
    print("Movie ticket price is 100 rupees")
elif age >= 12 and age < 18:
    print("Movie ticket price is 150 rupees")
else:
    print("Movie ticket price is 200 rupees")