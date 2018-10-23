from die import Die
import pygal

die1 = Die()
die2 = Die(10)

results = []
roll_num = int(input("How many rolls? "))

for roll_num in range(roll_num):
    results.append(die1.roll()+die2.roll())

print(results)

frequency = []
frequencies = []
for dieside in range(2, die1.numSides+die2.numSides+1):
    frequency = results.count(dieside)
    frequencies.append(frequency)

print(frequencies)

hist = pygal.Bar()

hist.title = "Results of rolling D6 and D10 " + str(roll_num+1) + " times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
'13', '14', '15', '16']
hist.y_title = "frequency"
hist.add("D6 + D6", frequencies)
hist.render_to_file("dievisual.svg")
