class GroceryItemOrder:
    def __init__(self, name, quantity, price_per_unit):
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def cost(self):
        return self.quantity * self.price_per_unit

    def __str__(self):
        return f"{self.name}: {self.quantity} units at ${self.price_per_unit} each, Total: ${self.cost()}"


class GroceryList:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    @property
    def total_cost(self):
        return sum(item.cost() for item in self.items)

    def __str__(self):
        item_list_str = "\n".join(str(item) for item in self.items)
        return f"Items in Grocery List:\n{item_list_str}\nTotal Cost: ${self.total_cost}"


def create_grocery_item(name, quantity, price_per_unit):
    return GroceryItemOrder(name, quantity, price_per_unit)


def create_grocery_list():
    return GroceryList()


def add_item_to_list(grocery_list, grocery_item):
    grocery_list.add(grocery_item)


def print_grocery_list(grocery_list):
    print(grocery_list)


def main():

    grocery_list = create_grocery_list()

    item1 = create_grocery_item("Apples", 4, 0.5)
    item2 = create_grocery_item("Cookies", 3, 2.0)
    item3 = create_grocery_item("Milk", 2, 1.5)

    add_item_to_list(grocery_list, item1)
    add_item_to_list(grocery_list, item2)
    add_item_to_list(grocery_list, item3)

    print_grocery_list(grocery_list)


if __name__ == "__main__":
    main()
