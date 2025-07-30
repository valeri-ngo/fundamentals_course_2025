from math import ceil

class BonusScoringSystem:

    def __init__(self):
        self.max_bonus_pts = 0
        self.max_attendances = 0

    def calculate_bonus(self, attendances, lectures, additional_bonus):
        if lectures == 0:
            return 0
        return attendances / lectures * ( 5 + additional_bonus )

    def main(self):

        number_of_students = int(input())
        number_of_lectures = int(input())
        additional_bonus = int(input())

        for _ in range(number_of_students):
            attendances = int(input())
            bonus = self.calculate_bonus(attendances, number_of_lectures, additional_bonus)

            if bonus >= self.max_bonus_pts:
                self.max_bonus_pts = bonus
                self.max_attendances = attendances

        print(f"Max Bonus: {ceil(self.max_bonus_pts)}.")
        print(f"The student has attended {self.max_attendances} lectures.")

if __name__ == '__main__':
    result = BonusScoringSystem()
    result.main()