def earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration):
    min_time = float('inf')

    for i in range(len(landStartTime)):
        for j in range(len(waterStartTime)):
            # Option 1: Land → Water
            land_start = landStartTime[i]
            land_end = land_start + landDuration[i]
            water_start = max(waterStartTime[j], land_end)
            total1 = water_start + waterDuration[j]

            # Option 2: Water → Land
            water_init = waterStartTime[j]
            water_end = water_init + waterDuration[j]
            land_start2 = max(landStartTime[i], water_end)
            total2 = land_start2 + landDuration[i]

            # Update the minimum finish time
            min_time = min(min_time, total1, total2)

    return min_time

landStartTime = [2, 8]
landDuration = [4, 1]
waterStartTime = [6]
waterDuration = [3]

print(earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration))
# Output: 9

landStartTime = [5]
landDuration = [3]
waterStartTime = [1]
waterDuration = [10]

print(earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration))
# Output: 14
