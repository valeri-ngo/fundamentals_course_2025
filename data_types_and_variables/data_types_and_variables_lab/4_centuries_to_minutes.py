from math import floor
centuries = int(input())

years = floor(centuries * 100)
days = floor(years * 365.2422)
hours = floor(days * 24)
minutes = floor(hours * 60)

print(f'{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')