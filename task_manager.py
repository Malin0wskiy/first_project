def add_task(tasks):
    task = input("Введите новую задачу: ")

    if task.strip() == "":
        print("Ошибка: задача не может быть пустой")
        return None

    tasks.append({
    "text": task,
    "done": False
})
    
    return task


def delete_task(tasks):
    if len(tasks) == 0:
        print("Нет задач для удаления")
        return

    print("\nВаши задачи:")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['text']}")

    try:
        number = int(input("Введите номер задачи для удаления: "))

        if number > 0 and number <= len(tasks):
            removed_task = tasks.pop(number - 1)
            return removed_task
        else:
            print("Такой задачи нет")

    except ValueError:
        print("Ошибка: нужно ввести число")

def complete_task(tasks):
    if len(tasks) == 0:
        print("Нет задач для выполнения")
        return

    print("\nВаши задачи:")

    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else ""
        print(f"{index}. {task['text']} {status}")

    try:
        number = int(input("Введите номер выполненной задачи: "))

        if number > 0 and number <= len(tasks):
            tasks[number - 1]["done"] = True
            return True
        else:
            print("Такой задачи нет")

    except ValueError:
        print("Ошибка: нужно ввести число")


def show_tasks(tasks):
    if len(tasks) == 0:
        print("У вас пока нет задач")
    else:
        print("\nВаши задачи:")

        for index, task in enumerate(tasks, start=1):
            status = "✓" if task["done"] else ""
            print(f"{index}. {task['text']} {status}")
