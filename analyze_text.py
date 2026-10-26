def analyze_text(text: str, target_word: str):

    # ტექსტის პატარა ასოებად გადაყვანა
    text = text.lower()
    target_word = target_word.lower()

    #ტექსტის სიტყვებად დაყოფა
    words = text.split()

    #სიტყვების საერთო რაოდენობა
    total_words = len(words)

    #საძიებო სიტყვის გამეორებების რაოდენობა
    word_count = words.count(target_word)

    #ყველაზე გრძელი სიტყვის პოვნა
    longest_word = ""

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    #სამი მნიშვნელობის დაბრუნება
    return total_words, word_count, longest_word


#ფუნქციის გამოძახება
text = "Khatuna lives in New York and Khatuna loves skiing"
target_word = "Khatuna"

total, count, longest = analyze_text(text, target_word)

print(f"სიტყვების საერთო რაოდენობა: {total}")
print(f"'{target_word}' მეორდება: {count}-ჯერ")