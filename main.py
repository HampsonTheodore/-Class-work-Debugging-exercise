# In this exercise, I am going to debug each line of code and explain whhats wrong with it.

#Code 1
#1. What's your Name?
#This program should ask for the user's name, then display "Hello {user's name goes here}"

input("Enter your name: ")
print(f"Hello {myName}")

# What types of errors did this program suffer from?

#NameError, did not define the 'myName' variable. 
   # Need to store the input into a variable so I can call it out in a print statement f string


   #The correct code
   
myName =input("Enter your name: ")

print(f"Hello {myName}")

# code 2
#Counting to 100
#This program should display the numbers from 1 to 100

for number in range(1, 101)
  print(number)

  # What types of errors did this program suffer from?
# Syntax Error, forgot to add the colon after the for loop ()

#The correct code 
#for number in range(1, 101):
  print(number)

#code 3 
#Shuffling the Deck

#This program should shuffle a deck of cards and randomly deal a "hand" to the player

myDeck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

random.shuffle(myDeck)
myHand = myDeck[0 : 5]

print(myHand)

# What types of errors did this program suffer from?
#NameError, need to define random varaible by importing the random module and its method called shuffle

# The correct code

from random import shuffle

myDeck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

shuffle(myDeck)
myHand = myDeck[0 : 5]

print(myHand)

#Code 4
#Odd One Out
#This program should successfully determine if the number passed in is even or odd

setCorrectly = False
while not setCorrectly:
  try:
    myNumber = int(input("Enter a number: "))
    setCorrectly = True
  except:
    print("Please enter a valid number")

remainder = myNumber % 2

if(remainder == 1):
    print("Your number is even!")
else:
    print("Your number is odd!")

    # What types of errors did this program suffer from?

# The code runs but it is a logical error. Something in the code isn't correct. 
   # For line 13 we need to set the if statement remainder parameter to 0 to be even

   # The correct code

setCorrectly = False
while not setCorrectly:
  try:
    myNumber = int(input("Enter a number: "))
    setCorrectly = True
  except:
    print("Please enter a valid number")

remainder = myNumber % 2

if(remainder == 0):
    print("Your number is even!")
else:
    print("Your number is odd!")

#code 5
#Born to Drive
#This program looks at your age and determines your eligibility for voting and a driver's license. Use the comments to help make sure that the program is working properly.

def getInteger(msg):
    text = "a"
    while(not text.isdigit()):
        text = input(msg)
    return int(text)

myAge = getInteger("Enter your age: ")

# If you are 18 or older, let the user know that they are allowed to vote and get a license!
if(myAge >= 18):
    print("You are allowed to get a license and vote!")

# If they are younger than 18, but older than 15, then they can get a license but NOT vote
elif(myAge < 18 or myAge > 5):
    print("You are allowed to get a license but not vote.")

# Otherwise, they can't do either
else:
    print("You are not allowed to get a license or vote.")

    What types of errors did this program suffer from?
#The code runs but this is a logical error. 
# On line 15 the second parameter in the elif should be set to 15 and not 5

# The correct code

def getInteger(msg):
    text = "a"
    while(not text.isdigit()):
        text = input(msg)
    return int(text)

myAge = getInteger("Enter your age: ")

# If you are 18 or older, let the user know that they are allowed to vote and get a license!
if(myAge >= 18):
    print("You are allowed to get a license and vote!")

# If they are younger than 18, but older than 15, then they can get a license but NOT vote
elif( 15 < myAge < 18):
    print("You are allowed to get a license but not vote.")

# Otherwise, they can't do either
else:
    print("You are not allowed to get a license or vote.")

    #code 6
    #Pairing Up Pets
#This program should ask the user for three pairs of pets and owners, store them in a collection, then loop through and display each one.

pairs = {}

for i in range(0, 3):
  name = input("Enter the owner's name: ")
  pet = input("Enter the pet's name: ")
  
  pairs.append(name, pet)

for key, value in pairs.items():
  print(f"Owner: {key}, Pet's Name: {value}")

  # What types of errors did this program suffer from?
#Attribute Error, the dictionary object has no attribute for append (line 8). Changed the formatting of line 8 for a dictionary 

#The correct code

pairs = {}

for i in range(0, 3):
  name = input("Enter the owner's name: ")
  pet = input("Enter the pet's name: ")

  pairs[name] = pet

for key, value in pairs.items():
  print(f"Owner: {key}, Pet's Name: {value}")

#Code 7
#Keeping Score
#This function is supposed to take in a grade as a number and display the corresponding letter grade. For example, a 92 should display an "A", and a 73 should display a "C"

#You will need to write some code to test the function.

def printGrade(grade):
    if(myGrade > 90):
        print("A")
    if(myGrade > 80):
        print("B")
    if(myGrade > 70):
        print("C")
    else:
        print("Failed")

        # What types of errors did this program suffer from?
# The code did not run because there was no code outside of the defined function. Needs elif and >= in the defintion of the function.

# The correct code

def printGrade(grade):
    if(myGrade >= 90):
        print("A")
    elif(myGrade >= 80):
        print("B")
    elif(myGrade >= 70):
        print("C")
    else:
        print("Failed")

# This is for user to input the grade
myGrade = int(input("Enter a grade: "))

# This uses the function to print out the letter grade
printGrade(myGrade)

#Code 8
#Maxing it Out
#This function is supposed to take in a list of numbers and return the largest number in the list

#ou will need to write some code to test the function.

# Finds the maximum number in a list


# defintion of function needed : after ()
# remove the equals in the if statement and flip the sign from > to <
def findMax(param):
  largest = numbers[0]
  for number in numbers:
    if(largest < number):
      largest = number
  return largest

numbers = [1 , 6, 26, 40, 29, 77, 10]

max = findMax(numbers)

print(f"This is the largest number in the list: {max}")

#Code 9
#Time Trials
#This program is supposed to take in a month as a number (1 = January, 4 = April, etc.) and tell you how many months are left in the year (give or take)

numberMonth = 0
while(numberMonth < 1 and numberMonth > 12):
    currentMonth = input("Enter the current month (as a number, 1-12): ")
    if(currentMonth.isdigit()):
        numberMonth = int(currentMonth)

monthsLeft = 12 - currentMonth
print("There are", numberMonth, "more months left in the year!")

# What types of errors did this program suffer from?
# NameError, the currentMonth variable is not defined 

# The correct code

numberMonth = 0

# made this variable take in an integer, put this variable outside the while loop
currentMonth = int(input("Enter the current month (as a number, 1-12): "))

while(numberMonth < 1 and numberMonth > 12):
  if(currentMonth.isdigit()):
      numberMonth = int(currentMonth)

# made an f string with the variable monthsLeft instead of numberMonth
monthsLeft = 12 - currentMonth
print(f"There are {monthsLeft} more months left in the year!")


