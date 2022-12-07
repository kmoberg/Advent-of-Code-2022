# 07 December
# Elf terminal emulator

from collections import defaultdict
from itertools import accumulate

# Initialize a dictionary to store the number of times each character appears
# Use defaultdict over a normal dictionary provides a default value of 0 for any key that doesn't exist
terminal = defaultdict(int)

# Open the input file and read it into a string
for line in open('input.txt'):

    # For each 'line' in the file, check if the line matches a pattern
    match line.split():
        # Root directory
        case '$', 'cd', '/':
            curr = ['']

        # 'Dir' indicates a subdirectory. No need to do anything with it
        case 'dir', _:
            pass                           

            # If the user moves INTO a directory, add the directory to the path
        case '$', 'cd', x:
            curr.append(x + '/')

        # If the user moves OUT one directory remove the last directory from the path
        case '$', 'cd', '..':
            curr.pop()

        # If the user types 'ls', print the current directory
        case '$', 'ls':
            pass

        # If the line starts with a number, it's a file. Add that number to the dictionary
        case size, _:
            for p in accumulate(curr):
                terminal[p] += int(size)

total_size = sum(s for s in terminal.values() if s <= 100_000)
space_saved = min(s for s in terminal.values() if s >= terminal[''] - 40_000_000)
print(f'Total size of directories: {total_size} bytes')
print(f'Potential space saving: {space_saved} bytes')
