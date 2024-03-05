def countLetter(input):
    LETTER = 0
    DIGIT = 0

    for value in range(len(input)):
        if input[value].isalpha():
            LETTER += 1
        if input[value].isdigit():
            DIGIT += 1
    return f"LETTERS {LETTER} DIGITS {DIGIT}"

def upper_and_lower_case(sentence):
    uppercase = 0
    lowercase = 0

    for letter in sentence:
        if letter.isupper():
            uppercase += 1
        if letter.islower():
            lowercase += 1

    # return f"UPPER CASE {uppercase} LOWER CASE {lowercase}"
    return {"UPPER CASE": uppercase, "LOWER CASE": lowercase}




input = "hello world! 123"

print(countLetter(input))