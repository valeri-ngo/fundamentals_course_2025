class Zoo:
    __animals = 0

    def __init__(self, name: str):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species__:str, name:str):
        if species__ == 'mammal':
            self.mammals.append(name)
        elif species__ == 'fish':
            self.fishes.append(name)
        elif species__ == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == 'mammal':
            result += f"Mammals in {self.name}: {', '.join(self.mammals)} \n"
        elif species == 'fish':
            result += f"Fishes in {self.name}: {', '.join(self.fishes)} \n"
        elif species == 'bird':
            result += f"Birds in {self.name}: {', '.join(self.birds)} \n"

        result += f"Total animals: {Zoo.__animals}"
        return result

zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())

for index in range(count):
    animals = input().split()
    species = animals[0]
    name = animals[1]
    zoo.add_animal(species, name)

info = input()
print(zoo.get_info(info))