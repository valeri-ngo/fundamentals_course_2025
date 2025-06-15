number_of_electrons = int(input())
shell_number = 1
filled_shells = 0

electron_list = []

while number_of_electrons > 0:

    shell_capacity = 2 * shell_number ** 2
    electrons_in_a_shell = min(number_of_electrons, shell_capacity)
    electron_list.append(electrons_in_a_shell)
    number_of_electrons -= electrons_in_a_shell
    shell_number += 1

print(electron_list)
