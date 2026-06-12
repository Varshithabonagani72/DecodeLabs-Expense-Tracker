total = 0

print("===== EXPENSE TRACKER =====")

while True:
    expense = input("Enter expense amount or type 'done' to finish: ")

    if expense == "done":
        break

    total = total + int(expense)

print("\nTotal Spent:", total)
print("Thank you for using Expense Tracker")