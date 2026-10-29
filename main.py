from defs import *

task_list = load_tasks()

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
        new_tasks(task_list)
        save_tasks(task_list)
    elif user_choice == '2':
        show_all_tasks(task_list)
    elif user_choice == '3':
        complete_task(task_list)
        save_tasks(task_list)
    elif user_choice == '4':
       remove_tasks(task_list)
       save_tasks(task_list)
    elif user_choice == '5':
        break
    else:
        print('Enter a valid value!')
