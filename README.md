# Task Manager

A command-line task manager written in Python. Tasks are saved to a JSON file, so they are still there the next time you open the program.

## Features

- Add one or more tasks
- List all tasks
- Mark a task as complete
- Remove a task
- Input validation (invalid options, non-numeric choices, out-of-range numbers)
- **Data persistence:** tasks are loaded on startup and saved after every change

## What changed in this version

### Data persistence with JSON (new)

Before, tasks lived only in a Python list in memory and disappeared when the program closed. Now:

- `load_tasks()` reads `tasks.json` once, when the program starts.
- `save_tasks(tasks)` writes the whole list back to `tasks.json` after each change (options 1, 3 and 4).
- If the file does not exist (first run), is empty, or is corrupted, `load_tasks()` returns an empty list instead of crashing (`FileNotFoundError` and `json.JSONDecodeError` are handled).
- The file name is stored in a single constant (`TASKS_FILE`), so it is written only once.
- `encoding='utf-8'` and `ensure_ascii=False` keep accented characters intact.

### Code organization

- Only `load_tasks` and `save_tasks` touch the file. The task functions (`new_tasks`, `complete_task`, `remove_tasks`, `show_all_tasks`) work only on the list in memory, so each function has a single responsibility.
- Removed the unused import from the main script.

## How it works

```
START   -> load_tasks()   : tasks.json -> task_list   (read, 'r')
USE     -> add / complete / remove change task_list in memory
CHANGE  -> save_tasks()   : task_list -> tasks.json   (write, 'w')
```

Each task is a dictionary:

```json
{
    "text": "Study Python",
    "done": false
}
```

## Project structure

```
.
├── V2.py           # main program (menu loop)
├── defsdraft.py    # task functions + load_tasks / save_tasks
└── tasks.json      # created automatically on the first save
```

## How to run

Requires Python 3.

```bash
python V2.py
```

## Planned improvements

- [ ] Reject empty task text
- [ ] Show completion status (`[X]`) when listing tasks
- [ ] Simplify `complete_task` and `remove_tasks` (less nesting, no recursion)
- [ ] Undo or confirm when completing a task
- [ ] Priority and due date
- [ ] Search tasks by text
- [ ] Automated tests with `pytest`

## What I learned

- Reading and writing files with `open` and `with` (modes `'r'`, `'w'`, `'a'`)
- Converting Python data to and from JSON with `json.dump` and `json.load`
- Handling expected errors with `try/except`
- Why the order matters: load first, change, then save
- Why functions should do only one thing
