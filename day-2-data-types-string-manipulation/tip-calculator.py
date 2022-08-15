print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
group_size = int(input("How many people to split the bill? "))

divided_bill_with_tip = total_bill * (1 + (percentage / 100)) / group_size

print(f"Each person should pay: ${round(divided_bill_with_tip, 2)}")
