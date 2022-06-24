
"""
source: https://www.youtube.com/watch?v=rfscVS0vtbw

#ex1 printing text
print("hello world!")
print("\n")

#ex2 drawing
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
print("\n")

#ex3 variables
character_name = "Tom"
character_age = "50.5678213" #what ever value you want
is_Male = False

print("There once was a man named " + character_name +",")
print("he was " + character_age + " years old.\n")

character_name = "Mike" #updated variable
print("He really liked the name " + character_name + ",")
print("but didn't like being " + character_age + ".\n")
print ("\n")

#ex4 working with strings
print("Giraffe\nAcademy") #enter within line
phrase = "Giraffe Academy"
print(phrase + " is cool") #concatination (add variable to text in this example)

print(phrase.lower()) #print in lower case
print(phrase.upper()) #print in upper case

print(phrase.isupper()) #see if string is in upper or lower case
print(phrase.upper().isupper()) #set to uppercase and print if its true
print(len(phrase)) #give length of string
print(phrase[0]) #print first letter of string
print(phrase.index("r")) #passing parameter (gives location of number)
print(phrase.replace("Giraffe", "Elephant")) #replace function
print ("\n")

#ex5 numbers
from math import *      #math library
print(2) #print number
print(-2.0987) #python prints this perfectly fine
print(3/ 4.5) #math
print (3 * (4 + 5)) # parentheses makes order
print (10 % 3) #(10 mod 3) 10/3 with the remainder of 1

my_num = -5
print(str(my_num) + " is my favorite number") # converts number to string
print(abs(my_num)) # absolute value of my_num
print(pow(3,2)) # first number to the power of the second number
print(max(6,4)) # return largest number
print(min(3,8)) # return smallest number
print(round(3.7)) # round a number
print(floor(3.7)) # grab lowest number, chops of decimal number
print(ceil(3.7)) # grab highest number, rounds up, no mather what.
print(sqrt(64)) # gets square root of number
print("\n")

#ex6 input from user
name = input("Enter your name: ")
age = input("Enter your age': ")
print("Hello " + name + "!")
print("You are " + age + " years old!")
print("\n")

#ex7 building a basic calculator
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2) # transform to floating numbers
print(result)
print("\n")

#ex8 mad libs game
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")
print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)
print("\n")

#ex9 Lists
friends = ["Kevin", "Karen", "Jim", "John", "Luca"] #list, can also be boolean or numbers
friends [1] = "Mike" #changing value of list
print(friends)
print(friends[-1]) #basicly a pointer to the x-st item in the list. with negatives, you start at the back of the list.
print(friends[1:3]) #select x up to y
print("\n")

#ex10 List functions
lucky_numbers = [4, 8, 15, 16, 23, 42, 19, 44, 29]
friends = ["Kevin", "Karen", "Jim", "John", "Luca", "Luca"] #list, can also be boolean or numbers
friends.extend(lucky_numbers)   #add to list
friends.append("Peter") # add a single item, append always adds item to end of the list
friends.insert(1, "Kelly") # add a new item to the location of X
friends.remove("Jim") # remove X from the list
#friends.clear() # empty the whole list
friends.pop() # pops last item of the list, removes last item
friends.sort() # puts list in alphabetical order, also works for numbers
friends.reverse() #reverses list

print(friends.index("Luca")) # searches for X in the list and gives the index of X
print(friends.count("Luca")) # shows how many times X is in the list
friends2 = friends.copy() # list 2 copies values of original list
print("\n")

#ex11 Tuples

tuples: a container wherein we can store different values.
key differences from list: tuples not mutable, cannot be changed,removed or anything, what you see is what you get.
coordinates[1] = 1 <- cannot be done, since tuples values cannot be changed ever
tuples is for data that is never going to change
"""
"""
coordinates = (4, 5)
print(coordinates[0])  # prints out index x
"""

"""
# ex12 Functions
def say_hi(name, age): # function declaration
    print("Hello " + name + ",you are: " + str(age) + " years old")

say_hi("Mike", 25) # function is being called
say_hi("Steve", 12)
print("\n")
# parameter: piece of information given to the function


# ex13 Return statements
def cube(num):
    return num*num*num  # gives num cubed and breaks out of function, all code after line this won't be executed


result = cube(4)  # stores value that gets returned from the function
print(cube(result))
print("\n")

# ex14 if statements
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not is_tall:
    print("You are a short male")
elif not is_male and is_tall:
    print("You are not a male, but you are tall")
else:
    print("You are not a male and not tall")
    print("\n")

# ex15 if statements and comparisons
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print("num1 is the largest number")
        return num1
    elif num2 >= num1 and num2 >= num3:
        print("num2 is the largest number")
        return num2
    elif num3 >= num1 and num3 >= num2:
        print("num3 is the largest number")
        return num3


print (max_num(300, 40, 5))


#ex16 Building a better calculator
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))\

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")
    print("\n")
    
#ex17 Dictionaries
#jan -> January
#mar -> march
monthConversions = {  # basically a lookup table for short words to longer words
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Okt": "October",
    "Nov": "November",
    "Dec": "December"
    1: "January",
    2: "February"

}

print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Luv", "not a valid key"))  # print second parameter if first isn't found in dictionary

print("\n")

#ex18 While loops
i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")
print("\n")

#ex19
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True


if out_of_guesses:
    print("Out of guesses, you loose!")
else:
    print("You win!")
print("\n")


#ex20 For loops
for letter in "Giraffe Academy":
    print(letter)

friends = ["Jim", "Karen", "Kevin"]
for name in friends:
    print(name)
    len(friends)  # get length of the array

for index in range(3, 10):  # print range of number 3-10
    print(index)

for index in range(5):  # print range of number 3-10
    if index == 0:
        print("first Iteration")
    else:
        print("Not first Iteration")
print("\n")

#ex21 Exponent functions
print(2**3) # this works
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num

print(raise_to_power(2, 3))
print("\n")       

#ex22 2D lists & nested loops
number_grid = [
    [1,2,3], # row 0
    [4,5,6],
    [7,8,9],
    [0]     # row 3
]

print(number_grid[2][1])  # print row x, colom x

for row in number_grid:
    print (row) # print all rows

for row in number_grid:
    for col in row:  # print all values in the number grid
        print(col)
print("\n")    

#ex23 build a translator
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase ")))  # print out the translation of whatever the user puts in
print("\n")  

#ex24 Comments
print("comments are fun")
# this program is cool
# print("text") # comment out text

#
#let's tell a long story...
#I can easily write multiple comments
#but # is preferred by Python users
#

print("\n")  


#ex25 Try / Except
# you want to be able to handle (human) error
try:
    # answer = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err: # best practice is to use specific errors, don't throw everything under one single except
    print(err)
except ValueError:
    print("Invalid input")
print("\n")


#ex26 Reading Files
"""  # end of disabled code
# open("employees.txt", "r")  # open file and only read information
# open("employees.txt", "w")  # open file and only write information
# open("employees.txt", "a")  # open file and only add extra data to the end of the file
# open("employees.txt", "r+")  # open file and read/write to it

employee_file = open("employees.txt", "r")
#print(employee_file.readable())  # check if the file can be read (we set it to "r")
print(employee_file.readline())  # read all info on file
employee_file.close()
