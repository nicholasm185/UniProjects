import datetime as dt
def findMiddle(input_list):
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return round((input_list[int(middle)] + input_list[int(middle-1)])/2)

def isweekend(weekno):
    weekno = dt.datetime.strptime(weekno, "%Y-%m-%d")
    day = weekno.weekday()
    if day < 5:
        return "Weekday"
    else:
        return "Weekend"

def getnumberdays(days, state):
    counter = 0
    if state == "Weekdays":
        for i in range(0, len(days)):
            if isweekend(days[i]) == "Weekday":
                counter +=1
    elif state == "Weekends":
        for i in range(0, len(days)):
            if isweekend((days[i])) == "Weekend":
                counter += 1
    return counter
