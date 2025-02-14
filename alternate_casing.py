def reformat_string(s):

    reformatted = ""
    upper = True  # Start with uppercase
    alphabet_chararacters = []

    # Separate alphabetic characters and others
    for char in s:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            alphabet_chararacters.append(char)
        else:
            reformatted += char 

    alpha_index = 0
    for char in s:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            current_alpha = alphabet_chararacters[alpha_index]
            if upper:
                reformatted += current_alpha.upper()
            else:
                reformatted += current_alpha.lower()
            upper = not upper  
            alpha_index += 1
        
    return reformatted



input_string = "Za^B8g@E2jH*kWl!MoPqXr7YvT1c$Fs3Ud9IwZ&yX0pLkV6sHqN^tB4rA+oZ%gFj"
reformatted_string = reformat_string(input_string)
print(reformatted_string)
