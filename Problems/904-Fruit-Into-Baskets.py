class Solution(object):
    def totalFruit(self, fruits):
        from collections import defaultdict
        
        count = defaultdict(int)  # to store fruit types and their counts
        left = 0                  # left pointer of the window
        max_fruits = 0            # maximum number of fruits we can collect

        for right in range(len(fruits)):
            fruit = fruits[right]
            count[fruit] += 1  # add fruit at position `right`

            # If we have more than 2 types of fruit, shrink the window from the left
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]  # completely remove the fruit type
                left += 1  # move left boundary to the right

            # Update the max number of fruits picked so far
            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
