from random import randint


def generate_dict(array: []):
    new_dict = {str(index): array[index] for index in range(len(array))}
    return new_dict


empty_list = []
for k in range(randint(1, 5)):
    empty_list.append(randint(0, 10))

print(empty_list)
print(generate_dict(empty_list))
