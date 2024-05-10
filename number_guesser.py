import random

#
# start = input("Enter your first number : ")
# end = input("Enter your last number : ")
#
# r = random.randrange(int(start), int(end))
# print(r)

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger then 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

# random_number = random.randrange(11)
random_number = random.randint(0, top_of_range)
# print(random_number)

guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please Enter a Number Next Time.")
        continue

    if user_guess == random_number:
        print("You got it")
        break
    else:
        if user_guess > random_number:
            print("Wrong you were above the number.")
        else:
            print("Wrong you were below the number.")

    if guesses > 10:
        more = input("Do you would like to play more?(yes/no) ")
        if more.lower() == "yes":
            guesses = 0
            continue
        else:
            break


print("You got it in", guesses, "guesses")
