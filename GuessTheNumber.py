from random import randint
my_number = randint(0, 20)

print "Guess the number!"
guess = int(raw_input("> "))

print my_number

while guess != my_number:
    if guess < my_number :
        print "Your guess is too low."
        print "Please guess again."
        guess = int(raw_input("> "))
    else:
        print "You guess is too high."
        print "Please guess again."
        guess = int(raw_input("> "))

print "Congratulations!"
