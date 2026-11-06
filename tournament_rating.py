def total(*scores):
    return sum(scores)


def parse_line(line):
    words = line.split()
    if not words:
        raise ValueError("пустая строка")

    name, *raw_scores = words

    if not raw_scores:
        raise ValueError("нет очков")

    scores = [int(x) for x in raw_scores]
    return name, scores


def make_rating(totals):
    return sorted(totals.items(), key=lambda item: (-item[1], item[0]))


def print_rating(rating):
    for place, (name, score) in enumerate(rating, start=1):
        print(f"{place}. {name} — {score}")


def ask_top_count(max_count):
    while True:
        raw = input(f"Сколько лучших показать (1-{max_count}): ")
        try:
            n = int(raw)
            if n < 1 or n > max_count:
                raise ValueError(f"нужно число от 1 до {max_count}")
            return n
        except ValueError as e:
            print(f"Ошибка: {e}")


def main():
    results = {}

    print("Вводите результаты: имя и очки через пробел. Чтобы закончить, введите «стоп».")

    while True:
        line = input("> ")
        if line.strip() == "стоп":
            break

        try:
            name, scores = parse_line(line)
        except ValueError as e:
            print("Строка пропущена:", e)
            continue

        results.setdefault(name, []).extend(scores)

    totals = {}
    for name, scores in results.items():
        totals[name] = total(*scores)

    rating = make_rating(totals)

    print()
    print("--- Рейтинг ---")
    print_rating(rating)

    ten_players = sorted(
        name for name, scores in results.items() if 10 in scores
    )

    print()
    if ten_players:
        print("Набирали 10 очков: " + ", ".join(ten_players))
    else:
        print("Набирали 10 очков: никто")

    if not rating:
        print("Рейтинг пуст.")
        return

    print()
    count = ask_top_count(len(rating))

    print()
    print(f"--- Топ-{count} ---")
    print_rating(rating[:count])


if __name__ == "__main__":
    main()