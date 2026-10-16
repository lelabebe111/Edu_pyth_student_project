films = ["дюна", "аватар", "матрица", "интерстеллар", "шрек"]
votes = {}
for film in films:
    votes[film] = 0

organizator = input("Введите ваше имя: ")
print(f"Здравствуйте, {organizator}! Открываем зрительское голосование")
print(f"Фильмы в программе фестиваля: {','.join(films)}")
print()

voters = set()
all_liked = None

while True:
    name = input('Имя зрителя (или "стоп", чтобы закончить) :')
    name = name.strip()

    if name == "":
        continue

    name_key = name.lower()

    if name_key == "стоп":
        break

    if name_key in voters:
        print(f"{name}, вы уже голосовали, второй голос не засчитан")
        print()
        continue

    voters.add(name_key)

    line = input("Какие фильмы вам понравились (через запятую):")
    liked = set()

    for part in line.split(","):
        film = part.strip().lower()
        if film == "":
            continue
        if film in votes:
            liked.add(film)
        else:
            print(f"Фильма {film} нет в программе, голос не засчитан")

    for film in liked:
        votes[film] += 1

    if all_liked is None:
        all_liked = set(liked)
    else:
        all_liked = all_liked & liked

    print(f"Спасибо. {name}! Засчитано голосов {len(liked)}")
    print()

print()
print("Итоги голосвания")
print(f"Прогосовало зрителей:{len(liked)}")
print()

for film in films:
    print(f"{film} - {votes[film]}")

winner = films[0]
for film in films:
    if votes[film] > votes[winner]:
        winner = film
print(f"Победитель: {winner}({votes[winner]})")

if all_liked:
    liked_names = []
    for film in films:
        if film in all_liked:
            liked_names.append(film)
    print(f"Понравились всем: {','.join(liked_names)}")
else:
    print("Фильмов, которые понравились всем нет")

none_films = []
for film in films:
    if votes[film] == 0:
        none_films.append(film)

if none_films:
    print(f"Не выбрал никто {','.join(none_films)}")
else:
    print("Фильмов, за которые не проголосовал никто, нет")

print()
print(f"До свидания, {organizator}!")