def one(philosophers, hungry_positions):
    print("\nAllow one philosopher to eat at any time")
    for pos in hungry_positions:
        print(f"\nP {philosophers[pos]} is granted to eat")
        for other in hungry_positions:
            if other != pos:
                print(f"P {philosophers[other]} is waiting")

def two(philosophers, hungry_positions):
    print("\nAllow two philosophers to eat at the same time")
    n = len(hungry_positions)
    combination = 1
    for i in range(n):
        for j in range(i + 1, n):
            if abs(hungry_positions[i] - hungry_positions[j]) >= 1 and abs(hungry_positions[i] - hungry_positions[j]) != len(philosophers) - 1:
                print(f"\nCombination {combination}")
                combination += 1
                print(f"P {philosophers[hungry_positions[i]]} and P {philosophers[hungry_positions[j]]} are granted to eat")
                for other in hungry_positions:
                    if other != hungry_positions[i] and other != hungry_positions[j]:
                        print(f"P {philosophers[other]} is waiting")

def main():
    print("\nDINING PHILOSOPHER PROBLEM")
    tph = int(input("Enter the total number of philosophers: "))
    philosophers = list(range(1, tph + 1))
    status = [1] * tph

    how_hungry = int(input("How many are hungry: "))
    if how_hungry == tph:
        print("\nAll are hungry... Deadlock stage will occur")
        print("Exiting")
        return

    hungry_positions = []
    for i in range(how_hungry):
        pos = int(input(f"Enter philosopher {i + 1} position (0-based index): "))
        hungry_positions.append(pos)
        status[pos] = 2

    while True:
        print("\n1. One can eat at a time")
        print("2. Two can eat at a time")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            one(philosophers, hungry_positions)
        elif choice == 2:
            two(philosophers, hungry_positions)
        elif choice == 3:
            print("Exiting")
            break
        else:
            print("\nInvalid option..")

if __name__ == "__main__":
    main()
