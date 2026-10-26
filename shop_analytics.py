#ინვენტარის შექმნა
inventory = {
    "laptop": {"price": 2500, "stock": 5},
    "phone": {"price": 1500, "stock": 10},
    "tablet": {"price": 900, "stock": 0}
}

#პროდუქტის დამატება ან განახლება
product_name = input("შეიყვანეთ პროდუქტის სახელი: ").strip().lower()

if product_name in inventory.keys():
    try:
        new_stock = int(input("შეიყვანეთ ახალი რაოდენობა: "))

        if new_stock >= 0:
            inventory[product_name]["stock"] = new_stock
            print("რაოდენობა განახლდა.")
        else:
            print("რაოდენობა არ შეიძლება იყოს უარყოფითი.")

    except ValueError:
        print("გთხოვთ შეიყვანოთ სწორი რიცხვი.")

else:
    try:
        price = float(input("შეიყვანეთ პროდუქტის ფასი: "))
        stock = int(input("შეიყვანეთ პროდუქტის რაოდენობა: "))

        if product_name != "" and price >= 0 and stock >= 0:
            inventory[product_name] = {
                "price": price,
                "stock": stock
            }
            print("ახალი პროდუქტი დაემატა.")
        else:
            print("არასწორი პროდუქტის მონაცემები.")

    except ValueError:
        print("გთხოვთ შეიყვანოთ სწორი რიცხვები.")


#მომხმარებლების სიმრავლეები
active_users = {"khatuna", "giorgi", "toma", "lizi"}
vip_users = {"khatuna", "toma"
"", "alberti"}

all_users = active_users | vip_users
active_vip = active_users & vip_users
regular_active = active_users - vip_users


#სრული ინვენტარი
print("\n----- სრული ინვენტარი -----")

for product, details in inventory.items():
    print(f"{product}: ფასი {details['price']:.2f} ლარი, რაოდენობა {details['stock']}")


#მარაგში არსებული პროდუქტები
print("\n----- მარაგში არსებული პროდუქტები -----")

for product, details in inventory.items():
    if details["stock"] > 0:
        print(f"{product} - {details['stock']} ცალი")


#ყველაზე ძვირადღირებული პროდუქტი
highest_price = -1
most_expensive = ""

for product, details in inventory.items():
    if details["price"] > highest_price:
        highest_price = details["price"]
        most_expensive = product

print("\n----- ყველაზე ძვირადღირებული -----")
print(f"პროდუქტი: {most_expensive}")
print(f"ფასი: {highest_price:.2f} ლარი")


#ინვენტარის ჯამური ღირებულება
total_value = 0

for product, details in inventory.items():
    total_value += details["price"] * details["stock"]

print(f"\nინვენტარის ჯამური ღირებულება: {total_value:.2f} ლარი")


#მომხმარებლების ანალიზი
print("\n----- მომხმარებლების ანალიზი -----")

print(f"ყველა უნიკალური მომხმარებელი: {sorted(all_users)}")
print(f"აქტიური VIP მომხმარებლები: {sorted(active_vip)}")
print(f"აქტიური არა-VIP მომხმარებლები: {sorted(regular_active)}")