import csv
import matplotlib.pyplot as plt
import useful_functions

filename = ".\\activity.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    steps = []
    days = []
    intervals = []

    for row in reader:
        step = row[0]
        day = row[1]
        # NA is assumed to be no data or 0 steps
        if step == "NA":
            steps.append(0)
            days.append(row[1])
            intervals.append(int(row[2]))
        else:
            steps.append(int(step))
            days.append((row[1]))
            intervals.append(int(row[2]))

# remove duplicates and turn back into list
wrkdays = set(days)
wrkdays = list(wrkdays)

# gets the number of days for weekends and weekdays
weekends = useful_functions.getnumberdays(wrkdays, "Weekends")
weekdays = useful_functions.getnumberdays(wrkdays, "Weekdays")

averages = []
wkndaverages = []
gIntervals = [i for i in range(0, 2356, 5)]
counter = 1

for i in range(0, 2356, 5):
    # finds the indexes for each 5 minute intervals
    indexes = [k for k, x in enumerate(intervals) if x == i]
    # print(i)
    # print(indexes)
    values = 0
    valueswknd = 0
    for j in range(0, len(indexes)):
        if useful_functions.isweekend(days[indexes[j]]) == "Weekday":
            values += steps[indexes[j]]
        elif useful_functions.isweekend(days[indexes[j]]) == "Weekend":
            valueswknd += steps[indexes[j]]
    values = values/weekdays
    valueswknd = valueswknd/weekends
    averages.append(values)
    wkndaverages.append(valueswknd)
    counter += 1

print("The maximum average steps is " + str(int(max(averages))) + " at the interval " + str(averages.index(max(averages))*5) + " minutes for weekdays")
print("The maximum average steps is " + str(int(max(wkndaverages))) + " at the interval " + str(wkndaverages.index(max(wkndaverages))*5) + " minutes for weekends")

weekday = plt.plot(gIntervals, averages, c = "red")
weekend = plt.plot(gIntervals, wkndaverages, c = "blue")
plt.ylabel("Number of steps")
plt.xlabel("Minutes")
plt.legend(["Weekday average", "Weekend average"])
plt.show()
