fire_input = input()
current_water = int(input())

cells_put_out = []
fire_extinguished = 0
effort_given = 0
fire_cells = fire_input.split('#')

for current_cell in fire_cells:
    type_of_fire, value_of_cell = current_cell.split(' = ')
    value_of_cell = int(value_of_cell)

    if (type_of_fire == 'High' and 81 <= value_of_cell <= 125) or \
        (type_of_fire == 'Medium' and 51 <= value_of_cell <= 80) or \
        (type_of_fire == 'Low' and 1 <= value_of_cell <= 50):
        if current_water >= value_of_cell:
            current_water -= value_of_cell
            fire_extinguished += value_of_cell
            effort_given += value_of_cell * 0.25
            cells_put_out.append(value_of_cell)
        else:
            continue
    else:
        continue


print(f'Cells:')
for cells in cells_put_out:
    print(f' - {cells}')
print(f'Effort: {effort_given:.2f}')
print(f'Total Fire: {fire_extinguished}')
