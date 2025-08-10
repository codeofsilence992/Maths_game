def main():
    import random
    import time
    is_running = True
    gameno = 0
    games = {}
    total = 0
    gametypes = []


    def multiplication():
        nonlocal correct
        for x in range(1, 11):
            num1 = random.randint(0, 12)
            num2 = random.randint(0, 12)
            print(f"Question {x}")
            print(f"{num1} x {num2}")
            ans = input("> ").strip()
            try:
                ans = int(ans)
                if ans == (num1 * num2):
                    correct += 1
                    print("Correct!")
                else:
                    print("Incorrect!")
            except ValueError:
                print("Incorrect!")

    def subtraction():
        nonlocal correct
        for x in range(1, 11):
            num1 = random.randint(0, 100)
            num2 = random.randint(0, num1)
            print(f"Question {x}")
            print(f"{num1} - {num2}")
            ans = input("> ").strip()
            try:
                ans = int(ans)
                if ans == (num1 - num2):
                    correct += 1
                    print("Correct!")
                else:
                    print("Incorrect!")
            except ValueError:
                print("Incorrect!")


    def addition():
        nonlocal correct
        for x in range(1, 11):
            num1 = random.randint(0, 100)
            num2 = random.randint(0, 100)
            print(f"Question {x}")
            print(f"{num1} + {num2}")
            ans = input("> ").strip()
            try:
                ans = int(ans)
                if ans == (num1 + num2):
                    correct += 1
                    print("Correct!")
                else:
                    print("Incorrect!")
            except ValueError:
                print("Incorrect!")

    def division():
        nonlocal correct
        for x in range(1, 11):
            numlist = []
            num1 = random.randint(0, 100)
            for number in range(1, num1):
                if num1 % number != 0:
                    continue
                elif num1 % number == 0:
                    numlist.append(number)
            num2 = random.choice(numlist)
            print(f"Question {x}")
            print(f"{num1} / {num2}")
            ans = input("> ").strip()
            try:
                ans = int(ans)
                if ans == (num1 / num2):
                    correct += 1
                    print("Correct!")
                else:
                    print("Incorrect!")
            except ValueError:
                print("Incorrect!")




    while is_running:
        print("Welcome to the game")

        print("What type of test do you want to do?")
        print("Division [D]")
        print("Multiplication [M]")
        print("Addition [A]")
        print("Subtraction [S]")
        print("Quit [Q]")
        gamemode = input("> ").lower().strip()
        if gamemode == "q":
            is_running = False
            continue
        elif gamemode not in ("m", "a", "s", "d"):
            print("Please choose a valid option!")
            continue

        correct = 0
        in_game = True
        while in_game:
            gameno += 1
            print(f"Game {gameno}")
            time.sleep(1)
            if gamemode == "m":
                gametypes.append("Multiplication")
                multiplication()
            elif gamemode == "a":
                gametypes.append("Addition")
                addition()
            elif gamemode == "s":
                gametypes.append("Subtraction")
                subtraction()
            elif gamemode == "d":
                gametypes.append("Division")
                division()
            games.update({gameno: correct})
            total += correct
            print(f"Good job! You got {correct}/10 correct!")
            print("New game [N]")
            print("Quit [Q]")
            print("View games [V]")

            while True:
                option = input("> ").lower().strip()
                if option == "q":
                    is_running = False
                    in_game = False
                    break
                elif option == "n":
                    in_game = False
                    break
                elif option == "v":
                    for key, value in games.items():
                        print(f"Game {key}: {value}/10 ({gametypes[key - 1]})")
                    print(f"Overall: {total}/{gameno * 10} ({total / (gameno * 10) * 100}%)")
                else:
                    print("Please choose a valid option")

    print("Thank you for playing!")


if __name__ == "__main__":
    main()