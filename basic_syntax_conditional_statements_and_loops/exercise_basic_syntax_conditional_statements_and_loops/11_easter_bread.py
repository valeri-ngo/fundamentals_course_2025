budget = float(input())     ## Budget
flour_price = float(input())        ## Price for 1 kg flour

pack_of_eggs_price = 0.75 * flour_price     ## Price for a pack of eggs
liter_milk_price = 1.25 * flour_price       ## Price for 1 liter of milk

quarter_of_milk = 0.25 * liter_milk_price       ## 250 ml of milk

loaves = 0      ## Counter for loaves made
colored_eggs = 0        ## Counter for colored eggs received
eggs_lost = 0       ## Counter for lost eggs per every 3rd loaf made
single_loaf = pack_of_eggs_price + flour_price + quarter_of_milk       ## Price for a single loaf made

while budget >= single_loaf:        ## Until budget is available
    loaves += 1     ## One loaf received
    budget -= single_loaf       ## One loaf - budget
    colored_eggs += 3       ## Number of colored eggs received

    if loaves % 3 == 0:        ## For every 3rd bread made, you lose colored eggs
        eggs_lost = loaves - 2
        colored_eggs -= eggs_lost

print(f'You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
