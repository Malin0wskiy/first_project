from storage import load_tasks, save_tasks
from task_manager import add_task, delete_task, show_tasks


tasks = load_tasks()


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
        show_tasks(tasks)


    elif choice == "2":
        add_task(tasks)
        save_tasks(tasks)


    elif choice == "3":
        delete_task(tasks)
        save_tasks(tasks)


    elif choice == "4":
        print("До свидания!")
        break


    else:
        print("Такого пункта нет")