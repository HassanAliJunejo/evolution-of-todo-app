"""TodoManager class to handle in-memory todo logic."""
from typing import List, Optional
from .models import Task
from .exceptions import TaskNotFoundError


class TodoManager:
    """
    Manages the collection of tasks, providing methods to add, delete,
    update, view, and mark tasks as complete.
    """

    def __init__(self):
        """Initialize the TodoManager with an empty task collection."""
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, title: str, description: str = "") -> int:
        """
        Add a new task to the collection.

        Args:
            title: The title of the task (non-empty string)
            description: The description of the task (string, can be empty)

        Returns:
            The ID of the newly created task

        Raises:
            ValueError: If title is empty
        """
        if not title.strip():
            raise ValueError("Title cannot be empty")

        task_id = self._next_id
        task = Task(id=task_id, title=title.strip(), description=description.strip())
        self._tasks[task_id] = task
        self._next_id += 1

        return task_id

    def get_task(self, task_id: int) -> Task:
        """
        Retrieve a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The Task object

        Raises:
            KeyError: If task with given ID doesn't exist
        """
        if task_id not in self._tasks:
            raise TaskNotFoundError(task_id)
        return self._tasks[task_id]

    def get_all_tasks(self) -> List[Task]:
        """
        Retrieve all tasks in the collection.

        Returns:
            A list of all Task objects, sorted by ID
        """
        return sorted(self._tasks.values(), key=lambda x: x.id)

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update the title and/or description of an existing task.

        Args:
            task_id: The ID of the task to update
            title: New title (optional, if provided must be non-empty)
            description: New description (optional)

        Returns:
            True if the task was successfully updated, False otherwise

        Raises:
            KeyError: If task with given ID doesn't exist
            ValueError: If new title is empty
        """
        if task_id not in self._tasks:
            raise TaskNotFoundError(task_id)

        task = self._tasks[task_id]

        if title is not None:
            if not title.strip():
                raise ValueError("Title cannot be empty")
            task.title = title.strip()

        if description is not None:
            task.description = description.strip()

        return True

    def mark_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete.

        Args:
            task_id: The ID of the task to mark as complete

        Returns:
            True if the task was successfully marked as complete, False otherwise

        Raises:
            KeyError: If task with given ID doesn't exist
        """
        if task_id not in self._tasks:
            raise TaskNotFoundError(task_id)

        self._tasks[task_id].status = "completed"
        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task from the collection.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was successfully deleted, False otherwise

        Raises:
            KeyError: If task with given ID doesn't exist
        """
        if task_id not in self._tasks:
            raise TaskNotFoundError(task_id)

        del self._tasks[task_id]
        return True