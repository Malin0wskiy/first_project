def add_task(tasks):
    task = input("Введите новую задачу: ")
    tasks.append(task)
    print("Задача добавлена!")


def delete_task(tasks):
    if len(tasks) == 0:
        print("Нет задач для удаления")
        return

    print("\nВаши задачи:")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    try:
        number = int(input("Введите номер задачи для удаления: "))

        if number > 0 and number <= len(tasks):
            removed_task = tasks.pop(number - 1)
            print(f"Удалена задача: {removed_task}")
        else:
            print("Такой задачи нет")

    except ValueError:
        print("Ошибка: нужно ввести число")