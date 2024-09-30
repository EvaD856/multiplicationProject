'''
Program: Basic Multiplication Table
Author: Eva Donahue

1. Ask the user for a number
2. Print our the name of the multiplaction table:
    "Multiplication Table for <number>: "
3. for Loop print out all the multiplication facts (1 to 12) for the users number
'''
factor = int(input("Enter a number to generate a multiplication table: "))

multiplier = 0

count=1
product = 0
for count in range(12):
    product = product + factor
    print(factor,"x",count,"=", product)

# Create your code 

'''
Multiplication Table Generator with Custom Range, and Multi-Table Option 

1. Ask the user if they want to generate multiple tables 
2. Create a Function to do stepts 2 & 3 above (3 variables: number, start=1, end=12)
3. Create a control structure to handle the user answer from step 1 
    What do we do if yes
    What do we do if no

answer = input("Do your want custom range?(yes or no) : ")
if answer == 'yes' :
    print("Excellent!")
else:
    print("ok, end")


start = int(input("What is your starting number? "))
end = int(input("What is your end number? "))

for custom in range (start, end):
    list = list + 
'''