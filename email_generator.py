#ვთხოვ მომხმარებელს შეიყვანოს თავისი სახელი და ვასუფთავებ
first_name = input("Please type your first name:\n").strip().lower()
#ვთხოვ მომხმარებელს შეიყვანოს თავისი გვარი და ვასუფთავებ
last_name = input("Please type your last name:\n").strip().lower()
#ვთხოვ მომხმარებელს აირჩიოს პლატფორმა
platform = input("Please choose the platform - gmail.com:\n").strip()
#ელფოსტის აწყობა
#ვიღებ სახელის პირველ ორ ასოს
first_two_letter = first_name[0:2]
#ელფოსტის აწყობა
email = f"{first_two_letter}{last_name}@{platform}"
print(email)
print()
print()
print("თქვენი ელფოსტა წარმატებით შეიქმნა!")