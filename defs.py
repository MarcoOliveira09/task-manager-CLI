import json

TASKS_FILE = 'tasks.json'

def load_tasks():
    try:
        with open(TASKS_FILE, 'r', encoding='utf-8') as arq:
            return json.load(arq)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w', encoding='utf-8') as arq:
        json.dump(tasks, arq, indent=4, ensure_ascii=False)

def new_tasks (tasks):
    while True:
            create_task = input('Add a new task > ').strip()
            if create_task.isdigit():
                print('Enter a valid value!')
            else:
                tasks.append({'text': create_task, 'done': False})
                print(f'New task {create_task} added!')
                break
    while True:
        create_another_task = input('Would you like to add another task? (Y/N) > ').strip().lower()
        if create_another_task == 'y':
            new_tasks(tasks)
            return
        elif create_another_task == 'n':
            return
        else:
            print('Enter a valid value!')
            continue

def show_all_tasks (shows_tasks):
        if not shows_tasks:
            print('No tasks yet!')
        else:
            for i, task in enumerate(shows_tasks):
                print(f' {i + 1} - {task["text"]}')
            input('Press enter to exit')
            return

def complete_task (mark_complete):
    if not mark_complete:
        print('No tasks yet!')
    else:
        for i, task in enumerate(mark_complete):
            mark_complete_status = 'X' if task['done'] else ' '
            print(f'[{mark_complete_status}] {i + 1} - {task["text"]}')
        while True:
                mark_complete_task = input('Which task would like to complete? > ').strip()
                try:
                    real_indice = int(mark_complete_task) - 1
                except ValueError:
                    print('You cannot leave this empty or type text! Please enter a valid number.')
                    continue
                if real_indice < 0 or real_indice >= len(mark_complete):
                    print('Enter a valid value!')
                    continue
                else:
                    mark_complete[real_indice]['done'] = True
                    mark_complete_task = 'X' if mark_complete[real_indice]['done'] else ' '
                    print(f'[{mark_complete_task}] {real_indice + 1} - {mark_complete[real_indice]["text"]}')
                while True:
                    another_complete_task = input('Would you like to complete another task? (Y/N) > ').strip().lower()
                    if another_complete_task == 'y':
                        complete_task(mark_complete)
                        return
                    elif another_complete_task == 'n':
                        return
                    else:
                        print('Enter a valid value!')
                        continue

def remove_tasks(remove_task):
    if not remove_task:
        print('No tasks yet!')
    else:
        for i, task in enumerate(remove_task):
            print(f'{i + 1} - {task["text"]}')
        while True:
            user_remove_task = input('Which task would you like to remove? > ').strip()
            if not user_remove_task.isdigit():
                print('Enter a valid value!')
            else:
                try:
                    real_indice = int(user_remove_task) - 1
                except ValueError:
                    print('You cannot leave this empty or type text! Please enter a valid number.')
                    continue
                if real_indice < 0 or real_indice >= len(remove_task):
                    print('Enter a valid option!')
                else:
                    removed_task = remove_task.pop(real_indice)
                    print(f'Task "{removed_task["text"]}" was removed!')
                    while True:
                        another_remove_task = input('Would you like to remove another task? (y/n) > ').strip().lower()
                        if another_remove_task == 'y':
                            remove_tasks(remove_task)
                            return
                        elif another_remove_task == 'n':
                            return