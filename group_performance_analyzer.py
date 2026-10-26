# ცარიელი სია ქულების შესანახად
scores = []

print("სტუდენტების ქულების დინამიური ანალიზატორი")
print("შეიყვანეთ ქულები (0-დან 10-მდე). დასასრულებლად ჩაწერეთ 'stop'\n")

# ქულების შეყვანის ციკლი
while True:
    user_input = input("შეიყვანეთ ქულა ან 'stop': ").strip().lower()
    
    # ციკლიდან გამოსვლის პირობა
    if user_input == 'stop':
        break
        
    # try-except ბლოკი არავალიდური მონაცემების დასამუშავებლად
    try:
        score = float(user_input)
        
        # ქულის ვალიდაცია (0-დან 10-მდე)
        if 0 <= score <= 10:
            scores.append(score)
        else:
            print("გაფრთხილება: ქულა უნდა იყოს 0-დან 10-მდე შუალედში!")
            
    except ValueError:
        print("გაფრთხილება: გთხოვთ შეიყვანოთ სწორი რიცხვი ან 'stop'")

# მონაცემების დამუშავება და ბეჭდვა (თუ სია ცარიელი არაა)
if scores:
    # მინიმალურის, მაქსიმალურისა და საშუალოს გამოთვლა
    min_score = min(scores)
    max_score = max(scores)
    avg_score = sum(scores) / len(scores)
    
    # ლამაზად ფორმატირებული სტრინგები
    print("\n" + "="*30)
    print("   კლასის პერფორმანსის ანალიზი")
    print("="*30)
    print(f"• მინიმალური ქულა: {min_score}")
    print(f"• მაქსიმალური ქულა: {max_score}")
    print(f"• საშუალო ქულა:     {avg_score:.2f}")
    print("-"*30)
    
    # ქულების დალაგება ზრდადობით
    sorted_scores = sorted(scores)
    print(f"ყველა ქულა ზრდადობით: {sorted_scores}")
    
    # ქულების გამეორების სიხშირე (უნიკალური ქულების მიხედვით)
    print("ქულების გამეორების სიხშირე:")
    unique_scores = sorted(list(set(scores)))
    for unique_score in unique_scores:
        count = scores.count(unique_score)
        print(f"  - ქულა {unique_score} განმეორდა: {count}-ჯერ")
    print("="*30)
else:
    print("\nანალიზისთვის ქულები არ არის შეყვანილი.")