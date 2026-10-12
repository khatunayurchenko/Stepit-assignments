

#პროგრამა სთხოვს მომხმარებელს შეიყვანოს თავისი სახელი
user_name = input("Please type your name:\n")
#პროგრამა სთხოვს მომხმარებელს შეიყვანოს თავისი გვარი
user_surname = input("Please type your surname:\n")
#პროგრამა სთხოვს მომხმარებელს შეიყვანოს დაბადების წელი
user_birth_year = int(input("Please type your birth year:\n"))
#პროგრამა სთხოვს მომხმარებელს შეიყვანოს საყვარელი პროგრამირების ენა
user_favourite_language = input("Please type your favourite programming language:\n")

#სახელი და გვარი გადამყავს დიდ ასოებში.
user_name = user_name.upper()
user_surname = user_surname.upper()
#ვანგარიშობ მომხმარებლის ასაკს მიმდინარე წლის (2026) გამოყენებით.
now = 2026
user_age = now - 1982
#ვამოწმებ არია თუ არა მომხმარებელი სრულწლოვანი
is_adult = user_age >=18
#ვბეჭდავ მომხმარებლის ინფორმაციას სეპარატორით |
print(f"{user_name} | {user_surname} | {user_age} | {user_favourite_language} | {is_adult}")

#ვითხოვ მოსწავლის ქულას
student_score = int(input("Please enter your score out of 20:\n"))
#ვასკალირებ 10 ბალიანი სისტემით
grade_out_of_10 = student_score // 2
#ვბეჭდავ ქულას 10 ბალიანით
print(grade_out_of_10)