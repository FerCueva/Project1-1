import os
import filecmp
#extra credit
#from dateutil.relativedelta import *
#from datetime import date

def getData(file):
# get a list of dictionary objects from the file 
#Input: file name        
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows
        inFile = open(file,"r")
        lines = inFile.readlines()
        inFile.close()

        dicList = []

        for line in lines:
                
                pollDict = {}
                #split values ar "," and get the values
                values =  line.split(",")
                first = values[0]
                last = values[1]
                email = values[2]
                class_year = values[3]
                dob = values[4]

                pollDict["First"] = first
                pollDict["Last"] = last
                pollDict["Email"] = email
                pollDict["Class"] = class_year
                pollDict["DOB"] = dob
                dicList.append(pollDict)
        return dicList

def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName
        sortedList = sorted(data, key=lambda k: k[col]) 
        for i in range (1):
                curr = sortedList[i]
                return(curr["First"] + " " + curr["Last"])


def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

        classSizes_List = []
        senior_counter =  0
        junior_counter = 0
        sophomore_counter = 0
        freshman_counter = 0

        for i in data:
                if i["Class"] == "Senior":
                        senior_counter += 1
                        
                if i["Class"] == "Junior":
                        junior_counter += 1

                if i["Class"] == "Sophomore":
                        sophomore_counter += 1

                if i["Class"] == "Freshman":
                        freshman_counter += 1
                        
        classSizes_List.append(("Senior", senior_counter))
        classSizes_List.append(("Junior", junior_counter))
        classSizes_List.append(("Sophomore", sophomore_counter))
        classSizes_List.append(("Freshman", freshman_counter))
        return sorted(classSizes_List, key = lambda k: k[1], reverse = True)

                





mySort(getData("P1DataA.csv"), "First")
classSizes(getData("P1DataA.csv"))

################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()

mySort(getData("P1DataA.csv"), "First")
