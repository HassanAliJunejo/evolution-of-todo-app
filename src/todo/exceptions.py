"""Custom exceptions for the todo application."""


class TaskNotFoundError(Exception):
    """
    Raised when a task with a specified ID is not found.

    Attributes:
        task_id: The ID of the task that was not found
    """
    def __init__(self, task_id: int):
        self.task_id = task_id
        super().__init__(f"Task with ID {task_id} not found")


class InvalidTaskError(Exception):
    """Raised when a task is invalid."""
    pass