import random

def roll_die(sides=6):
    return random.randint(1, sides)

def main():
    print("🎲 Simple Dice Roller")
    while True:
        # Ask for number of sides
        sides_input = input("Enter number of sides (default 6, or 'q' to quit): ").strip().lower()
        if sides_input == 'q':
            print("Goodbye!")
            break

        # Validate sides
        if sides_input == '':
            sides = 6
        else:
            if not sides_input.isdigit() or int(sides_input) < 2:
                print("Please enter a valid number (at least 2).")
                continue
            sides = int(sides_input)

        # Roll loop
        while True:
            result = roll_die(sides)
            print(f"You rolled: {result}")
            nxt = input("Roll again? (y/n, or 'c' to change sides): ").strip().lower()
            if nxt == 'y':
                continue
            elif nxt == 'c':
                break
            else:
                print("Goodbye!")
                return

if __name__ == "__main__":
    main()
