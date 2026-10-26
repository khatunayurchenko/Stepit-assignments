total = 0
count = 0

while True:
    user_input = input("შეიყვანეთ რიცხვი ან 'stop' დასასრულებლად: ")
    
    #ციკლიდან შეწყვეტის პირობა
    if user_input == "stop":
        break

    #ტექსტის რიცხვად (float) გადაქცევას
    try:
        number = float(user_input)
    
    #შეცდომის დამუშავება არავალიდური ტექსტის შემთხვევაში
    except ValueError:
        print("გთხოვთ შეიყვანოთ მხოლოდ რიცხვი ან 'stop'")
        continue

    #ჯამისა და რაოდენობის განახლება
    total += number
    count += 1

    #მინიმალურისა და მაქსიმალურის განსაზღვრა
    if count == 1:
        minimum = number
        maximum = number
    else:
        if number < minimum:
            minimum = number

        if number > maximum:
            maximum = number
            
#შედეგების ბეჭდვა ციკლის დასრულების შემდეგ
if count > 0:
    print(f"ჯამი: {total}")
    print(f"რაოდენობა: {count}")
    print(f"მაქსიმალური: {maximum}")
    print(f"მინიმალური: {minimum}")
else:
    print("არცერთი რიცხვი არ შეგიყვანიათ.")