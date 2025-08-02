class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        # Step 1: Get earliest land ride finish time
        min_land_finish = float('inf')
        for i in range(len(landStartTime)):
            finish = landStartTime[i] + landDuration[i]
            if finish < min_land_finish:
                min_land_finish = finish
        
        # Step 2: Get earliest water ride finish time
        min_water_finish = float('inf')
        for j in range(len(waterStartTime)):
            finish = waterStartTime[j] + waterDuration[j]
            if finish < min_water_finish:
                min_water_finish = finish
        
        # Step 3: Try both sequences
        # Land first → wait for water
        earliest_land_to_water = float('inf')
        for j in range(len(waterStartTime)):
            start_after_land = max(min_land_finish, waterStartTime[j])
            finish = start_after_land + waterDuration[j]
            if finish < earliest_land_to_water:
                earliest_land_to_water = finish

        # Water first → wait for land
        earliest_water_to_land = float('inf')
        for i in range(len(landStartTime)):
            start_after_water = max(min_water_finish, landStartTime[i])
            finish = start_after_water + landDuration[i]
            if finish < earliest_water_to_land:
                earliest_water_to_land = finish

        return min(earliest_land_to_water, earliest_water_to_land)

sol = Solution()
# Example 1
print(sol.earliestFinishTime([2, 8], [4, 1], [6], [3]))  # ➜ 9

# Example 2
print(sol.earliestFinishTime([5], [3], [1], [10]))       # ➜ 14
