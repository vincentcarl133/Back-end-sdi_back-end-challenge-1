
seat = int(input("Please input number (seat): "))


cheapestCost = float('inf')


seatSmall = 5
seatMedium = 10
seatLarge = 15

costSmall = 5000
costMedium = 8000
costLarge = 12000

if seat < 5:
    print('S X', costSmall)
else:
    for small in range((seat // seatSmall) + 1):
        for medium in range((seat // seatMedium) + 1):
            for large in range((seat // seatLarge) + 1):

                totalCost = small * costSmall + medium * costMedium + large * costLarge
                totalSeats = small * seatSmall + medium * seatMedium + large * seatLarge

                if totalSeats >= seat and totalCost < cheapestCost:
                    cheapestCost = totalCost
                    car = (small, medium, large)
    
    if car[0] !=0:
        print ('S X', car[0])
    if car[1] !=0:
        print ('M X', car[1])
    if car[2] !=0:
        print ('L X', car[2])

    print('Total = PHP', cheapestCost)