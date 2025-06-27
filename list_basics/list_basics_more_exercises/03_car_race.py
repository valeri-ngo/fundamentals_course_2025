time_input = list(map(int,input().split()))
middle_side = len(time_input) // 2

left_side = time_input[:middle_side]
right_side = time_input[-1: middle_side: -1]

left_side_time = 0
right_side_time = 0

for time in left_side:
    if time == 0:
        left_side_time *= 0.8
    else:
        left_side_time += time

for time in right_side:
    if time == 0:
        right_side_time *= 0.8
    else:
        right_side_time += time

if left_side_time < right_side_time:
    print(f"The winner is left with total time: {left_side_time:.1f}")
else:
    print(f"The winner is right with total time: {right_side_time:.1f}")
