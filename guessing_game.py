
import random as rd

def guessing_game():
    print("<--------------------Guessing game--------------------->")

    print("Select the range of numbers\n")
    print('1.0-10\n2.0-20')
    range = int(input("Enter your choice (1 or 2): "))

    if range ==1 :
        range_st = 0
        range_ed = 10
    elif range==2:
        range_st = 0
        range_ed = 20
    else:
        print("invalid choice exiting the game\n")
        return

    comp_generated_num = rd.randint(range_st,range_ed)
    while True:
        guess = int(input(f"Enter the number to guess ({range_st} {range_ed}): "))
        if guess<range_st and guess>range_ed :
                print("Guessed number is out of range try within range(0-10)\n")
        elif guess==comp_generated_num :
                print("Congratulation! you guessed the right number\n")
                break
        else:
                print("Wrong guess,Try again.")

if __name__ == "__main__":
    while True:
        start_or_exit=int(input('Enter\n1.Start\n2.Exit\n'))
        if start_or_exit==1:
            guessing_game()
        elif start_or_exit == 2:
            print("Game closed.")
            break




