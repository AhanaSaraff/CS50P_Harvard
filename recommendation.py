difficulty = input("Difficult or Casual? ")
player = input("Multiplayer or Single? ")

def main():
    if difficulty == "Difficult": 
        if player == "Multiplayer":
            return "Poker"
        elif player == "Single":
            return "Klondike"
        else:
            return "Enter valid player type"
    elif difficulty == "Casual":
        if player == "Multiplayer":
            return "Hearts"
        elif player=="Single":
            return "Clock"
        else:
            return "Enter valid player type"
    else:
        return "Enter a valid difficulty"

        

print(main())
