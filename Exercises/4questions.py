# number 1
def hapax(directory):
    book = open(directory)
    content = book.read().lower().split()
    print(content)
    hapaxes = []
    for i in range(0, len(content)):
        if content.count(content[i]) == 1:
            hapaxes.append(content[i])
    print(hapaxes)

# number 2
def nlines(directory):
    tfile = open(directory)
    tlist = tfile.read().splitlines()
    # print(tlist)
    open("C:\\Users\\Nicholas\\OneDrive\\Assignments\\newfile.txt","w+")
    newfile = open("C:\\Users\\Nicholas\\OneDrive\\Assignments\\newfile.txt","w")
    for i in range(0, len(tlist)):
        content = str(str(i+1)+ " "+ tlist[i])
        newfile.write(content+"\n")
        # print(tlist[i])

# number 3
def avgCalc(directory):
    tfile = open(directory)
    tlist = tfile.read().split()
    summer = []
    for i in range(0, len(tlist)):
        summer.append(len(tlist[i]))
    print("Average word length is: "+ str((sum(summer)/(len(tlist)))))

# number 4
def sentSplitter(directory):
    test = open(directory)
    sentence = str(test.read())
    sentence = (sentence + " ")
    start = 0
    punctuation = [".", "!", "?"]
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    titles = ["Mr.","Mrs.","Jr.","Dr."]
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                "u", "v", "w", "x", "y", "z"]
    for i in range(0, len(sentence)-1):
        if sentence[i] == "." and sentence[i+1] in numbers:
            continue
        elif sentence[i-1] in alphabet and sentence[i-2] == ".":
            continue
        elif sentence[i-2:i+1] in titles or sentence[i-3:i+1] in titles:
            continue
        elif sentence[i] == "." and sentence[i+1] in alphabet:
            continue
        elif sentence[i] == "." and sentence[i+1] in punctuation:
            continue
        elif sentence[i] in punctuation:
            print(sentence[start: i+1])
            start = i+2


# hapax("C:\\Users\\Nicholas\\OneDrive\\Assignments\\testfile.txt")
# nlines("C:\\Users\\Nicholas\\OneDrive\\Assignments\\testfile.txt")
# avgCalc("C:\\Users\\Nicholas\\OneDrive\\Assignments\\The King Behind the King.txt")
# sentSplitter("C:\\Users\\Nicholas\\OneDrive\\Assignments\\testfile.txt")
