import re

places_string = input()

filter_for_string = r'([=/])([A-Z][a-zA-Z]{2,})\1'
places_after_filter = re.finditer(filter_for_string, places_string)

sum_destination_length = 0
destinations = []

for match in places_after_filter:
    destination = match.group(2)
    destinations.append(destination)
    sum_destination_length += len(destination)

print(f"Destinations: {', '.join(destinations)}")
print(f'Travel Points: {sum_destination_length}')
