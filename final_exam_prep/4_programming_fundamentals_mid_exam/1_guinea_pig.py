def decrease_food(food: float):
    return food - 0.3

def decrease_hay(hay: float, food: float):
    return hay - food * 0.05

def decrease_cover(cover: float, guinea_weight: float):
    return cover - (guinea_weight / 3)

def main():
    food = float(input())
    hay = float(input())
    cover = float(input())
    guinea_pig_weight = float(input())


    for day in range(1, 30 +1):

        food = decrease_food(food)

        if food <= 0.3:
            print("Merry must go to the pet store!")
            break

        if day % 2 == 0:
            hay = decrease_hay(hay, food)
            if hay <= 0:
                print("Merry must go to the pet store!")
                break

        if day % 3 == 0:
            cover = decrease_cover(cover, guinea_pig_weight)
            if cover <= 0:
                print("Merry must go to the pet store!")
                break

    else:
        print(f'Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.')

if __name__ == '__main__':
    main()