seat = int(input("Please input number (seat): "))


seatSmall = 5
seatMedium = 9
seatLarge = 15

costSmall = 5000
costMedium = 8000
costLarge = 12000


numSmall = (seat + seatSmall - 1) // seatSmall
numMedium = (seat + seatMedium - 1) // seatMedium
numLarge = (seat + seatLarge - 1) // seatLarge

totalCostSmall = numSmall * costSmall
totalCostMedium = numMedium * costMedium
totalCostLarge = numLarge * costLarge


cheapestCost = min(totalCostSmall, totalCostMedium, totalCostLarge)

if cheapestCost == totalCostSmall:
    print('S X', numSmall)
elif cheapestCost == totalCostMedium:
    print('M X', numMedium)
else:
    print('L X', numLarge)

print('Total = PHP', cheapestCost)
