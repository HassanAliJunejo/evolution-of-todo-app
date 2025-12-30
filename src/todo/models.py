from dataclasses import dataclass
from typing import Union


@dataclass
class Task:
    """
    Represents a single todo item with id, title, description, and status.

    Attributes:
        id: Auto-incremented unique identifier
        title: Non-empty task title
        description: Task description (can be empty)
        status: Either "pending" or "completed"
    """
    id: int
    title: str
    description: str
    status: str = "pending"

    def __post_init__(self):
        """Validate the task attributes after initialization."""
        if not self.title.strip():
            raise ValueError("Title cannot be empty")
        if self.status not in ["pending", "completed"]:
            raise ValueError("Status must be either 'pending' or 'completed'")