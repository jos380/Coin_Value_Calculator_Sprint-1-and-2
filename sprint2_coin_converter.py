# Coin Value Calculator System

def calculate_total(pennies, nickels, dimes, quarters):
    total = (pennies * 0.01) + (nickels * 0.05) + (dimes * 0.10) + (quarters * 0.25)
    return round(total, 2)


def run_tests():
    print("\n================ TEST RESULTS ================\n")
    print(f"{'Test Case':60} {'Result'}")
    print("-" * 75)

    tests = [
        ("1 penny and 2 nickels", calculate_total(1, 2, 0, 0)),
        ("4 dimes and 7 quarters", calculate_total(0, 0, 4, 7)),
        ("1 quarter and 3 pennies", calculate_total(3, 0, 0, 1)),
        ("21 pennies, 17 dimes, 52 quarters", calculate_total(21, 0, 17, 52))
    ]

    for description, result in tests:
        print(f"{description:60} ${result}")


def user_input_mode():
    print("\n===== Coin Calculator =====")
    p = int(input("Enter number of pennies: "))
    n = int(input("Enter number of nickels: "))
    d = int(input("Enter number of dimes: "))
    q = int(input("Enter number of quarters: "))

    total = calculate_total(p, n, d, q)
    print(f"\nTotal value: ${total}")


# Main Program
if __name__ == "__main__":
    run_tests()

    choice = input("\nDo you want to enter your own values? (y/n): ")
    if choice.lower() == 'y':
        user_input_mode()
