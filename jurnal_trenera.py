surname = input("Введите вашу фамилию: ")
name = input("Введите ваше имя: ")
print(f"Добро пожаловать, {name}! Начинаем принимать зачёт")
print()

sportsmen_count = int(input("Сколько спортсменов сдают зачёт: "))
approaches_count = int(input("Сколько подходов делает каждый: "))
print()

surnames = []
totals = []
norma_done = 0

for i in range(sportsmen_count):
    print(f"--- Спортсмен {i + 1} ---")
    student = input("Фамилия спортсмена: ")

    total = 0
    for j in range(approaches_count):
        result = int(input(f"Подход {j + 1}: "))
        total = total + result

    surnames.append(student)
    totals.append(total)

    if total >= 30:
        print(f"{student}: всего {total} — норматив выполнен")
        norma_done = norma_done + 1
    else:
        print(f"{student}: всего {total} — норматив не выполнен")
    print()

print("Итоговая таблица:")
for i in range(len(surnames)):
    print(f"{i + 1}. {surnames[i]} — {totals[i]}")
print()

print(f"Норматив выполнили: {norma_done} из {sportsmen_count}")
print(f"Всего подтягиваний группы: {sum(totals)}")
print()
print(f"До свидания, {name}!")