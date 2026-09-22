fio = input("Введите ваш ФИО: ").split()
print(f"Привет, {fio[1]}!")

a = input("Введите первый товар: ")
b = input("Введите второй товар: ")
c = input("Введите третий товар: ")

items_list = [a, b, c]
print(f"Ваш список: {items_list}")
print(f"Товаров в списке: {len(items_list)}")

items_list.append("стакан")
print(f"Список после добавления подарка: {items_list}")

items_list.sort()
print(f"Отсортированный список: {items_list}")

print(f"До свидания, {fio[1][0]}.{fio[2][0]}.{fio[0]}")