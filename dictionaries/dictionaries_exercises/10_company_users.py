company_users = {}

while True:
    user_input = input()
    if user_input == "End":
        break

    company, employee_id = user_input.split(" -> ")
    if company not in company_users.keys():
        company_users[company] = []

    if employee_id not in company_users[company]:
        company_users[company].append(employee_id)

for company, employees in company_users.items():
    print(company)
    for employee_id in employees:
        print(f"-- {employee_id}")