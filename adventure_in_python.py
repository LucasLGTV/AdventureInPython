##############################################
#------------Adventures in Python------------#
##############################################

#-------------->MODULES
# Modules are extra bits of code you can import and use to save you time
import random
import time

#-------------->VARIABLES
# Variables are a way of storing data/values that you can use later in your code
# You assign the value on the right of the = to the value on the left and then use
# the value on the left in your code.

# With these variables we assign values that we can use later in the code.
# Try changing the myName value to your name and see what happens 
space = "\n\n"
myName = "Rob Gray"

#-------------->ARRAYS
# Arrays are the same as variables but differ in that they allow you to store 
# a list of data/values that you can later access in your code.
# Here we store a list of items in our backpack to help us escape the cave.
inventory = ["Torch", "Pencil", "Rubber Band", "Catapult", "Rope", "Knife", "Matches"]

# print the name of the game appended with the variable assigned with your name.
print ("Welcome to Escape The Cave by " + myName + "\n")
print ("------------------------------------------" + space)

# we begin the story
print ("You awake in total darkness with nothing but your backpack..." + space)
print ("...you decide to arm yourself with a " + space)

# here we use that time module and a function/method to tell our code to wait a few seconds
# wait for 2 seconds
time.sleep(2)

# here we create a variable called item to store the input from the console
item = input("Think of an object and type it in...\n")

# print a sentance with the input variable at the end
print ("You look in your backpack for a ", item)

# wait 2 seconds
time.sleep(2)

# print some more of the story
print ("You could not find the ", item)
print ("You select any item that comes to hand from the backpack instead" + space)

# wait 3 seconds
time.sleep(3)

# here we use the random module to randomly select an item from your 
# inventory array/list
print(random.choice(inventory))

# question
action = input("You encounter an enemy what do you do?\n")

# response
print ("You bravely ", action)

# wait 3 seconds
time.sleep(3)

# question
action = input("You encounter a person what do you do?\n")

# response
print ("You", action)

time.sleep(3)

# questions
print ("Choose what you want to say?\n\n")
print ("1 = Hello how are you\n")
print ("2 = What are you doing here this is my cave\n")
print ("3 = Plese go away\n\n")

action = input("Enter 1, 2 or 3\n")

# responses if someValue == "someOtherValue" : thenDoSomething()
if action == "1" : print ("I'm fine how are you\n")
elif action == "2" : print ("I'm lost how about you\n")
elif action == "3" : print ("Ok i'm sorry to have bothered you\n")
else: print ("You do something crazy...la la la la!!")


##############################################
#------------Adventures in Python------------#
##############################################

#-------------->MODULES
# Modules are extra bits of code you can import and use to save you time
import random
import time

#-------------->VARIABLES
# Variables are a way of storing data/values that you can use later in your code
# You assign the value on the right of the = to the value on the left and then use
# the value on the left in your code.

# With these variables we assign values that we can use later in the code.
# Try changing the myName value to your name and see what happens 
space = "\n\n"
myName = "Rob Gray"

#-------------->ARRAYS
# Arrays are the same as variables but differ in that they allow you to store 
# a list of data/values that you can later access in your code.
# Here we store a list of items in our backpack to help us escape the cave.
inventory = ["Torch", "Pencil", "Rubber Band", "Catapult", "Rope", "Knife", "Matches"]

# print the name of the game appended with the variable assigned with your name.
print ("Welcome to Escape The Cave by " + myName + "\n")
print ("------------------------------------------" + space)

# we begin the story
print ("You awake in total darkness with nothing but your backpack..." + space)
print ("...you decide to arm yourself with a " + space)

# here we use that time module and a function/method to tell our code to wait a few seconds
# wait for 2 seconds
time.sleep(2)

# here we create a variable called item to store the input from the console
item = input("Think of an object and type it in...\n")

# print a sentance with the input variable at the end
print ("You look in your backpack for a ", item)

# wait 2 seconds
time.sleep(2)

# print some more of the story
print ("You could not find the ", item)
print ("You select any item that comes to hand from the backpack instead" + space)

# wait 3 seconds
time.sleep(3)

# here we use the random module to randomly select an item from your 
# inventory array/list
print(random.choice(inventory))

# question
action = input("You encounter an enemy what do you do?\n")

# response
print ("You bravely ", action)

# wait 3 seconds
time.sleep(3)

# question
action = input("You encounter a person what do you do?\n")

# response
print ("You", action)

time.sleep(3)

# questions
print ("Choose what you want to say?\n\n")
print ("1 = Hello how are you\n")
print ("2 = What are you doing here this is my cave\n")
print ("3 = Plese go away\n\n")

action = input("Enter 1, 2 or 3\n")

# Conditional logic allows you to perform different actions depending on a
# specific condition being met. Note because we already use = for assignment 
# we need to use double equals for equality.

# if someValue == "someOtherValue" : thenDoSomething()
if action == "1" : print ("I'm fine how are you\n")
elif action == "2" : print ("I'm lost how about you\n")
elif action == "3" : print ("Ok i'm sorry to have bothered you\n")
else: print ("You do something crazy...la la la la!!\n")

# the rest is up to you...
# try using the conditional logic for different paths out of the cave

print ("The rest of the story is up to you...." + space)
       
# next we will look at loops an learn how they can help us do things
# with less typing/code.      

