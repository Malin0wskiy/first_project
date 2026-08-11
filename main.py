from storage import load_tasks, save_tasks
from task_manager import add_task, delete_task, show_tasks, complete_task 


tasks = load_tasks()


def show_menu():
    print("\n=== Менеджер задач ===")
    print("1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Удалить задачу")
    print("4. Отметить задачу выполненной")
    print("5. Выход")


while True:
    show_menu()

    choice = input("Выберите действие: ")

    if choice == "1":
        show_tasks(tasks)


    elif choice == "2":
        new_task = add_task(tasks)

        if new_task is not None:
            save_tasks(tasks)
            print(f"Задача добавлена: {new_task}")


    elif choice == "3":
        removed_task = delete_task(tasks)

        if removed_task is not None:
            save_tasks(tasks)
            print(f"Удалена задача: {removed_task}")


    elif choice == "4":
        result = complete_task(tasks)

        if result:
            save_tasks(tasks)
            print("Задача отмечена как выполненная")


    elif choice == "5":
        print("До свидания!")
        break


    else:
        print("Такого пункта нет")