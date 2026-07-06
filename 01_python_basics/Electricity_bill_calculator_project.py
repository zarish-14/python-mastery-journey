print("=============================")
print("    Electricity Bill         ")
print("=============================")

customer_name=input("Enter name of customer: ") #user inputs
customer_id=input("Enter cutomer id: ")
units_consumed=int(input("Enter your consumed unit: "))
print("Customer :" , customer_name)
print("Customer ID: ", customer_id)
print("Units: ", units_consumed)
if 0 <= units_consumed <= 100: #Calculating rates according to the units consumed 
    rate_per_unit=10
elif 101 <= units_consumed <= 200:
    rate_per_unit=15
elif 201<= units_consumed <= 300:
    rate_per_unit=20
elif units_consumed >300:
    rate_per_unit=25
else:
    print("invalid")
    exit()
bill=units_consumed*rate_per_unit
if bill > 5000 : #Calculating surcharge
    surcharge= bill * 0.05
    total_bill=bill + surcharge
else:
    surcharge=0
    total_bill=bill
print("Rate: Rs ",rate_per_unit)
print("Bill: Rs ",bill)
print("Surcharge: Rs ",surcharge)
print("Total Bill: Rs ",total_bill)
print(" ===== Thank You! =====  ")
       

