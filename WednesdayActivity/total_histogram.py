import csv
import pygal
from useful_functions import findMiddle

filename = ".\\activity.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    steps = []
    days = []
    intervals = []
    missingno = 0

    for row in reader:
        step = row[0]
        day = row[1]
        # NA is assumed to be no data or 0 steps
        if step == "NA":
            steps.append(0)
            days.append(row[1])
            intervals.append(row[2])
            missingno += 1
            continue
        else:
            steps.append(int(step))
            days.append((row[1]))
            intervals.append(row[2])

    # gets the number of days
    numdays = [i for i in range(len(set(days)))]

    # set lists needed for the loop
    day_tot = []
    summer = []
    daychk = days[0]
    meaner = []
    for data in range(0, len(steps)):
        currentday = days[data]
        if daychk == currentday:
            summer.append(steps[data])
        else:
            day_tot.append(sum(summer))
            meaner.append(sum(summer)/len(set(days)))
            summer = []
            summer.append(steps[data])
        daychk = currentday

    # add the last day's steps
    day_tot.append(sum(summer))
    meaner.append(sum(summer)/len(set(days)))

#
hist = pygal.Bar()

hist.title = "Total steps per day"
hist.x_label = str(set(days))
hist.y_title = "Number of steps"
hist.add("Set1", day_tot)

hist.render_to_file("Total_Steps_per_Day.svg")

# gets the median from the daily totals
median = findMiddle(sorted(day_tot))

print("The mean of the total number of steps taken is " + str(round(sum(meaner))) + " steps")
print("The median of the total number of stesp taken is " + str(median) + " steps")
print("There are " + str(missingno) + " missing data")
