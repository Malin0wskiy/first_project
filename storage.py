import json


def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

            for task in tasks:
                if isinstance(task, str):
                    task_index = tasks.index(task)
                    tasks[task_index] = {
                        "text": task,
                        "done": False
                    }

            return tasks

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Ошибка: файл tasks.json повреждён")
        return []


def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)