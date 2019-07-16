# Used original code from Michael Walden and modified into a working program to track the total of business expenses each month and outputting how much is leftover.


# enter the monthly budget provided
currentBudget = 40000



def main():
    print('Welcome to Expense Tracker 1.0! ')

    closeProgram = 'no'
    totalBudget = currentBudget

    while closeProgram == 'no': 
        print()
        print('Expense Tracker Selections: ')
        print('1- Add your Monthly Expenses Total (Rent, Food, Labor, Maintenance, Etc..): ')
        print('2- Check your remaining Monthly Budget: ')
        print('3- Exit Expense Tracker: ')
        print()

        choice = int(input('Proceed by entering a selection:'))
        if choice == 1:
            print()
            totalBudget = addExpense(totalBudget)

        elif choice == 2:
            print()
            print('Your current monthly budget is {40000}'.format(totalBudget))
        
        elif choice == 3:
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
        print('Your business expenses have been recorded, your remaining total for the month is: ${0}'.format(totalBudget))
        return totalBudget

    else:
        print('You have exceeded your monthly budget!')
        return totalBudget

main()
