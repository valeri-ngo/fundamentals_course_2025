def positive_integer(number:int) -> str:
    divisor_sum = 0

    for current_number in range(1, number):
        if number % current_number == 0:
            divisor_sum += current_number

    if divisor_sum == number:
        print("We have a perfect number")
    else:
        print("It's not so perfect.")

positive_number = int(input())
positive_integer(positive_number)