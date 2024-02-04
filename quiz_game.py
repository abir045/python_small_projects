print("Welcome to my computer quiz")

playing = input(" do you want to play? ")

if playing.lower() != "yes":
    quit()


print("okay! Lets play: )")

score = 0

ans = input("what does cpu stand for? ")

if ans.lower() == "central processing unit": 
    print('correct!')
    score += 1
else: 
    print('incorrect')    

ans = input('what does GPU stand for ?')

if ans.lower() == "graphics processing unit" : 
    print('correct')
    score += 1
else: 
    print('incorrect')    

ans = input('what does PSU stand for? ')

if ans.lower() == "power supply unit":
    print('correct')
    score += 1

else: print('incorrect')

ans = input('what does RAM atand for? ')

if ans.lower() == 'random access memory':
    print('correct')
    score += 1
else: print('incorrect')    


print("you got " + str(score) +  ' questions correct')
print("you got " + str((score/4) * 100 ) + "%. " )


