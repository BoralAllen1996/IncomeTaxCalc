#Program to identify the tax of user........................

income = int(input("\nPlease enter your income? ")) # User must input the income amount...

if income <= 10_000:
     tax = 0
elif income <= 20_000: 
    tax = (income - 10_000) * 0.1              # 10% on income above 10K
else:
    tax = (income-20_000) * 0.2 +  10_000*0.1  # 20% on income above 20K, plus tax on 10K of income below 20K

print(f"For income {income}, You owe {tax} pesos in tax!\n" )
 
 #END...............
