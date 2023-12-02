with open('./dec1_a_data.txt') as data_file:
    lines = data_file.readlines()

sum = 0

for line in lines:
    first_number_index = -1
    last_number_index = -1
    for i in range(len(line)):
        curr_char = line[i]
        if curr_char.isdigit():
            if first_number_index == -1:
                first_number_index = curr_char
            last_number_index = curr_char
    if first_number_index != -1 and last_number_index != -1:
        sum += int(first_number_index + last_number_index)

print(sum)