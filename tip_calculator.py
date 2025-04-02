print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
# チップの百分率
tip_as_percent = tip / 100
# チップの総額
total_tip_amount = bill * tip_as_percent
# 請求金額+チップの総額
total_bill = bill + total_tip_amount
# 一人当たりの支払い金額
bill_per_person = total_bill / people
# 一人当たりの金額を小数点以下２桁で丸める
final_amount = round(bill_per_person, 2)
# Fストリングスで表示
print(f"Each person should pay: ${final_amount}")


