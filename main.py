#HOT or WARM or COLD

#import random number 

import random
random_number =  str(random.randint(100,999))
#if You known a random number uncomment line below
#print(random_number)

user_number = input("please enter a 3-digit number\n")


while(user_number != random_number):

  for i in range(len(random_number)):
    if (user_number[i] == random_number[i]):
      print("HOT")
    elif (user_number[i] in random_number):
      print("WARM")
    else:
      print("COLD")
      

  user_number = input("please enter a 3-digit number\n")

print("Congratulation")