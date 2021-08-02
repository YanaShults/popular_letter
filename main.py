
dict = {}
num = 1
s = input("Введите строку: ").lower()

def most_wanted_letter(s):
    for i in s:
        if i.isalpha():
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = num
    if len(dict) == 0:
        print("There are no letters in the string.")
    else:
        letter = max(dict, key=dict.get)
        print(letter)

most_wanted_letter(s)