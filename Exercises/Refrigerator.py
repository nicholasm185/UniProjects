top = {}
mid = {}
bot = {}
space = 10
while True:
    status = str(input("Would you like to use the fridge? Y/N "))
    if status.upper() == "Y":
        Cont = str(input("which shelf ,(top,mid,bot)"))

        if Cont.lower() == "top":
            content = str(input("add something? "))
            takeOrNot = str(input("remove or add"))
            change = int(input("How many? "))
            takeOrNot = takeOrNot.strip()

            if takeOrNot == "remove":
                change = 0 - change

            itemValue = top.get(content,0)+ change
            chkCont = sum(top.values())+ change

            if chkCont > 10:
                print("DOESNT FIT DUMBASS")
            elif itemValue < 0:
                print("TANGGAL TUA, BODAT")
            else:
                top.update({content : itemValue})

            print(top)

        if Cont.lower() == "mid":
            content = str(input("add something? "))
            takeOrNot = str(input("remove or add"))
            change = int(input("How many? "))
            takeOrNot = takeOrNot.strip()

            if takeOrNot == "remove":
                change = 0 - change

            itemValue = mid.get(content, 0) + change
            chkCont = sum(mid.values()) + change

            if chkCont > 10:
                print("DOESNT FIT DUMBASS")
            elif itemValue < 0:
                print("TANGGAL TUA, BODAT")
            else:
                mid.update({content: itemValue})

            print(mid)

        if Cont.lower() == "bot":
            content = str(input("add something? "))
            takeOrNot = str(input("remove or add"))
            change = int(input("How many? "))
            takeOrNot = takeOrNot.strip()

            if takeOrNot == "remove":
                change = 0 - change

            itemValue = bot.get(content, 0) + change
            chkCont = sum(bot.values()) + change

            if chkCont > 10:
                print("DOESNT FIT DUMBASS")
            elif itemValue < 0:
                print("TANGGAL TUA, BODAT")
            else:
                bot.update({content: itemValue})

            print(bot)

    elif status.upper() == "N":
        break
