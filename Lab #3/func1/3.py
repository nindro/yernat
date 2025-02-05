#Write a program to solve a classic puzzle: 
#We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
#`create function: solve(numheads, numlegs):`
def solve(numheads, numlegs):
    for chick in range(numheads+1):
        rab = numheads - chick
        if 2*chick + 4*rab == numlegs:
            return chick, rab
    return "No solution"
    
heads = 35
legs = 94
chickens, rabbits = solve(heads, legs)
print(f"Chickens: {chickens}, Rabbits: {rabbits}")
#RESULTS
#Chickens: 23, Rabbits: 12