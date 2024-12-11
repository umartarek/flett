import flet as ft

def main(page: ft.Page):
    page.title = "Task Manager"

    # List to store tasks
    tasks = []

    # Function to add a task
    def add_task(e):
        if task_input.value.strip():
            tasks.append(task_input.value)
            task_input.value = ""  # Clear the input field
            update_tasks()

    # Function to delete a task
    def delete_task(e):
        tasks.remove(e.control.data)
        update_tasks()

    # Function to mark a task as complete
    def complete_task(e):
        index = tasks.index(e.control.data)
        tasks[index] += " (completed)"
        update_tasks()

    # Function to update the task list UI
    def update_tasks():
        task_list.controls.clear()
        for task in tasks:
            task_list.controls.append(
                ft.Row([
                    ft.Text(task, expand=True),
                    ft.IconButton(ft.icons.CHECK, on_click=complete_task, data=task),
                    ft.IconButton(ft.icons.DELETE, on_click=delete_task, data=task),
                ])
            )
        page.update()

    # UI Elements
    task_input = ft.TextField(hint_text="Enter a task")
    add_button = ft.ElevatedButton("Add Task", on_click=add_task)
    task_list = ft.Column()

    page.add(
        ft.Column([
            ft.Row([task_input, add_button]),
            task_list
        ])
    )

# Run the app
ft.app(target=main)
