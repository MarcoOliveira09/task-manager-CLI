task_list = []

while True:
    print('''
    TASK MANAGER
    1 - ADD NEW TASK
    2 - LIST ALL TASKS
    3 - MARK TASK AS COMPLETE
    4 - REMOVE TASK
    5 - EXIT PROGRAM''')

    user_choice = input('Enter an option > ').strip()

    if user_choice == '1':
        while True:
            new_task = input('Add a new task > ').strip()
            if new_task.isdigit():
                print('Enter a valid value!')
            else:
                task_list.append({'text': new_task, 'done': False})
                print(f'New task "{new_task}" added!')
                break

        while True:
            another_task = input('Would you like to add another task? (y/n) > ').strip()
            if another_task.lower().strip() == 'y':
                while True:
                    another_new_task = input('Add a new task > ').strip()
                    if another_new_task.isdigit():
                        print('Enter a valid value!')
                    else:
                        task_list.append({'text': another_new_task, 'done': False})
                        print(f'New task "{another_new_task} added!')
                        break
            elif another_task.strip().lower() == 'n':
                break
            else:
                print('Enter a valid value!')

    elif user_choice == '2':
        if not task_list:
            print('No tasks yet!')
        else:
            for i, task in enumerate(task_list):
                print(f' {i + 1} - {task["text"]}')
            input('Press enter to exit')

    elif user_choice == '3':
        if not task_list:
            print('No tasks yet!')
        else:
            for i, task in enumerate(task_list):
                task_status = 'X' if task['done'] else ' '
                print(f'[{task_status}] {i + 1} - {task["text"]}')
            while True:
                mark_done = input('Which task would like to complete? > ').strip()
                if mark_done.isalpha():
                    print('Enter a valid value!')
                elif not mark_done.isdigit():
                    print('You cannot leave this empty!')
                else:
                    break
            real_indice = int(mark_done) - 1
            if real_indice < 0 or real_indice >= len(task_list):
                print('Enter a valid value!')
            else:
                task_list[real_indice]['done'] = True
                task_status = 'X' if task_list[real_indice]['done'] else ' '
                print(f'[{task_status}] {real_indice + 1} - {task_list[real_indice]["text"]}')
                while True:
                    another_task_done = input('Would you like to complete another task? (y/n) > ').strip()
                    if another_task_done.strip().lower() == 'y':
                        while True:
                            mark_done = input('Which task would like to complete? > ').strip()
                            if not mark_done.isdigit():
                                print('Enter a valid value!')
                            else:
                                real_indice = int(mark_done) - 1
                                break
                        if real_indice < 0 or real_indice >= len(task_list):
                            print('Enter a valid value!')
                        else:
                            task_list[real_indice]['done'] = True
                            task_status = 'X' if task_list[real_indice]['done'] else ' '
                            print(f'[{task_status}] {real_indice + 1} - {task_list[real_indice]["text"]}')
                    else:
                        break

    elif user_choice == '4':
        if not task_list:
            print('No tasks yet!')
        else:
            for i, task in enumerate(task_list):
                print(f'{i + 1} - {task["text"]}')
            while True:
                remove_task = input('Which task would you like to remove? > ').strip()
                if not remove_task.isdigit():
                    print('Enter a valid value!')
                else:
                    break
            real_indice = int(remove_task) - 1
            if real_indice < 0 or real_indice >= len(task_list):
                print('Enter a valid option!')
            else:
                removed_task = task_list.pop(real_indice)
                print(f'Task "{removed_task["text"]}" was removed!')
                while True:
                    another_remove_task = input('Would you like to remove another task? (y/n) > ').strip()
                    if another_remove_task.strip().lower() == 'y':
                        while True:
                            remove_task = input('Which task would you like to remove? > ').strip()
                            if not remove_task.isdigit():
                                print('Enter a valid value!')
                            else:
                                break
                        real_indice = int(remove_task) - 1
                        if real_indice < 0 or real_indice >= len(task_list):
                            print('Enter a valid option!')
                        else:
                            removed_task = task_list.pop(real_indice)
                            print(f'Task {removed_task["text"]} was removed!')
                    else:
                        break


    elif user_choice == '5':
        break

    else:
        print('Enter a valid value!')
