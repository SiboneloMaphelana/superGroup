def reformat_string(s):
    letters = [char for char in s if char.isalpha()]
    reformatted = []
    upper = True

    letter_index = 0
    for char in s:
        if char.isalpha():
            reformatted.append(letters[letter_index].upper() if upper else letters[letter_index].lower())
            upper = not upper
            letter_index += 1
        else:
            reformatted.append(char)

    return "".join(reformatted)

input_string = " Za^B8g@E2jH*kWl!MoPqXr7YvT1c$Fs3Ud9IwZ&yX0pLkV6sHqN^tB4rA+oZ%gFj"
reformatted_string = reformat_string(input_string)
print(reformatted_string)
