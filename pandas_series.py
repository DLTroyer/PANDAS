import pandas as pd

grades = pd.Series([87,100,94])

#print(grades)

my_array = pd.Series(98.6, range(3))

#print(my_array)

print(grades[0])

print(grades.describe())

hardware = pd.Series(['Hammer','Saw','Wrench'])

a = hardware.str.contains('a')

print(a)

b = hardware.str.upper()

print(b)