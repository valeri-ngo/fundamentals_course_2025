countries = input().split(", ")
cities = input().split(", ")
summary_capitals = {countries[index]:cities[index]for index in range(len(countries))}

for country, capital in summary_capitals.items():
    print(f"{country} -> {capital}")
