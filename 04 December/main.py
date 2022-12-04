# 04 December
# Elf Seating Arrangement

i = 0
complete_overlap = 0
any_overlap = 0

# Open the input file and read it into an array
with open('input.txt') as f:
    # Read the lines into an array and remove the newline character from the end of each line
    lines = [line.rstrip() for line in f.readlines()]

    # Count the number of lines
    lineCount = len(lines)

    # Loop through the lines
    for line in lines:
        i += 1
        # Get the first half of the line separated by a comma
        firstHalf = line[:line.find(",")]

        # Get the second half of the line separated by a comma
        secondHalf = line[line.find(",") + 1:]

        # Generate the range of numbers for the first half
        firstHalfRange = range(int(firstHalf[:firstHalf.find("-")]), int(firstHalf[firstHalf.find("-") + 1:]) + 1)

        # Generate the range of numbers for the second half
        secondHalfRange = range(int(secondHalf[:secondHalf.find("-")]), int(secondHalf[secondHalf.find("-") + 1:]) + 1)

        # Check if the ranges completely overlap
        if firstHalfRange[0] in secondHalfRange and firstHalfRange[-1] in secondHalfRange:
            complete_overlap += 1

        # Check if the second range is completely within the first range
        elif secondHalfRange[0] in firstHalfRange and secondHalfRange[-1] in firstHalfRange:
            complete_overlap += 1

        # Check if any of the first half range overlaps with the second half range
        if any(item in firstHalfRange for item in secondHalfRange):
            any_overlap += 1


print(f"Complete Overlap: {complete_overlap}")
print(f"Any Overlap: {any_overlap}")
