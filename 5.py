palavra = input()
string_len = len(palavra)

reverse_string = []
for i in range(string_len):
    index = (string_len - 1) - i
    letter = palavra[index]
    reverse_string.append(letter)

print(''.join(reverse_string))