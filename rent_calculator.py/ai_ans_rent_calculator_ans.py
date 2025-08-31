# Rent Calculator Script

# Input section
flat_rent = float(input("Enter your flat/hostel rent: ₹"))
food_expense = float(input("Enter total food expense: ₹"))
electricity_units = float(input("Enter electricity units consumed: "))
charge_per_unit = float(input("Enter charge per electricity unit: ₹"))
num_persons = int(input("Enter number of persons sharing the room: "))

# Calculation section
electricity_bill = electricity_units * charge_per_unit
total_amount = flat_rent + food_expense + electricity_bill
amount_per_person = total_amount / num_persons

# Output section
print("\n--- Rent Split Summary ---")
print(f"Total Rent + Food + Electricity: ₹{total_amount:.2f}")
print(f"Each person should pay: ₹{amount_per_person:.2f}")
