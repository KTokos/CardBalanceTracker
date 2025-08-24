#######################################
#
# Kristian Tokos
# 08.23.2025
# University at Albany
# Computer Science Major
#
#######################################

# Create an empty purchases list
purchases = []

# Create an empty variable to accumulate total cost
totalCost = 0.00

# Open the text file and read all lines into a list
with open('CardBalance.txt', 'r') as file:
    lines = file.readlines()

# Extract the starting balance from the file
startingBalanceLine = lines[0]
startingBalance = startingBalanceLine.split(': ')[1].strip()
print(f"Starting Balance: {startingBalance}")

# Prompt the user to add more purchases
response = input("Would you like to add a purchase? (yes/no): ").strip().lower()

if response == "yes":
    purchaseName = input("Name of purchase: ").strip()
    purchasePrice = input("Price of purchase: ").strip()

    lines.append(f"\n{purchaseName} - {purchasePrice}")

    # Get the starting line of the purchases
    searchTerm = "Purchases:"
    for i, line in enumerate(lines):
        if searchTerm in line:
            purchasesLine = i + 1
            break

    # Add all purchases to the list of purchases
    for line in lines[purchasesLine:]:
        if '- ' in line:
            try:
                price = line.split('- ')[1].strip()
                purchases.append(price)
            except IndexError:
                print(f"Skipping malformed line: {line}")

    # Get the value of all the purchases combined
    for price in purchases:
        totalCost += float(price)

    # Calculate the remaining balance
    remainingBalance = float(startingBalance) - totalCost

    # Update the remaining balance in the list
    lines[1] = f"Remaining Balance: {remainingBalance}"

    # Clear the file
    with open('CardBalance.txt', 'w') as file:
        file.write("")

    # Rewrite the file with new changes
    with open('CardBalance.txt', 'w') as file:
        file.writelines(lines)
else:
    print("No changes made...")