import random

# Get guess
def get_guess():
    return list(input("What is your guess"))
#Generate computer code
def generate_digits():
    digits = [str(num) for num in range(10)]

    random.shuffle(digits)
    return digits[:3]
#Generate the clues
def generate_clues(digits, user_guess):
    if user_guess == digits:
        return "You've won!"

    clues = []

    for index,num in enumerate(user_guess):
        if num == digits[index]:
            clues.append("Match")
        elif num in digits:
            clues.append("Close")

    if clues == []:
        return ["Nope"]
    else:
        return clues
#Run game logic
print("Welcome to code breaker game. Let's see if you can guess my 3 digit number!")
secret_code = generate_digits()
print("Code has been generated, please guess a 3 digit number")

clue_report = []

while clue_report != "You've won!":
    guess = get_guess()

    clue_report = generate_clues(guess, secret_code)
    print("Here is the result of your guess: ")
    for clue in clue_report:
        print(clue)
