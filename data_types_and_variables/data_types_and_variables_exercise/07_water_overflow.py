refill_loop = int(input())
tank_capacity = 255
liters = 0

for liters_added in range(refill_loop):
    liters_of_water = int(input())

    if liters_of_water > tank_capacity:
        print('Insufficient capacity!')
        continue

    tank_capacity -= liters_of_water
print(255 - tank_capacity)
#
# number_of_refills = int(input())
# tank_capacity = 255
# sum_liters = 0
#
# while tank_capacity > sum_liters:
#     water_added = int(input())
#
#     sum_liters += water_added
#
#     if tank_capacity < sum_liters:
#         print('Insufficient capacity!')
#         continue
# print(abs(255 - tank_capacity))