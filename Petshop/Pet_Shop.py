class petShop:

    balance = 0
    pets = {}

    def __init__(self, balance):
        self.balance = balance


    def deposit(self,amount):
        self.balance += amount
        print("Transaction successful")

    def buyPets(self, pet, price):
        self.balance -= price
        self.pets.update({pet:price})


    def sellPets(self, petName):
        amount = self.pets.get(petName)
        self.balance += amount
        del self.pets[petName]
        print("Pet sold!")

def main():

    petshopdic = {}
    pets = {"Chihuahua":200, "Pitbull":400, "Akita":1000, "Bat": 100, "Turtle":75}

    while True:
        status = str(input("Do you have a pet shop? Y/N or exit "))
        if status.upper() == "N":
            print("\nLets make a new pet shop!")
            pshopName = str(input("Insert your pet shop name: "))
            petShopper = petShop(int(input("Insert initial balance: ")))
            petshopdic.update({pshopName:petShopper})
            print("New pet shop created!\n")
            # print(petshopdic)

        if status.upper() == "Y":
            nameShop = str(input("What is your pet shop's name? "))
            shopname = petshopdic.get(nameShop)

            while True:
                if nameShop in petshopdic:
                    petdo = int(input("\nWhat would you like to do?\n1: Sell Pets 2: Buy Pets 3: Deposit money 4: View Inventory 5: Exit shop "))

                    if petdo == 1:
                        print(shopname.pets)
                        petname = str(input("Which pet in the inventory would you like to sell? "))
                        if petname not in shopname.pets:
                            print("You don't have that pet!")
                        else:
                            shopname.sellPets(petname)

                    elif petdo == 2:
                        print("You can currently buy:")
                        print(pets)
                        whatbuy = str(input("What would you like to buy? "))
                        if whatbuy in shopname.pets:
                            print("You already have that in your inventory, please choose another pet!")
                        elif pets.get(whatbuy) > shopname.balance:
                            print("Insufficient balance! Please deposit more to buy more pets!")
                        else:
                            shopname.buyPets(whatbuy,pets.get(whatbuy))
                            print("You now have a balance of: " + str(shopname.balance))

                    elif petdo == 3:
                        shopname.deposit(int(input("How much would you like to invest? ")))
                        print("Your pet shop now has a balance of: " + str(shopname.balance))

                    elif petdo == 4:
                        print("In your inventory, you have: ")
                        print(shopname.pets)
                        print("And a balance of: "+ str(shopname.balance))

                    elif petdo == 5:
                        print("Thank you, please come again to the " + nameShop + " pet shop!\n\n")
                        break

                else:
                    print("Shop doesnt exit! Please make a new one or choose from existing shops!")
                    break

        elif status.upper() == "EXIT":
            print("Thank you for using the Pet Shop simulator!")
            break

main()
