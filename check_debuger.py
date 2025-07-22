'''
Є список [1, 2, 3, 4, 5, 6, 7, 8, 9]
Потрібно написати функція, що виводить всі непарні функції з списку
'''

def print_only_odd_of_list(some_list: list) -> list:
    # Пройтися по всіх числах
    # Перевірити чи парне чи ні
    # Вивести у термінал якщо непарне

    final_list = []
    for elem in some_list:
        if elem % 2 == 1:
            final_list.append(elem)

    return(final_list)

    # return(filter(lambda x: x % 2 == 1, some_list))

print(*print_only_odd_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    