actual_number = 5,4,3,2,1
attempts = 0
while True:
    attempts += 1
    guess = int(input("Guess the number: \n"))
    if guess < actual_number:
        print("your guess was too low")

    elif guess > actual_number:
        print("your guess was too high")

    else:
        print("you guessed the number in {attempts} attempts ")





