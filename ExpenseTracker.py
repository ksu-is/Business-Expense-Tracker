# Borrowed some Code from Michael Walden

# enter the monthly budget provided
currentBudget = 20000

def main():
    print('Welcome to Expense Tracker 1.0! ')

    closeProgram = 'no'
    totalBudget = currentBudget

    while closeProgram == 'no': 
        print()
        print('Expense Tracker Selections: ')
        print('1- Add your Monthly Expenses Total (Rent, Food, Labor, Maintenance, Etc..): ')
        print('2- Would you like to remove an expense?: ')
        print('3- Check your remaining Monthly Budget: ')
        print('4- Exit Expense Tracker: ')
        print()

        choice = int(input('Proceed by entering a selection:'))
        if choice == 1:
            print()
            totalBudget = addExpense(totalBudget)

        elif choice == 2: 
            print()
            totalBudget = removeExpense(totalBudget)

        elif choice == 3:
            print()
            print('Your current remaining monthly budget is {0}'.format(totalBudget))

        elif choice == 4:
            print()
            closeProgram = 'yes'
            print('Expense tracker will now close. Have a nice day!')

        else:
            print('You have not entered a valid selection, please do so again')

def addExpense(totalBudget):
    expense = float(input('Enter your total monthly expenses amount: $'))
    totalExpense = expense
    if totalBudget - totalExpense >= 0:
        totalBudget = totalBudget - totalExpense
        print('Your business expenses have been recorded, your remaining total for the month is: ${}'.format(totalBudget))
        return totalBudget

    else:
        print('This expense cannot be added to your total!')
        return totalBudget
   

def removeExpense(totalBudget):
    remove = float(input('Enter the amount you would like to remove: $'))
    totalRemove = remove
    if totalBudget + totalRemove >= 0:
        totalBudget = totalBudget + totalRemove
        print('Your expense has been removed, and your remaining total is now: ${}'.format(totalBudget))
        return totalBudget
    

main()
