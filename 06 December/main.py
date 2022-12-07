# 06 December
# Elf packet tracing

# Open the input file and read it into a string
with open('input.txt') as f:
    chars: str = f.read()

    # Remove the newline character from the end of the string
    chars = chars.rstrip()

    # Count the number of characters
    charCount: int = len(chars)

# Read through the string, and count how many characters needs to be processed before there are four unique characters in a row
for i in range(charCount):
    # Get the next four characters
    fourChars: str = chars[i:i+4]

    # Check if the four characters are unique
    if len(set(fourChars)) == 4:
        # Print the number of characters that need to be processed
        print(4+i)
        break

# Part 2
# Read through the string again, and count how many characters needs to be processed before there are 14 unique characters in a row
for i in range(charCount):
    # Get the next 14 characters
    fourteenChars: str = chars[i:i+14]

    # Check if the 14 characters are unique
    if len(set(fourteenChars)) == 14:
        # Print the number of characters that need to be processed
        print(14+i)
        break