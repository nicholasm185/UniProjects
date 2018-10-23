import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "C:\\Users\\Nicholas\\OneDrive\\Recources\\Program Design Methods\\death_valley_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing data")
        else:
            highs.append(int(high))
            lows.append(int(low))
            dates.append(current_date)

    print(highs)

fig = plt.figure(dpi = 128, figsize=(10,6))
plt.plot(dates, highs, "--", c = "red", alpha = 0.5)
plt.plot(dates, lows, "--", c = "blue", alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = "grey", alpha = 0.3)

plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA", fontsize = 20)
plt.xlabel("", fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = "both", which = "major", labelsize = 14)

plt.show()


