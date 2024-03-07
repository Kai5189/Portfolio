expenses = []
expense1 = {'amount':'12.00', 'category':'Drink'}
expenses.append(expense1)


def removeExpense():
    while True:
        listExpenses()
        print("what expense would you like to remove")
        try:
            expenseToRemove = int(input("> "))
            del expenses[expenseToRemove]
            break
        except:
            print("Invalid input, please try again.")

def addExpense(amount,category):
    expense = {'amount': amount, 'category': category}
    expenses.append(expense)


def printMenu():
    print("Please chose a option")
    print("1. Add New Expense")
    print("2. Remove Expense")
    print("3. List all expenses")

def listExpenses():
    print("Here is your expenses")
    print("----------------------")
    counter = 0
    for expense in expenses:
        print("#", counter, "--",expense['amount'], "--", expense['category'])
        counter += 1
    print("----------------------")

if __name__ == "__main__":
  while True:
      ###Prompt User
      printMenu()
      optionSelected = input("> ")
      if optionSelected == "1":
          print("How much was this expense?")
          while True:
              try:
                  amountToAdd = input("> ")
                  break
              except:
                  print("Invalid input, please try again.")

          print("What category was this expense?")
          while True:
              try:
                  category = input("> ")
                  break
              except:
                  print("Invalid input, please try again.")

          addExpense(amountToAdd,category)
      elif(optionSelected == "2"):
          removeExpense()
      elif(optionSelected == "3"):
          listExpenses()
else:
    print("Invalid input, please try again.")