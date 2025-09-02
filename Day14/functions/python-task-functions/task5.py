# Task 5: Dynamic To-Do List
def update_todo_list(todo_list, *new_tasks, **status_updates):
    """
    Manage a temporary to-do list by adding new tasks and updating task statuses.
    
    Parameters:
    todo_list: Existing dictionary with tasks as keys and their status as values.
    new_tasks: Any number of new tasks to add (status defaults to 'pending').
    status_updates: Key-value pairs to update the status of existing tasks.
    
    Example:
        todos = {}
        update_todo_list(todos, "Wash dishes", "Read book", Read_book="completed")
    """
    for task in new_tasks:
        todo_list[task] = "Pending"
    todo_list["Read book"] = status_updates["Read_book"]
    todo_list["Sweep"] = status_updates["Sweep"]
    print(todo_list)
todo_list = {}
update_todo_list(todo_list,"Wash dishes", "Read book", "Code", "Sweep", Read_book = "Completed", Sweep = "Completed")
