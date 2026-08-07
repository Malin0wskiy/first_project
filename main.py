tasks = []


def show_menu():
    print("\n=== Менеджер задач ===")
    print("1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Удалить задачу")
    print("4. Выход")


while True:
    show_menu()

    choice = input("Выберите действие: ")

    if choice == "1":
        if len(tasks) == 0:
            print("У вас пока нет задач")
        else:
            print("\nВаши задачи:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "2":
        task = input("Введите новую задачу: ")
        tasks.append(task)
        print("Задача добавлена!")

    elif choice == "3":
        if len(tasks) == 0:
            print("Нет задач для удаления")
        else:
            print("\nВаши задачи:")

        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

        number = int(input("Введите номер задачи для удаления: "))
        if number > 0 and number <= len(tasks):
            removed_task = tasks.pop(number - 1)
            print(f"Удалена задача: {removed_task}")
        else:
            print("Такой задачи нет")

    elif choice == "4":
        print("До свидания!")
        break

    else:
        print("Такого пункта нет")