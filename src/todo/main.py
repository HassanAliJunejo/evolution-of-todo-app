"""Main CLI application for the todo app."""
import sys
import re
from typing import List
from src.todo.manager import TodoManager
from src.todo.exceptions import TaskNotFoundError


def display_help():
    """Display available commands."""
    print("Available commands:")
    print("  add \"title\" \"description\"    - Add a new task")
    print("  list                         - View all tasks")
    print("  update id \"title\" \"description\" - Update a task")
    print("  complete id                  - Mark a task as complete")
    print("  delete id                    - Delete a task")
    print("  help                         - Show this help message")
    print("  quit                         - Exit the application")


def display_tasks(tasks):
    """Display tasks in a formatted list."""
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        status_indicator = "[x]" if task.status == "completed" else "[ ]"
        print(f"{task.id}. {status_indicator} {task.title} - {task.description}")


def main():
    """Main application loop."""
    print("Welcome to the Todo App!")
    print("Type 'help' for available commands or 'quit' to exit.")

    todo_manager = TodoManager()

    while True:
        try:
            command_input = input("\n> ").strip()
            if not command_input:
                continue

            # Use regex to handle quoted arguments
            pattern = r'add\s+"([^"]*)"\s+"([^"]*)"'
            match = re.match(pattern, command_input)

            if command_input.lower().startswith("add "):
                if match:
                    title, description = match.groups()
                    try:
                        task_id = todo_manager.add_task(title, description)
                        print(f"Added task #{task_id}: {title}")
                    except ValueError as e:
                        print(f"Error: {e}")
                else:
                    print("Invalid add command format. Use: add \"title\" \"description\"")
            elif command_input.lower() == "list":
                tasks = todo_manager.get_all_tasks()
                display_tasks(tasks)
            elif command_input.lower().startswith("complete "):
                parts = command_input.split()
                if len(parts) != 2:
                    print("Invalid complete command format. Use: complete id")
                else:
                    try:
                        task_id = int(parts[1])
                        success = todo_manager.mark_complete(task_id)
                        if success:
                            print(f"Task #{task_id} marked as complete")
                        else:
                            print(f"Failed to mark task #{task_id} as complete")
                    except ValueError:
                        print("Task ID must be a number")
                    except TaskNotFoundError:
                        print(f"Task with ID {parts[1]} not found")
            elif command_input.lower().startswith("update "):
                # Parse update command: update id "new title" "new description"
                parts = command_input.split(maxsplit=1)
                if len(parts) < 2:
                    print("Invalid update command format. Use: update id \"new title\" \"new description\"")
                    continue

                # Extract the arguments after "update"
                args_str = parts[1]
                # Use regex to parse ID, title, and description
                update_pattern = r'^(\d+)\s+"([^"]*)"\s+"([^"]*)"$'
                update_match = re.match(update_pattern, args_str)

                if update_match:
                    task_id, new_title, new_description = update_match.groups()
                    try:
                        task_id = int(task_id)
                        success = todo_manager.update_task(task_id, new_title, new_description)
                        if success:
                            print(f"Task #{task_id} updated successfully")
                        else:
                            print(f"Failed to update task #{task_id}")
                    except ValueError as e:
                        print(f"Error: {e}")
                    except TaskNotFoundError:
                        print(f"Task with ID {task_id} not found")
                else:
                    print("Invalid update command format. Use: update id \"new title\" \"new description\"")
            elif command_input.lower().startswith("delete "):
                parts = command_input.split()
                if len(parts) != 2:
                    print("Invalid delete command format. Use: delete id")
                else:
                    try:
                        task_id = int(parts[1])
                        success = todo_manager.delete_task(task_id)
                        if success:
                            print(f"Task #{task_id} deleted successfully")
                        else:
                            print(f"Failed to delete task #{task_id}")
                    except ValueError:
                        print("Task ID must be a number")
                    except TaskNotFoundError:
                        print(f"Task with ID {parts[1]} not found")
            elif command_input.lower() == "quit":
                print("Goodbye!")
                break
            elif command_input.lower() == "help":
                display_help()
            else:
                print(f"Unknown command: {command_input.split()[0] if command_input.split() else command_input}. Type 'help' for available commands.")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()