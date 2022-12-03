# 03 December/main.py
# Get the contents of an elfs rucksack.

# Open the input file and read it into an array
with open('input.txt') as f:
    lines = [line.rstrip() for line in f.readlines()]

# Remove the newline character from the end of each line
lines = [line.rstrip() for line in lines]
duplicateItems = ""
duplicateSum = 0
i = 0

# Loop through the lines
for line in lines:
    # Get the first half of the line
    compartment1 = line[:len(line) // 2]
    # Get the second half of the line
    compartment2 = line[len(line) // 2:]

    # Check if any character in the first half is in the second half
    # If it is, add the character to the list
    if any(char in compartment2 for char in compartment1):
        # Get the character that is in both halves
        duplicateItems = ([char for char in compartment1 if char in compartment2][0])
        # print(f"Duplicate item: {duplicateItems}")

        # If the character is a lowercase letter, assign it a value 1-26
        if duplicateItems.islower():
            duplicateSum += ord(duplicateItems) - 96
            # print(f"Duplicate sum: {duplicateSum}")

        # If the character is an uppercase letter, assign it a value 27-52
        elif duplicateItems.isupper():
            duplicateSum += ord(duplicateItems) - 38

            # print(f"Duplicate sum: {duplicateSum}")

print(f"Final sum: {duplicateSum}")


# Part 2
# Figure out what group the elf is in and what the elf's score is.

# Create a new sum
sum = 0

# Loop through the lines again and add the value of each character to the sum
for i in range(0, len(lines), 3):
    # Get the first character of the line
    x, y, z = [set(items) for items in lines[i:i + 3]]

    # Get the intersection of the three sets
    char = list(x & y & z)[0]

    # If the character is a lowercase letter, assign it a value 1-26
    if char.islower():
        sum += ord(char) - 96

    # If the character is an uppercase letter, assign it a value 27-52
    elif char.isupper():
        sum += ord(char) - 38

print(sum)


f.close()
