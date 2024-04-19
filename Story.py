#
# Gavin and Will
# 4/whatever/24
# fucntions for the text element of story parts
import os
import random
from time import sleep
import Main
import Filesaver

# Will Vanderploeg:
# Displays the intro one line at a time using the intro.txt file


def intro():
    year = random.randrange(224, 8427)
    print(f"\n\nThe year is {year}")
    sleep(.87)
    intro = open("intro.txt", "r")
    for line in intro:
        print(line.strip())
        sleep(.87)
    intro.close()


# Gavin M.
def game_over(score, name):
    death = """\t\t░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
\t\t░   ░░░░░░   ░░░░░     ░░░░░░   ░░░░░   ░░░░░░░      ░░░░░   ░         ░      ░░░░
\t\t▒▒   ▒▒▒▒   ▒▒▒▒   ▒▒▒▒   ▒▒▒   ▒▒▒▒▒   ▒▒▒▒▒▒▒   ▒▒▒   ▒▒   ▒   ▒▒▒▒▒▒▒   ▒▒▒   ▒
\t\t▒▒▒   ▒   ▒▒▒▒   ▒▒▒▒▒▒▒▒   ▒   ▒▒▒▒▒   ▒▒▒▒▒▒▒   ▒▒▒▒   ▒   ▒   ▒▒▒▒▒▒▒   ▒▒▒▒   
\t\t▓▓▓▓▓   ▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓   ▓▓▓▓▓   ▓▓▓▓▓▓▓   ▓▓▓▓   ▓   ▓       ▓▓▓   ▓▓▓▓   
\t\t▓▓▓▓▓   ▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓   ▓▓▓▓▓   ▓▓▓▓▓▓▓   ▓▓▓▓   ▓   ▓   ▓▓▓▓▓▓▓   ▓▓▓▓   
\t\t▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓▓▓▓▓   ▓▓   ▓▓▓▓▓   ▓▓▓▓▓▓▓   ▓▓▓   ▓▓   ▓   ▓▓▓▓▓▓▓   ▓▓▓   ▓
\t\t█████   ██████████     ████████      ██████████      █████   █         █      ████
\t\t██████████████████████████████████████████████████████████████████████████████████"""
    for line in death.splitlines():
        print(line)
        sleep(.34)
    print("Try again? (y/n)")
    again = input("\t").lower()
    print()
    while True:
        if again == 'y':
            print("You feel a strange surging of determi--")
            sleep(.8)
            print("\tEmpowerment..", end=" ")
            sleep(1)
            print("Anyway lets try again.")
            score_table = Filesaver.full_process(score, name, True)
            count = 5
            for time in range(5):
                os.system("cls")
                print(f"Continuing in: {count}")
                Filesaver.displayscores(score_table, False)
                sleep(1)
                count -= 1
            Main.main()
            break
        elif again == 'n':
            Filesaver.full_process(score, name)
            sleep(5)
            quit()
        else:
            print('huh?')
            sleep(4)
            print("\nTry again? (y/n)")
            again = input("\t").lower()

game_over(2, "Vir Patel")
