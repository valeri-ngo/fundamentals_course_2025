class BakeryShop():

    def __init__(self):
        self.stocks = {}
        self.commands = {
            'Receive': self.receive,
            'Sell': self.sell
        }
        self.sold = 0

    def receive(self, quantity: int, food):
        """
        Adds the given quantity to the food stock.
        If the food is not in the stock, it adds it.
        Ignores invalid (zero or negative) quantities.
        """

        quantity = int(quantity)

        if quantity <= 0:
            return

        if food not in self.stocks:
            self.stocks[food] = quantity
        else:
            self.stocks[food] += quantity

    def sell(self, quantity: int, food: str):
        """
        Sells the requested quantity of a food.
        - If the food is not available, notifies the user.
        - If the quantity is insufficient, sells what's available and removes it from stock.
        - If the quantity is sufficient, updates the stock and removes the item if empty.
        """
        quantity = int(quantity)

        if food not in self.stocks:
            print(f"You do not have any {food}.")
            return

        available_stock = self.stocks[food]

        if available_stock < quantity:
            self.sold += available_stock
            del self.stocks[food]
            print(f"There aren't enough {food}. You sold the last {available_stock} of them.")
            return

        else:
            self.stocks[food] -= quantity
            self.sold += quantity
            if self.stocks[food] == 0:
                del self.stocks[food]
            print(f'You sold {quantity} {food}.')

    def main(self):
        """
        Main loop to process user commands.
        Accepts 'Receive' and 'Sell' until 'Complete' is received.
        Prints the final stock and total sold items.
        """

        while True:

            stocks = input()

            if stocks == 'Complete':
                break

            stock_parts = stocks.split()

            command = stock_parts[0]
            arguments = stock_parts[1:]

            if command in self.commands:
                self.commands[command](*arguments)

        for food, qty in self.stocks.items():
            print(f"{food}: {qty}")
        print(f"All sold: {self.sold} goods")

if __name__ == '__main__':
    result = BakeryShop()
    result.main()