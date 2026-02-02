WORDS = {"PAIR": 4, "HAIR":4, "CHAIR":5, "GRAPHIC":7}

def main():
    print("Welcome to Spelling Bee")
    print("Your letters are: A C G H I P R ")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ")

        if guess == "GRAPHIC":
            WORDS.clear()
            print("You've won!")

        if guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"Good job! You scored {points} points.")
            

    print("Thats the game!")

main()    
for words, pnts in WORDS.items():
        print(f"{words} was worth {pnts} points")
