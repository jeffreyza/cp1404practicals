def main():
    items_number = int(input("How many items? "))
    total_price = 0
    while items_number < 0:
        print("invalid")
        items_number = int(input("How many items? "))
    for i in range(items_number):
        price = float(input("What is the item price? "))
        total_price = total_price + price
    if total_price > 100:
        total_price = total_price * 0.9

    print("Number of items: ", items_number)
    print("Price of item:", price)
    print("Total price of ", items_number, "items is ${:.2f}".format(total_price))


main()
