import os
import filecmp
from datetime import date, datetime

def getData(file):
# get a list of dictionary objects from the file 
#Input: file name        
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows
        inFile = open(file,"r")
        next(inFile)
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

def findMonth(a):
#Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data

        birthMonth_List = {}

        for i in a:
                if i["DOB"].split("/")[0] in birthMonth_List:
                        birthMonth_List[i["DOB"].split("/")[0]] += 1

                elif i["DOB"].split("/")[0] not in birthMonth_List:
                        
                        birthMonth_List[i["DOB"].split("/")[0]] = 1

        sorted_birthMonth_List = sorted(birthMonth_List.items(), key = lambda k: k[1], reverse = True)
        return(int(sorted_birthMonth_List[0][0]))                                       
                        

def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as first,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written
        outFile = open(str(fileName),"w")

        sorted_Data = sorted(a, key = lambda k:k[str(col)])

        for data in sorted_Data:
                
                first = data["First"]
                last = data["Last"]
                email = data["Email"]
                outFile.write(first + "," + last + "," + email + "\n")
                
        outFile.close()
        
def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.
        ages_list = []

        now = datetime.now()
        
        for student in a:
                age = abs(int(now.year) - int(student["DOB"].split("/")[2]))
                ages_list.append(age)

        average_age = (int(sum(ages_list)/len(ages_list)))
                       
        return average_age
                        

        

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

