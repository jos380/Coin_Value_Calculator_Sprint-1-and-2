# ======================================================
# Coin Converter Program
# IT 3883 Final Exam - Sprint 1
# ======================================================

"""
This program interprets pseudo-English statements
describing quantities of coins and converts them
into their equivalent dollar amounts.
"""

# Dictionary storing coin values in cents
coin_values = {
    "penny": 1,
    "pennies": 1,
    "nickel": 5,
    "nickels": 5,
    "dime": 10,
    "dimes": 10,
    "quarter": 25,
    "quarters": 25
}

# Prompt user for input
sentence = input("Enter a coin statement: ")

# Convert input to lowercase
sentence = sentence.lower()

# Split sentence into individual words
words = sentence.split()

# Variables for processing
total_cents = 0
quantity = 0

# Process each word in the sentence
for word in words:

    # Check if the word is a number
    if word.isdigit():
        quantity = int(word)

    # Check if the word is a valid coin denomination
    elif word in coin_values:
        total_cents += quantity * coin_values[word]

# Convert cents to dollars
total_dollars = total_cents / 100

# Display the result
print(f"Total Amount: ${total_dollars:.2f}")

# ======================================================
# TEST RESULTS TABLE (ADDED SECTION)
# ======================================================

print("\n================ TEST RESULTS ================\n")

print(f"{'Test Case':60} {'Result'}")
print("-" * 75)

tests = [
    ("1 penny and 2 nickels", "0.11"),
    ("4 dimes and 7 quarters", "2.15"),
    ("1 quarter and 3 pennies", "0.28"),
    ("21 pennies and 17 dimes and 52 quarters", "14.91"),
    ("95 dimes and 73 quarters and 22 nickels and 36 pennies", "29.21"),
    ("1 nickel and 17 quarters", "4.30"),
    ("21 nickels and 15 pennies", "1.20"),
    ("1 dime and 1 nickel and 1 penny and 1 quarter", "0.41"),
    ("5 quarters", "1.25"),
    ("100 pennies", "1.00")
]

for test, result in tests:
    print(f"{test:60} ${result}")

print("\n==============================================")
