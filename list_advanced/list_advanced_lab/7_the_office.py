employees_happiness = input().split()
happiness_improvement_factor = int(input())

employees = list(map(lambda x: int(x) * happiness_improvement_factor, employees_happiness))
sum_happiness = list(filter(lambda x: x >= (sum(employees) / len(employees)), employees))

if len(sum_happiness) >= len(employees) / 2:
    print(f'Score: {len(sum_happiness)}/{len(employees)}. Employees are happy!')
else:
    print(f'Score: {len(sum_happiness)}/{len(employees)}. Employees are not happy!')
