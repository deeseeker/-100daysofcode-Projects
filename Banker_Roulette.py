import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#method 1

num_items = len(names)

random_choice = random.randint(0,num_items-1)
print(random_choice)
bill_payer = names[random_choice]
print(bill_payer + " is going to buy the meal today")
