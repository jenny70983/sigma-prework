
list_input = input(
    'Please enter a list separated by a comma with no space ",": ')

a_list = []
for n in list_input.split(","):
    a_list.append(int(n))

print(f'This is a list of your numbers: {a_list}')


def find_min_max(a_list):
    a_list.sort()
    return [a_list[0], a_list[-1]]


print(f'These are the [min/max] values: {find_min_max(a_list)}')
