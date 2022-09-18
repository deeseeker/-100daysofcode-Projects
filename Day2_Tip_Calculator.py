
print('Welcome to the Tip Calculator')

#prompt user for inputs
total_bill = input('What was the total bill?')
percentage_tip = input('What percentage tip would you like to give? 10,12, or 15?')
people_split = input('How many people to split the bill?')

#proces the data
tot_bill = int(total_bill.replace('$',''))
perc_tip = int(percentage_tip)/100
people_as_int = int(people_split)

perc_share = round((tot_bill/people_as_int) * (1 +perc_tip),2)

print(f'Each person should pay {perc_share}')
