import pandas as pd

grades_dict = {'Wally':[87,96,70],'Eva':[100,87,90], 'Sam':[94,77,90], 'Katie':[100,81,82], 'Bob': [83,65,85]}

grades = pd.DataFrame(grades_dict)

grades.index = ['Test1','Test2','Test3']


#print out sams grades
#print(grades.Sam)


#these two are the same thing
#the colon would be Test1-3, replace the colon with a "," and make it a list within a list to get just test1 and test3
#print(grades.loc['Test1':'Test3'])

#print(grades.iloc[0:2])


#just kaite and ava
##print(grades.loc[['Test1','Test3'],['Eva','Katie']])

#print(grades.iloc[[0,1],[1,3]])

print(grades)

#prints all of the grades that are greater than 90
#print(grades[grades>90])

print(grades[(grades>= 80) & (grades < 90)])

#perminately changes eva's grade for test2 
grades.at['Test2','Eva'] = 100

#goes straight to location in array
#print(grades.at['Test2','Eva'])

#print(grades)

#same thing as above but using locations
#print(grades.iat[1,2])

#grades.iat[1,2] = 87

#print(grades)

#This is a fast way to show you some of the sats of the data frame
#print(grades.describe())

#makes the output of the desccribe to only 2 decimal places
#pd.set_option('precision',2)

#print(grades.describe())

#just tell us the mean for each student
#print(grades.mean())

#finds the mean of the tests
#print(grades.T.mean())

#arrange the tests
#print(grades.sort_index(ascending=False)

#arrange the people
#axis 1 = column, 0 = row
#rint(grades.sort_index(axis=1))


print(grades.sort_values(by='Test1',axis=1,ascending=False))

print(grades.T.sort_values(by='Test1', ascending = False))

print(grades.loc['Test1'].sort_values(ascending=False))

