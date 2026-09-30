weather = (0,1,1,0,0,1,0,1,0,0,1,1,0,1,0,1)
sunny = 0
rainy = 0
for i in range(0,16):
    if weather[i]== 0:
        rainy += 1
    else:
        sunny += 1

if (rainy<sunny):
    print("Good Weather") 
elif(rainy==sunny):
    print("Normal Weather")   
else:
    print("Bad Weather")              
