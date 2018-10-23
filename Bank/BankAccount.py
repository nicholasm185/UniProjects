class Account:

    balance = 0

    def __init__(self, balance = 0):
        self.balance = balance

    def getBalance(self):
        return self.balance

    def deposit(self,amount):
        if amount < 0:
            print("You cannot enter your debts!")
        else:
            self.balance += amount
            print("Transaction successful!")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print("Transaction successful!")

class Customer:

    firstName = ""
    lastName = ""
    account = ""

    def __init__(self, firstname, lastname):
        self.firstName = firstname
        self.lastName = lastname

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getAccount(self):
        return self.account

    def setAcc(self, account):
        self.account = account

class Bank:

    customerDict = {}
    numOfCustomers = 0
    bankName = ""

    def __init__(self, bname):
        self.bankName = bname

    def getBankName(self):
        return self.bankName

    def addCustomer(self, firstname, lastname):
        self.customerDict.update({firstname + lastname : Customer(firstname, lastname)})
        self.numOfCustomers += 1

    def getNumOfCustomers(self):
        return self.numOfCustomers

    def getCustomer(self, custname):
        return self.customerDict.get(custname)


def main():

    bankNames = {}

    while True:
        bankStat = str(input("Do you have a bank? Y/N "))

        if bankStat.upper() == "N":
            print("Let's make a new bank >>> ")
            BName = str(input("What is the bank name? "))
            BVal = Bank(BName)
            bankNames.update({BName:BVal})
            print(bankNames)

        elif bankStat.upper() == "Y":

            nameOfBank = str(input("Insert the name of the bank: "))
            workBank = bankNames.get(nameOfBank)

            while True:
                if nameOfBank in bankNames:
                    print("\n"+"What would you like to do with the bank? ")
                    custStat = int(input("1: Get bank name 2: Get number of customers 3: Add a new Customer 4: Access customer menu 5: logout\n"))
                    if custStat == 1:
                        print(workBank.getBankName())
                    elif custStat == 2:
                        print(workBank.getNumOfCustomers())
                    elif custStat == 3:
                        workBank.addCustomer(str(input("Enter first name: ")), str(input("Enter last name: ")))
                        print("Customer Registered!")
                        print(workBank.getNumOfCustomers())
                    elif custStat == 4:
                        custName = str(input("What is the customer's name?"))

                        while True:
                            if custName in workBank.customerDict:
                                print("Logged in as " + custName)
                                print("What would you like to do?\n")
                                staCus = int(input("1: Get first name 2: Get last name 3: Account menu 4: Make account 5: Back to bank menu\n"))
                                if staCus == 1:
                                    print("The first name is "+ workBank.getCustomer(custName).getFirstName())
                                elif staCus == 2:
                                    print("The last name is " + workBank.getCustomer(custName).getLastName())
                                elif staCus == 3:
                                    print("Accessing account menu for " + custName)

                                    while True:
                                        staAcc = (int(input("What would you like to do with your account?\n1: Show balance 2: Deposit 3: Withdraw 4: Back to customer menu")))
                                        if staAcc == 1:
                                            print("You have a balance of: " + str(workBank.getCustomer(custName).getAccount().getBalance()))
                                        elif staAcc == 2:
                                            amount = int(input("How much would you like to deposit? "))
                                            workBank.getCustomer(custName).getAccount().deposit(amount)
                                            print("You now have a balance of: " + str(workBank.getCustomer(custName).getAccount().getBalance()))
                                        elif staAcc == 3:
                                            workBank.getCustomer(custName).getAccount().withdraw(int(input("How much would you like to withdraw? ")))
                                            print("You now have a balance of: " + str(workBank.getCustomer(custName).getAccount().getBalance()))
                                        elif staAcc == 4:
                                            print("Going back to customer menu: ")
                                            break

                                elif staCus == 4:
                                    workBank.getCustomer(custName).setAcc(Account(int(input("Enter initial balance: "))))
                                    print("Account created for "+custName+" with a balance of "+ str(workBank.getCustomer(custName).getAccount().getBalance()))
                                elif staCus == 5:
                                    print("Going back to Bank menu\n")
                                    break

                    elif custStat == 5:
                        print(nameOfBank + " logged out\n")
                        break
            else:
                print("Bank not found!")




    # bank1 = Bank("BCA")
    # print(bank1.getBankName())
    # bank1.addCustomer("Jovan","Jelek")
    # print(bank1.getCustomer("JovanJelek"))
    # bank1.getCustomer(str(input("Customer name? "))).setAcc(Account(100))
    # print(bank1.getCustomer("JovanJelek").getAccount().getBalance())


    # accNList = []
    # accNumber = 0
    # accList = []
    #
    # while True:
    #     state = ""
    #     state1 = str(input("Do you have an account? Y/N "))
    #
    #     if state1.upper() == "N":
    #         state = str(input("Would you like to make a new account? Y/N "))
    #
    #     if state.upper() == "Y":
    #         accName = input("Insert account name: ")
    #         accList.append(accName)
    #         accNList.append(accName)
    #         accList[accNumber] = Account(int(input("Deposit initial balance: ")))
    #         print("Your account name is " + accName + " and your account number is: " + str(accNumber) + "\nWith a balance of " + str(accList[accNumber].balance)+"\n\n")
    #         accNumber += 1
    #
    #     elif state.upper() == "N" or state1.upper() == "Y":
    #
    #         workAcc = int(input("What is your acc number? "))
    #         print("\nYou are logged in as: " + str(accNList[workAcc]) + "\n")
    #         operation = int(input("What would you like to do? (1: deposit, 2: withdraw, 3: display account, 4: exit) "))
    #
    #
    #         if operation == 1:
    #             accList[workAcc].deposit(int(input("What is the amount: ")))
    #             print("Your account now has " + str(accList[workAcc].balance+"\n\n"))
    #         elif operation == 2:
    #             accList[workAcc].withdraw(int(input("What is the amount: ")))
    #             print("Your account now has " + str(accList[workAcc].balance)+"\n\n")
    #         elif operation == 3:
    #             print("Your account name is "+ str(accNList[workAcc]) +". Your account balance is: " + str(accList[workAcc].balance)+"\n\n")
    #         elif operation == 4:
    #             print("\nProgram Terminated\n")

main()
