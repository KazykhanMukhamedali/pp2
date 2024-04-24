import random
def bolnaya_igra():
    name = input("Hello! What is your name? ")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    guess = int(input("Take a guess."))
    while True:
        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too much")
        else:
            print("Correct")
            break
        guess = int(input("Take a guess."))