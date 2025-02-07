def double_char_in_string(C, S):
    new_string = ""
    for char in S:
        if char == C:
            new_string += char * 2
        else:
            new_string += char
    return new_string


# Ввод
C = 'a'
S = "ananas"
result = double_char_in_string(C, S)
print(result)
