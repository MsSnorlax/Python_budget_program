
#Budget and expenses dictionary
budget = {'income': 0, 'expenses': {}, 'savings': 0}

# get user input for income
budget['income'] = float(input("Enter your total income: "))

# get user input for expenses
num_expenses = int(input("How many expenses do you have? "))
for i in range(num_expenses):
    expense_name = input("Enter the name of expense #" + str(i+1) + ": ")
    expense_amount = float(input("Enter the amount of expense #" + str(i+1) + ": "))
    budget['expenses'][expense_name] = expense_amount

# get user input for savings goal
budget['savings'] = float(input("Enter your savings goal for the month? "))

# calculate the budget
savings = input("Enter the amount into savings: ")
total_expenses = sum(budget['expenses'].values())
budget_amount = budget['income'] - total_expenses - budget['savings']

# print the budget
print("Your budget for the month is: $", format(budget_amount, ".2f"))
print("Here's a breakdown of your expenses:")
for expense_name, expense_amount in budget['expenses'].items():
    print("- " + expense_name + ": $" + str(expense_amount))
print("Your savings goal for the month is: $", format(budget['savings']))
