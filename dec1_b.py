import re
with open('./dec1_a_data.txt') as data_file:
    lines = data_file.readlines()

sum = 0

numbers = {
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

for line in lines:
    found_dict = {i: val for i in range(len(line)) for val in list(numbers.keys()) if line.startswith(val, i) }
    indices = list(found_dict.keys())
    indices.sort()
    if indices and len(indices) > 0:
        sum += int(numbers[found_dict[indices[0]]] + numbers[found_dict[indices[-1]]])

print(sum)