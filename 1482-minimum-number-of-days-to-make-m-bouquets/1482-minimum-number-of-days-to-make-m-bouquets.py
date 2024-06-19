class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        def getBouquetCount(waitingDays: int) -> int:
            bouquetCount = 0
            requiredFlowers = k
            for day in bloomDay:
                if day > waitingDays:
                    requiredFlowers = k
                else:
                    requiredFlowers -= 1
                    if requiredFlowers == 0:
                        bouquetCount += 1
                        requiredFlowers = k
            return bouquetCount

        dayMin = min(bloomDay)
        dayMax = max(bloomDay)

        while dayMin < dayMax:
            dayMid = (dayMin + dayMax) // 2
            if getBouquetCount(dayMid) >= m:
                dayMax = dayMid
            else:
                dayMin = dayMid + 1

        return dayMin