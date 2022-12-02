# December 01

# Open the input file
with open('input.txt') as f:

    # Read the file into a list
    lines = f.readlines()

    sum_calories: int = 0
    elf: int = 1

    elf_with_most_calories: int = 0
    elf_current_calories: int = 0
    max_calories: int = 0

    elf_with_second_most_calories: int = 0
    second_most_calories: int = 0

    elf_with_third_most_calories: int = 0
    third_most_calories: int = 0

    # Loop through the list
    for line in lines:

        # Check if the line is empty or not
        if line.strip():
            sum_calories += int(line)
            elf_current_calories += int(line)

        else:
            if elf_current_calories == max_calories:
                print(f"Elf {elf} has the same amount of calories as elf {elf_with_most_calories}")
            elif elf_current_calories > max_calories:

                # Since we have a new leader, we need to move the current leader down
                # to second place. We need to do this by moving the second place elf to third place FIRST.

                # Move the current second to the third place
                third_most_calories = second_most_calories
                elf_with_third_most_calories = elf_with_second_most_calories

                # Move the current max to the second place
                second_most_calories = max_calories
                elf_with_second_most_calories = elf_with_most_calories


                # Set the new max
                max_calories = elf_current_calories
                elf_with_most_calories = elf

                print(f"Elf {elf} is now in the lead with {max_calories} calories")

            elif elf_current_calories > second_most_calories:
                # Move the current second to the third place
                third_most_calories = second_most_calories
                elf_with_third_most_calories = elf_with_second_most_calories

                second_most_calories = elf_current_calories
                elf_with_second_most_calories = elf

            elif elf_current_calories > third_most_calories:

                third_most_calories = elf_current_calories
                elf_with_third_most_calories = elf

            print(f"{elf},{elf_current_calories}")
            elf += 1
            elf_current_calories = 0


print('Total calories: {}'.format(sum_calories))
print(f"Elf {elf_with_most_calories} has the most calories with {max_calories} calories")
print(f"Elf {elf_with_second_most_calories} has the second most calories with {second_most_calories} calories")
print(f"Elf {elf_with_third_most_calories} has the third most calories with {third_most_calories} calories")

# Get the sum of the top 3 elves
top_3_elves = max_calories + second_most_calories + third_most_calories
print(f"The sum of the top 3 elves is {top_3_elves}")


