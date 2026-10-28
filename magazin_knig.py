FILENAME = "catalog.txt"

def load_catalog(filename):
    catalog = {}
    try:
        with open(filename, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(";")
                if len(parts) != 4:
                    print(f"Предупреждение: некорректная строка пропущена: {line}")
                    continue
                try:
                    book_id = int(parts[0])
                    price = int(parts[2])
                    quantity = int(parts[3])
                except ValueError:
                    print(f"Предупреждение: неверные числовые данные, строка пропущена: {line}")
                    continue

                if book_id <= 0:
                    print(f"Предупреждение: id должен быть > 0, строка пропущена: {line}")
                    continue
                if price <= 0:
                    print(f"Предупреждение: цена должна быть > 0, строка пропущена: {line}")
                    continue
                if quantity < 0:
                    print(f"Предупреждение: количество не может быть < 0, строка пропущена: {line}")
                    continue

                if book_id in catalog:
                    print(f"Предупреждение: повторяющийся id {book_id}, строка пропущена.")
                    continue
                catalog[book_id] = (parts[1], price, quantity)
    except FileNotFoundError:
        print(f"Файл {filename} не найден. Каталог пуст.")
        return {}
    return catalog

def save_catalog(filename, catalog):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for book_id in sorted(catalog):
                title, price, quantity = catalog[book_id]
                print(f"{book_id};{title};{price};{quantity}", file=f)
    except OSError as e:
        print(f"Ошибка сохранения файла {filename}: {e}")
        return False
    print(f"Каталог сохранён в файл {filename}.")
    return True

def print_catalog(catalog):
    if not catalog:
        print("Каталог пуст.")
        return
    print()
    print("Каталог:")
    for book_id in sorted(catalog):
        title, price, quantity = catalog[book_id]
        if quantity == 0:
            print(f"{book_id}. {title} — {price} руб., нет в наличии")
        else:
            print(f"{book_id}. {title} — {price} руб., остаток: {quantity}")

def add_book(catalog):
    try:
        book_id = int(input("ID новой книги: "))
    except ValueError:
        print("ID должен быть целым числом.")
        return False

    if book_id <= 0:
        print("ID должен быть положительным целым числом.")
        return False

    if book_id in catalog:
        print(f"Книга с ID {book_id} уже есть в каталоге.")
        return False

    title = input("Название: ").strip()
    if not title:
        print("Название не может быть пустым.")
        return False

    try:
        price = int(input("Цена: "))
    except ValueError:
        print("Цена должна быть целым числом.")
        return False
    if price <= 0:
        print("Цена должна быть больше 0.")
        return False

    try:
        quantity = int(input("Количество: "))
    except ValueError:
        print("Количество должно быть целым числом.")
        return False
    if quantity < 0:
        print("Количество не может быть отрицательным.")
        return False

    catalog[book_id] = (title, price, quantity)
    print(f"Книга «{title}» добавлена.")
    return True

def delete_book(catalog):
    try:
        book_id = int(input("ID книги: "))
    except ValueError:
        print("ID должен быть целым числом.")
        return False

    if book_id not in catalog:
        print(f"Книги с ID {book_id} нет в каталоге.")
        return False

    title = catalog.pop(book_id)[0]
    print(f"Книга «{title}» удалена.")
    return True

def change_price(catalog):
    try:
        book_id = int(input("ID книги: "))
    except ValueError:
        print("ID должен быть целым числом.")
        return False

    if book_id not in catalog:
        print(f"Книги с ID {book_id} нет в каталоге.")
        return False

    try:
        new_price = int(input("Новая цена: "))
    except ValueError:
        print("Цена должна быть целым числом.")
        return False
    if new_price <= 0:
        print("Цена должна быть больше 0.")
        return False

    title, _, quantity = catalog[book_id]
    catalog[book_id] = (title, new_price, quantity)
    print(f"Цена книги «{title}» изменена на {new_price} руб.")
    return True

def change_quantity(catalog):
    try:
        book_id = int(input("ID книги: "))
    except ValueError:
        print("ID должен быть целым числом.")
        return False

    if book_id not in catalog:
        print(f"Книги с ID {book_id} нет в каталоге.")
        return False

    try:
        new_quantity = int(input("Новое количество: "))
    except ValueError:
        print("Количество должно быть целым числом.")
        return False
    if new_quantity < 0:
        print("Количество не может быть отрицательным.")
        return False

    title, price, _ = catalog[book_id]
    catalog[book_id] = (title, price, new_quantity)
    print(f"Количество книги «{title}» изменено на {new_quantity}.")
    return True

def main():
    catalog = load_catalog(FILENAME)
    print(f"Файл {FILENAME} загружен. Книг в каталоге: {len(catalog)}")

    print()
    print("Меню:")
    print("1 — показать каталог")
    print("2 — добавить книгу")
    print("3 — удалить книгу")
    print("4 — изменить цену")
    print("5 — изменить количество")
    print("0 — сохранить и выйти")

    while True:
        try:
            choice = int(input("Выберите пункт: "))
        except ValueError:
            print("Пункт меню должен быть целым числом.")
            continue

        if choice == 1:
            print_catalog(catalog)
        elif choice == 2:
            add_book(catalog)
        elif choice == 3:
            delete_book(catalog)
        elif choice == 4:
            change_price(catalog)
        elif choice == 5:
            change_quantity(catalog)
        elif choice == 0:
            save_catalog(FILENAME, catalog)
            print("До свидания!")
            break
        else:
            print("Такого пункта меню нет.")


if __name__ == "__main__":
    main()