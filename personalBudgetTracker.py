import csv

print("Welcome To Budget Planner")
income = int(input("How Much Is Your Income: \n"))
rent = int(input("How Much Is Your Rent: \n"))
utilities = int(input("How Much Are Your Utilities: \n"))
black_tax = int(input("How Much Is Your Black Tax: \n"))
groceries = int(input("How Much Are Your Groceries: \n"))
mis = int(input("How Much Can You Approx. Your Miscellanous Expenses: \n"))
totalExpenses = rent + utilities + groceries + mis
balance = income - totalExpenses
print(f"Your Balance Is {balance}")


data = {
    "Income": income,
    "Rent": rent,
    "Utilities": utilities,
    "Black Tax": black_tax,
    "Groceries": groceries,
    "Miscellanous": mis,
    "Available Balance": balance,
    "Totalspending": totalExpenses
    }

with open('budget.csv', 'w', newline='') as file:
    for key, value in data.items():
        file.write(f"{key} : {value}\n")
    writer = csv.writer(file)
with open('budget.csv', "a") as file:
    writer = csv.writer(file)
    file.write("Your Available Balance Is: " + str(balance))
with open('budget.csv', "r") as file:
    reader = csv.reader(file)
    print(list(reader))