dwarf_dict = {}

while True:
    line_input = input().split(" <:> ")
    if "Once upon a time" in line_input:
        break

    dwarf_name, dwarf_hat_color, dwarf_physics = line_input[0], line_input[1], line_input[2]
    dwarf_physics = int(dwarf_physics)

    if (dwarf_name, dwarf_hat_color) not in dwarf_dict:
        dwarf_dict[(dwarf_name, dwarf_hat_color)] = dwarf_physics
    else:
        if dwarf_physics > dwarf_dict[(dwarf_name, dwarf_hat_color)]:
            dwarf_dict[(dwarf_name,dwarf_hat_color)] = dwarf_physics

hat_color_count = {}

for key in dwarf_dict.keys():
    hat_color = key[1]
    if hat_color not in hat_color_count:
        hat_color_count[hat_color] = 0
    hat_color_count[hat_color] += 1

sorted_dwarfs = sorted(
    dwarf_dict.items(),
    key=lambda item: (-item[1], -hat_color_count[item[0][1]])
)

for (name, color), physics in sorted_dwarfs:
    print(f"({color}) {name} <-> {physics}")