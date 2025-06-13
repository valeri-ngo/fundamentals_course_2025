def tribonacci_sequence(number: int) -> None:
    if number < 0:
        return

    first_t0 = 1
    second_t1 = 1
    third_t2 = 2
    tribonacci_list = [1, 1, 2]


    for current_number in range(3, number):
        num = first_t0 + second_t1 + third_t2
        first_t0 = second_t1
        second_t1 = third_t2
        third_t2 = num
        tribonacci_list.append(num)
    print(' '.join(str(x) for x in tribonacci_list[:number]))

number_input = int(input())
tribonacci_sequence(number_input)

