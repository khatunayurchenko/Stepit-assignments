import re

#მომხმარებლს ვთხოვ ტექსტის შეყვანას
user_input = input("გთხოვთ, შეიყვანეთ ბილეთების რაოდენობა და გადახდილი თანხა: ")
#ტექსტიდან რიცხვების ამოღება
numbers = re.findall(r"-?\d+(?:\.\d+)?", user_input)

#შეცდომების შემოწმება
try:
    #რიცხვების შესაბამის ტიპებში გადამყავს
    ticket_count = int(numbers[0])
    paid_amount = float(numbers[1])

    #ვამოწმებ ბილეთების რაოდენობას
    if ticket_count <= 0:
        raise ValueError("ბილეთების რაოდენობა უნდა იყოს მინიმუმ 1")

    #ბილეთების ჯამური ღირებულება
    ticket_price = 15
    total_price = ticket_count * ticket_price

    #ვამოწმებ გადახდილ თანხას
    if paid_amount < total_price:
        raise ValueError("თანხა არ არის საკმარისი")

#შეცდომების დამუშავება
except IndexError:
    print("შეცდომა: მიუთითეთ ბილეთების რაოდენობა და გადახდილი თანხა.")
except ValueError as error:
    print(f"შეცდომა: {error}")

#წარმატებული ჯავშანი
else:
    change = paid_amount - total_price

    print("ჯავშანი წარმატებით შესრულდა!")
    print(f"ბილეთების რაოდენობა: {ticket_count}")
    print(f"ჯამური ღირებულება: {total_price:.2f} ლარი")
    print(f"გადახდილი თანხა: {paid_amount:.2f} ლარი")
    print(f"ხურდა: {change:.2f} ლარი")

#საბოლოო შეტყობინება
finally:
    print("[სისტემა]: ტრანზაქციის მცდელობა დასრულდა.")