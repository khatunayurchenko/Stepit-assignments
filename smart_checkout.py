import sys

#მომხმარებლის მონაცემები
cart_total = 200
user_status = "vip"
has_promo_code = True
loyalty_points = 600
delivery_city = "თბილისი"
is_account_active = True

#cart_total = 120
#user_status = "regular"
#has_promo_code = True
#loyalty_points = 0
#delivery_city = "ქუთაისი"
#is_account_active = True

#cart_total = 90
#user_status = "regular"
#has_promo_code = False
#loyalty_points = 0
#delivery_city = "ბათუმი"
#is_account_active = True

#cart_total = 300
#user_status = "admin"
#has_promo_code = True
#loyalty_points = 0
#delivery_city = "ფოთი"
#is_account_active = True

#cart_total = 100
#user_status = "vip"
#has_promo_code = True
#loyalty_points = 200
#delivery_city = "თბილისი"
#is_account_active = True

#ანგარიშის შემოწმება
if not is_account_active:
    print("ანგარიში დაბლოკილია. შეკვეთა ვერ დამუშავდება.")
    sys.exit()

#კალათის შემოწმება
if cart_total <= 0:
    print("შეცდომა: კალათის ღირებულება უნდა იყოს 0-ზე მეტი.")
    sys.exit()

#ფასდაკლების სისტემა
discount = 0

if user_status == "vip":
    discount = 20

    if loyalty_points >= 500:
        discount = 25

elif user_status == "regular":
    if has_promo_code or cart_total >= 150:
        discount = 10
    else:
        discount = 0

elif user_status == "admin":
    discount = 50

else:
    print("შეცდომა: მომხმარებლის სტატუსი არასწორია.")
    sys.exit()

#ფასდაკლებული თანხის გამოთვლა
discount_amount = cart_total * discount / 100
discounted_total = cart_total - discount_amount

#მიტანის საფასურის გამოთვლა
if delivery_city in ["თბილისი", "ქუთაისი", "ბათუმი"]:
    if discounted_total >= 100:
        delivery_fee = 0
    else:
        delivery_fee = 5
else:
    delivery_fee = 15

#საბოლოო გადასახდელი თანხა
final_total = discounted_total + delivery_fee

#ინვოისის დაბეჭდვა
print("----- შეკვეთის ინვოისი -----")
print(f"საწყისი ფასი: {cart_total:.2f} ლარი")
print(f"ფასდაკლება: {discount}%")
print(f"ფასდაკლების თანხა: {discount_amount:.2f} ლარი")
print(f"მიტანის საფასური: {delivery_fee:.2f} ლარი")
print(f"საბოლოო გადასახდელი: {final_total:.2f} ლარი")
