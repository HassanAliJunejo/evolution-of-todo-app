# TodoManager API Contract

## Overview
The TodoManager class provides the core business logic for managing todo tasks in the application.

## Methods

### add_task(title: str, description: str) -> int
**Description**: Adds a new task to the collection
**Parameters**:
- title: The title of the task (non-empty string)
- description: The description of the task (string, can be empty)
**Returns**: The ID of the newly created task
**Raises**: ValueError if title is empty
**Post-condition**: A new task with status "pending" is added to the collection

### get_task(task_id: int) -> Task
**Description**: Retrieves a task by its ID
**Parameters**:
- task_id: The ID of the task to retrieve
**Returns**: The Task object
**Raises**: KeyError if task with given ID doesn't exist

### get_all_tasks() -> List[Task]
**Description**: Retrieves all tasks in the collection
**Returns**: A list of all Task objects, sorted by ID

### update_task(task_id: int, title: str = None, description: str = None) -> bool
**Description**: Updates the title and/or description of an existing task
**Parameters**:
- task_id: The ID of the task to update
- title: New title (optional, if provided must be non-empty)
- description: New description (optional)
**Returns**: True if the task was successfully updated, False otherwise
**Raises**: KeyError if task with given ID doesn't exist, ValueError if new title is empty

### mark_complete(task_id: int) -> bool
**Description**: Marks a task as complete
**Parameters**:
- task_id: The ID of the task to mark as complete
**Returns**: True if the task was successfully marked as complete, False otherwise
**Raises**: KeyError if task with given ID doesn't exist
**Post-condition**: The task's status is changed to "completed"

### delete_task(task_id: int) -> bool
**Description**: Deletes a task from the collection
**Parameters**:
- task_id: The ID of the task to delete
**Returns**: True if the task was successfully deleted, False otherwise
**Raises**: KeyError if task with given ID doesn't exist
**Post-condition**: The task is removed from the collection

## Data Types

### Task
A dataclass representing a single todo item with the following attributes:
- id: int (auto-incremented unique identifier)
- title: str (non-empty task title)
- description: str (task description, can be empty)
- status: str (either "pending" or "completed")