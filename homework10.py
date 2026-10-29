# =========================
# ნაწილი 1 - რეკურსია
# =========================

#ვქმნი ფუნქციას, რომელსაც გადაეცემა რიცხვი n
def factorial_recursive(n):

    #ეს ტექსტი აღწერს ფუნქციის დანიშნულებას
    """Returns the factorial of n using recursion."""

    #ვამოწმებთ, არის თუ არა რიცხვი უარყოფითი
    if n < 0:

        #უარყოფითი რიცხვისთვის ფაქტორიალი არ განისაზღვრება
        return "Factorial is not defined for negative numbers."

    #საბაზისო შემთხვევა (Base Case)
    #თუ n არის 0 ან 1, ფუნქცია აბრუნებს 1-ს
    #აქ რეკურსია ჩერდება
    if n == 0 or n == 1:
        return 1

    #რეკურსიული შემთხვევა (Recursive Case)
    #ფუნქცია საკუთარ თავს იძახებს n - 1 მნიშვნელობით
    #ასე გრძელდება მანამ, სანამ n არ გახდება 1
    #შემდეგ შედეგები ერთმანეთზე მრავლდება
    return n * factorial_recursive(n - 1)


#ფუნქციის გამოძახება და შედეგის გამოტანა
print(factorial_recursive(5))  #120
print(factorial_recursive(0))  #1


# =========================
# ნაწილი 2 - ონლაინ მაღაზია
# =========================

#discount_rate არის ფასდაკლების პროცენტი
#*prices იღებს ნებისმიერი რაოდენობის ფასს
def calculate_cart_total(discount_rate, *prices):

    #ვქმნი ცვლადს საბოლოო თანხისთვის
    total = 0.0

    #ციკლით გადავუვლი თითოეულ ფასს
    for price in prices:

        #ვითვლი ფასს ფასდაკლების შემდეგ
        discounted_price = price - (price * discount_rate / 100)

        #ფასდაკლებულ ფასს ვუმატებ ჯამს
        total += discounted_price

    #ვაბრუნებ საბოლოო თანხას
    return total


#ფუნქციის გამოძახება
print(calculate_cart_total(10, 100, 200, 300))


#ნაწილი 2 - ფუნქცია 2

#**products იღებს პროდუქტების სახელებს და ფასებს
def filter_and_sort_products(**products):

    #ვფილტრავ პროდუქტებს, რომელთა ფასი >= 100
    filtered_products = filter(
        lambda item: item[1] >= 100,
        products.items()
    )

    #ვალაგებ პროდუქტებს ფასის ზრდადობით
    sorted_products = sorted(
        filtered_products,
        key=lambda item: item[1]
    )

    #ვაბრუნებ დალაგებულ ტუპლების სიას
    return sorted_products


#ფუნქციის გამოძახება
print(filter_and_sort_products(
    laptop=2500,
    mouse=50,
    keyboard=150,
    monitor=700
))


# =========================
# ნაწილი 3 - სტუდენტების ანალიზი
# =========================

#სტუდენტების სახელები
names = ["Ana", "Nino", "Luka", "Giorgi", "Mariam"]

#სტუდენტების შესაბამისი ქულები
scores = [45, 82, 91, 38, 74]


#ფუნქცია აერთიანებს სახელებს და ქულებს
def pair_students(names_list, scores_list):

    #zip აერთიანებს სახელებს შესაბამის ქულებთან
    #list გარდაქმნის შედეგს სიად
    paired_data = list(zip(names_list, scores_list))

    #ვაბრუნებთ ტაპლების სიას
    return paired_data


#ფუნქციის გამოძახება
students = pair_students(names, scores)

print(students)


#ფუნქცია არჩევს სტუდენტებს, რომლებმაც ჩააბარეს
def get_passed_students(paired_data, passing_score=60):

    #filter ტოვებს მხოლოდ შესაბამის სტუდენტებს
    passed_students = list(filter(
        lambda student: student[1] >= passing_score,
        paired_data
    ))

    #ვაბრუნებ ჩაბარებული სტუდენტების სიას
    return passed_students


#ფუნქციის გამოძახება
passed = get_passed_students(students)

print(passed)


#reduce ფუნქციის იმპორტი
from functools import reduce


#ფუნქცია ითვლის ჩაბარებული სტუდენტების საშუალო ქულას
def calculate_average_of_passed(passed_students):

    #თუ სია ცარიელია, ვაბრუნებთ 0.0-ს
    if len(passed_students) == 0:
        return 0.0

    #map იღებს მხოლოდ სტუდენტების ქულებს
    scores = list(map(
        lambda student: student[1],
        passed_students
    ))

    #reduce კრებს ყველა ქულას
    total = reduce(lambda a, b: a + b, scores)

    #საშუალო = ქულების ჯამი / სტუდენტების რაოდენობა
    average = total / len(scores)

    #ვაბრუნებთ საშუალო ქულას
    return average


#ფუნქციის გამოძახება
average = calculate_average_of_passed(passed)

print(average)


