expenses = []

total = 0

while True:
    amount = input("Enter expense amount (or type 'done'): ")

    if amount.lower() == 'done':
        break

    amount = float(amount)
    expenses.append(amount)
    total += amount

print("\nExpenses:")
for expense in expenses:
    print(expense)

print("Total Expense:", total)