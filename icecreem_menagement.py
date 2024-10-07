menu = {
    "Cookies and Cream": 500,
    "Chocolate": 250,
    "Vanilla": 200,
    "Mint Chocolate Chip": 350,
    "Mango": 220,
    "Cherry": 320,
    "Peach": 250,
    "Rocky Road": 300,
    "Banana": 150,
    "Orange": 170,
}

print("Welcome to Qureshi Ice Cream")
print("\nMenu:")
for item, price in menu.items():
    print(f"{item} = Rs{price}")

order_total = 0

while True:
    item = input("\nEnter the name of the item you want to order: ")
    item = item.title()
    if item in menu:
        print("\nYour order is successful.")
        order_total += menu[item]
        another = input("Do you want to order another item? (yes/no): ")
        if another.lower() != 'yes':
            break
    else:
        print("Please order according to the menu.")

print(f"\nThe total price to pay is: Rs{order_total}")
