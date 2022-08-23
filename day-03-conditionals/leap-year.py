# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

leap_year = True

if year % 4 != 0:
    leap_year = False
else:
    if year % 100 == 0 and year % 400 != 0:
        leap_year = False

print("Leap year.") if leap_year == True else print("Not leap year.")
