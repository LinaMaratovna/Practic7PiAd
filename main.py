import random  # Импортируем модуль random для генерации случайных чисел


class DetskiySad:  # Объявляем класс "Детский сад"
    # Атрибуты класса (общие для всех экземпляров)
    institution = "Детский сад № 7"  # Название учреждения
    max_capacity = 25  # Максимальная вместимость группы

    def __init__(self, group_name, children_count, sick_count):  # Конструктор класса
        # Атрибуты экземпляра
        self.group_name = group_name  # Название группы
        self.children_count = children_count  # Количество детей в группе
        self.sick_count = sick_count  # Количество заболевших детей

    def show_info(self):  # Метод вывода полной информации об объекте
        print("\n" + "=" * 50)
        print(f"Учреждение: {DetskiySad.institution}")
        print(f"Группа: {self.group_name}")
        print(f"Количество детей: {self.children_count}")
        print(f"Количество заболевших: {self.sick_count}")
        print(f"Максимальная вместимость: {DetskiySad.max_capacity}")
        if hasattr(self, "educator"):  # Проверяем наличие дополнительного атрибута
            print(f"Воспитатель: {self.educator}")
        else:
            print("Воспитатель: не назначен")
        print("=" * 50)

    def change_count(self, operation):  # Метод увеличения (+) или уменьшения (-) показателей на 1
        if operation == "+":
            self.children_count += 1
            self.sick_count += 1
            print("Количество детей и заболевших увеличено на 1")
        elif operation == "-":
            if self.children_count > 0:
                self.children_count -= 1
            if self.sick_count > 0:
                self.sick_count -= 1
            print("Количество детей и заболевших уменьшено на 1")
        else:
            print("Неверная операция! Используйте только '+' или '-'")

    def add_educator(self, name):  # Метод добавления дополнительного атрибута экземпляра
        self.educator = name
        print(f"Дополнительный атрибут добавлен: воспитатель — {name}")


def main():  # Главная функция программы
    print("=== Практическая работа № 7. Вариант 3: Детский сад ===\n")

    # Исходные данные о группах (название группы)
    starting_groups = [  # Создаём список названий групп
        "Солнышко",
        "Радуга",
        "Звёздочка",
        "Ромашка",
        "Василёк"
    ]

    groups = []  # Создаём пустой список, в который будем добавлять объекты классов

    for name in starting_groups:  # Проходим по каждому названию группы
        children = random.randint(12, 24)  # Генерируем случайное количество детей от 12 до 24
        sick = random.randint(0, 6)  # Генерируем случайное количество заболевших от 0 до 6
        group = DetskiySad(name, children, sick)  # Создаём экземпляр класса
        groups.append(group)  # Добавляем объект в список

    # Добавляем дополнительного атрибута (воспитателя) только первым двум группам
    groups[0].add_educator("Иванова Мария Петровна")
    groups[1].add_educator("Петрова Анна Сергеевна")

    print("1. Исходная информация о группах:")  # Выводим заголовок первой части
    print(f"{'Группа':<12} {'Дети':<8} {'Заболевшие':<12} {'Воспитатель'}")
    print("-" * 50)

    for group in groups:  # Проходим по всем созданным группам
        educator = getattr(group, "educator", "не назначен")  # Получаем воспитателя или значение по умолчанию
        print(f"{group.group_name:<12} {group.children_count:<8} {group.sick_count:<12} {educator}")

    # Открываем файл для записи исходной информации (кодировка UTF-8)
    with open(r"C:\Users\ИСП-31\Desktop\kindergarten_initial.txt", "w", encoding="utf-8") as f:
        f.write(f"{'Группа':<12} {'Дети':<8} {'Заболевшие':<12} {'Воспитатель'}\n")
        f.write("-" * 50 + "\n")
        for group in groups:
            educator = getattr(group, "educator", "не назначен")
            f.write(f"{group.group_name:<12} {group.children_count:<8} {group.sick_count:<12} {educator}\n")

    # Фильтруем группы, в которых заболевших больше 3
    problem_groups = [g for g in groups if g.sick_count > 3]

    print("\n2. Группы с количеством заболевших больше 3:")  # Выводим заголовок второй части
    print(f"{'Группа':<12} {'Дети':<8} {'Заболевшие':<12}")
    print("-" * 40)

    for group in problem_groups:
        print(f"{group.group_name:<12} {group.children_count:<8} {group.sick_count:<12}")

    # Открываем файл для записи проблемных групп
    with open(r"C:\Users\ИСП-31\Desktop\problem_groups.txt", "w", encoding="utf-8") as f:
        f.write(f"{'Группа':<12} {'Дети':<8} {'Заболевшие':<12}\n")
        f.write("-" * 40 + "\n")
        for group in problem_groups:
            f.write(f"{group.group_name:<12} {group.children_count:<8} {group.sick_count:<12}\n")

    # Считаем общее количество заболевших во всех группах
    total_sick = sum(g.sick_count for g in groups)

    print(f"\nОбщее количество заболевших детей: {total_sick}")

    # Открываем файл для записи общей статистики
    with open(r"C:\Users\ИСП-31\Desktop\sick_total.txt", "w", encoding="utf-8") as f:
        f.write(f"Общее количество заболевших детей: {total_sick}\n")

    # --- Интерактивная часть с + и - ---
    print("\n--- Управление количеством детей и заболевших ---")
    print("Введите '+' чтобы увеличить показатели на 1")
    print("Введите '-' чтобы уменьшить показатели на 1")
    print("Введите 'info' чтобы посмотреть текущее состояние всех групп")
    print("Введите 'exit' для выхода\n")

    while True:
        choice = input("Команда (+ / - / info / exit): ").strip().lower()

        if choice == "exit":
            print("Работа программы завершена.")
            break
        elif choice == "info":
            for group in groups:
                group.show_info()
        elif choice in ("+", "-"):
            print("\nВыберите группу:")
            for i, group in enumerate(groups, 1):
                print(f"{i} — {group.group_name}")
            group_choice = input("Номер группы: ").strip()

            if group_choice.isdigit() and 1 <= int(group_choice) <= len(groups):
                selected = groups[int(group_choice) - 1]
                selected.change_count(choice)
                selected.show_info()
            else:
                print("Неверный номер группы!")
        else:
            print("Неизвестная команда!")


main()  # Вызываем главную функцию, чтобы программа начала работу