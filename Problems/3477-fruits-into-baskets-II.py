class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        used = [False] * len(baskets)  # Track used baskets
        unplaced = 0 # Count how many fruits couldn't be placed

        # Step: Go through each fruit in order
        for i in range(len(fruits)):
            placed = False # Reset for this fruit
            # Step : Try placing this fruit in the leftmost fitting unused basket
            for j in range(len(baskets)):
                if not used[j] and baskets[j] >= fruits[i]:
                    used[j] = True # Mark basket as used
                    placed = True # Mark fruit as placed
                    break # No need to check other baskets
            if not placed:
                unplaced += 1 # Fruit couldn't be placed

        return unplaced
