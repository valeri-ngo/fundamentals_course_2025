class BlackFlag:

    def __init__(self, days, expected_plunder, daily_plunder):
        self.days = days
        self.daily_plunder = daily_plunder
        self.expected_plunder = expected_plunder

    def calculate(self):

        total_gain = 0

        for day in range(1, self.days +1):
            total_gain += self.daily_plunder

            if day % 3 == 0:
                total_gain += self.daily_plunder * 0.5

            if day % 5 == 0:

                total_gain *= 0.7

        if total_gain >= self.expected_plunder:
            return f"Ahoy! {total_gain:.2f} plunder gained."
        else:
            percentage = (total_gain / self.expected_plunder) * 100
            return f"Collected only {percentage:.2f}% of the plunder."

def main():

    days = int(input())
    daily_plunder = int(input())
    expected_plunder = float(input())

    game = BlackFlag(days, expected_plunder, daily_plunder)
    result = game.calculate()
    print(result)

if __name__ == '__main__':
    main()