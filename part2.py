'''
***PART 2***

Write a program that prompts the user to enter a number. The program then prints "Hunter" the number of times the user entered. Use a while loop.

Example of what should appear when the program runs:

Times to print: 3
Hunter
Hunter
Hunter

'''

x = int(input("enter a number: "))
y = 0 
while x>0:
  print("hunter")
  y+=1
  if y >= x:
    break 


#OR! 
'''
for i in range(x):
  print("hunter")
'''