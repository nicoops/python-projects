import math
import sys

def triple_check():
    print("Input the length of each side of your triangle.")
    sides = []

    while len(sides) != 3:
        side_length = input('> ')
        if side_length.isdigit() == True and int(side_length) != 0:
            sides.append(int(side_length))
        else:
            print("Not a proper length. Try again.\n")

    hyp = max(sides)
    c = hyp
    a = sides[0]
    b = sides[1]

    if a ** 2 + b ** 2 == c ** 2:
        print ("This is a Pythagorean triangle. Congrats.")
    elif a ** 2 + b ** 2 != c ** 2:
        print ("This is not a Pythagorean triangle. Weak.")

    ask_question()

def ask_question():
    answer = input("Press enter to try again, and 'q' to quit.")
    if answer == (''):
        triple_check()
    elif answer == 'q':
        pass
    else:
        print ("I didn't recognize that command. Try again.")
        ask_question()

if __name__ == "__main__":
    triple_check()
