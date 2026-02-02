def main():
    history = []

    while True:
        action = input('Action: ')

        if action == "Undo":
            history.pop()
        else:
            history.append(action)
        print(history)

main()