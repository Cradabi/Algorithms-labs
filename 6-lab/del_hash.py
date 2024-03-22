input_string = input()
exit_string = ""

for i in range(len(input_string)):
    actual_ord = ord(input_string[i])
    exit_string += str(actual_ord % len(input_string))

print(hex(int(exit_string)))
