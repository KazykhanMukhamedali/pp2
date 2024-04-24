def solve(heads, legs):
    chickens = heads
    rabbits = 0
    while chickens*2+rabbits*4!=legs:
        chickens-=1
        rabbits+=1
    return chickens, rabbits
print(solve(35,94))