my_list = range(1, 17)


# for number in my_list:
# print(number)


def task2(value):
    new_list = []
    for item in value:
        new_list.append(item)
        new_list.append(item)
    return new_list


def task3(value):
    new_list = []
    for number in value:
        if number not in new_list:
            new_list.append(number)
    return new_list


def task4(value):
    count = 0
    sum = 0
    for i in range(len(value)):
        count += 1
        if (count % 3 == 0):
            sum += value[i]
    return sum


def task5(value):
    sum = 0
    if len(value) % 2 == 1:
        middle_number = len(value) // 2 + 1
        sum += value[0] + value[middle_number] + value[-1]
    else:
        first_middle_number = len(value) // 2
        second_middle_number = len(value) // 2 + 1
        print(value[0])
        print(first_middle_number)
        print(second_middle_number)
        print(value[len(value) - 1])
        sum += value[0] + value[first_middle_number] + value[second_middle_number] + value[-1]
    return sum

def task6(value):
    elements = set()
    for i in range(len(value)):
        elements.add(value[i])
    return elements

task5(my_list)