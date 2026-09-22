surname = input("Введите вашу фамилию: ")
name = input("Введите ваше имя: ")
print(f"Добро пожаловать, {name}! Начинаем приём заявок")
print()

total = 0
enroll = 0

while True:
    student = input('Фамилия абитуриента (или "завершить", чтобы закончить приём): ')

    if student == "завершить":
        break

    score = int(input("Балл абитуриента: "))
    diploma = input("Есть ли диплом олимпиады? (да/нет): ")

    if score >= 220:
        print(f"{student}: заявка одобрена")
        enroll = enroll + 1
    elif diploma == "да" and score >= 180:
        print(f"{student}: заявка одобрена")
        enroll = enroll + 1
    else:
        print(f"{student}: заявка отклонена")

    total = total + 1
    print()

print(f"Рассмотрено абитуриентов: {total}")
print(f"Зачислено: {enroll}")
print()
print(f"До свидания, {name}!")