#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Oct 2021
# This is a guessing game

from constants import NUM


def main():
    # This function inputs guess and outputs if correct or not

    # input
    guess = int(input("Enter guess(0-9): "))

    # process/output
    if guess == NUM:
        print("You guessed correctly!")
    else:
        print(f"Incorrect, the number was {NUM}.")

    # output finished
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
