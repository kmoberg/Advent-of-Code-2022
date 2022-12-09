# 08 December
# Elf Treehouse
# Calculate how many trees are hidden from outside the grid of trees

# Finally a good use for numnpy!
import numpy as np

# Open the input file and read it into a numpy array
forest = np.array([list(x.strip()) for x in open('input.txt')], int)
visible_trees = np.zeros_like(forest, int)
senic_score = np.ones_like(forest, int)

# Loop through the forest
for _ in range(4):
    for x, y in np.ndindex(forest.shape):
        # Calculate if the tree is lower than the tree in the same column, but one row above
        z = [tree < forest[x, y] for tree in forest[x, y + 1:]]

        # Calculate how many trees are lower than the current tree
        visible_trees[x, y] |= all(z)

        # Calculate the senic score - take the number of trees around the tree and check how far you can see
        # in each direction without getting to a tree that is higher than the current tree
        senic_score[x, y] *= next((i + 1 for i, v in enumerate(z) if ~v), len(z))

        # Rotate the forest 90 degrees to get both directions
        forest = np.rot90(forest)
        visible_trees = np.rot90(visible_trees)
        senic_score = np.rot90(senic_score)

# Print the number of visible trees
print(np.sum(visible_trees))
print(senic_score.max())
