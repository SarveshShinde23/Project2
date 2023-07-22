print("Welcome to the tip calculator!")
bill=float(input("What was the total bill? $"))
tip=int(input("How much tip would you like to give? 10,12, or 15?"))
split=int(input("How many people to split the bill?"))

tip_as_percent=tip /100
total_tip_amount= bill * tip_as_percent
total_bill =bill+total_tip_amount
bill_pre_person=total_bill /split
final_amount=round(bill_pre_person,2)

print(f"Each person sholud pay : ${final_amount}")

