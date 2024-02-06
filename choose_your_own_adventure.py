name = input("Type your name: ")
print("Welcome", name, "to this adventure")

answer = input("You are on a dirt rod, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
   answer =   input("you come to a river, you can walk around or swim to swim across? type walk to walk around and swim to swim across: ")

   if answer == "swim":
      print("you swam across and were eaten by an alliagtors")
   elif answer =="walk":
      print("you walked for many miles, ran out of water and lost the game ")
   else:
     print('Not a valid option, you lose') 
            
elif answer == "right":
  print()

else: 
   print('Not a valid option, you loose')