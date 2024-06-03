# dictionary data types used

# hotel Menu


menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 80
}
# print(menu)

print("Welcome to Python Restaurant")
print("Pizza  Rs:40 \nPasta Rs:50 \nBurger Rs:60 \nSalad Rs:80")

order_total = 0
#80 + 70 = 150

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1] #0+50 = 50
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet")

another_order = input("Do yo want to add another item ? (yes/No)")
if another_order == "yes":
    item_2 = input("Enter the name of second item =")
    if item_1 in menu:
        order_total +=menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"ordered item {item_2} is not available")
print(f"The total amount of items to pay is {order_total}")



