import os
import time

program = input("Which part(1, 2, 3, 4, or 5)? ")

while program not in ['1', '2', '3', '4', '5']:
    os.system('clear')
    print("That's not a valid input.")
    time.sleep(1)
    program = input("Which part(1, 2, 3, 4, or 5)? ")

os.system('clear')

if program == '1':
  import part1
elif program == '2':
  import part2
elif program == '3':
  import part3
elif program == '4':
  import part4
elif program == '5':
  import part5


  #i'm sorry it is 2am and as i have been working on this for around two hours and i am still not done i will be giving up for now