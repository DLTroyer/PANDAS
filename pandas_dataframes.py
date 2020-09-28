import pandas as pd

grades_dict = {'Wally':[87,96,70],'Eva':[100,87,90], 'Sam':[94,77,90], 'Katie':[100,81,82], 'Bob': [83,65,85]}

grades = pd.DataFrame(grades_dict)

grades.index = ['Test1','Test2','Test3']

print(grades)

#print out sams grades
#print(grades.Sam)


#these two are the same thing
#the colon would be Test1-3, replace the colon with a "," and make it a list within a list to get just test1 and test3
print(grades.loc['Test1':'Test3'])

print(grades.iloc[0:2])


#just kaite and ava
print(grades.loc[['Test1','Test3'],['Eva','Katie']])

print(grades.iloc[[0,1],[1,3]])

