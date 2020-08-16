import random 
number_of_streaks = 0
streak = 0
flips = [] #Stores 1 for heads, 0 for tails

#Flips the coin
for experiment_number in range (10000): 
    for i in range(100):
        flips.append(random.randint(0,1))
    
    for i in range(len(flips)): 
        if i ==0: 
            pass
        elif flips[i] == flips[i-1]: 
            streak +=1 
        else: 
            streak =0
        if streak == 6:
            number_of_streaks += 1 
    flips = []
print (f"Chances of streak: {number_of_streaks/ 100} %")




            
            



