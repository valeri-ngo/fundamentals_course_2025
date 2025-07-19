wealth_per_person = list(map(int, input().split(', ')))
minimum_wealth = int(input())
total_wealth = sum(wealth_per_person)

if total_wealth < minimum_wealth * len(wealth_per_person):
    print('No equal distribution possible')
else:
    while min(wealth_per_person) < minimum_wealth:
        poorest_person = wealth_per_person.index(min(wealth_per_person))
        richest_person = wealth_per_person.index(max(wealth_per_person))

        needed = minimum_wealth - wealth_per_person[poorest_person]
        available = wealth_per_person[richest_person] - minimum_wealth
        if available <= 0:
            print('No equal distribution possible')
            break
        if available >= needed:
            wealth_per_person[richest_person] -= needed
            wealth_per_person[poorest_person] += needed
        else:
            wealth_per_person[richest_person] -= available
            wealth_per_person[poorest_person] += available
    print(wealth_per_person)