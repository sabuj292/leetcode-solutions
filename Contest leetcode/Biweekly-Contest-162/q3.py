
import sys
# For faster input
input = sys.stdin.readline
# For faster output
sys.stdout.write(str(result) + "\n")
class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        min_finish_time = float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                # Option 1: Land ride → Water ride
                land_start = landStartTime[i]
                land_end = land_start + landDuration[i]
                water_start_after_land = max(land_end, waterStartTime[j])
                water_end_after_land = water_start_after_land + waterDuration[j]

                total_time1 = water_end_after_land

                # Option 2: Water ride → Land ride
                water_start = waterStartTime[j]
                water_end = water_start + waterDuration[j]
                land_start_after_water = max(water_end, landStartTime[i])
                land_end_after_water = land_start_after_water + landDuration[i]

                total_time2 = land_end_after_water

                # Update the minimum of both plans
                min_finish_time = min(min_finish_time, total_time1, total_time2)

        return min_finish_time

landStartTime = [2, 8]
landDuration = [4, 1]
waterStartTime = [6]
waterDuration = [3]
sol = Solution()
print(sol.earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration))
# Output: 9 
landStartTime = [5]
landDuration = [3]
waterStartTime = [1]
waterDuration = [10]

print(sol.earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration))
# Output: 14 
