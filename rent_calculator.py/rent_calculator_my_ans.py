##Input we need from the user
# Total rent
# Total food ordered for snacking
# Electricity units spend
# Charge per Unit

# #Output
# Total amount you've to pay is

rent=float(input("What's the total rent of room?:"))
food= float(input("Please input the food cost ordered for snacking: "))
elect=float(input("Electricity units consumed (in watts): "))
elect_charges= 8

electricity=float (elect *elect_charges)
person= int(input("Please enter the no. of persons who are sharing the room:"))

Total_amount= (rent+ food +electricity)
Amount_by_each_person= Total_amount/person

print("\n ----  Reciept Processed  ----")
print("Total rent amount with rent + food + elctricity charges :",Total_amount )

print("The amount to be paid by each person is:",Amount_by_each_person)