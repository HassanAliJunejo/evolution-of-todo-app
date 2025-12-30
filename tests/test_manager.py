"""Unit tests for the TodoManager class."""
import pytest
from src.todo.manager import TodoManager
from src.todo.exceptions import TaskNotFoundError


class TestTodoManager:
    """Test cases for the TodoManager class."""

    def setup_method(self):
        """Set up a fresh TodoManager instance for each test."""
        self.manager = TodoManager()

    def test_add_task_success(self):
        """Test that adding a task works correctly."""
        title = "Test Task"
        description = "Test Description"

        task_id = self.manager.add_task(title, description)

        # Verify the task was added with correct details
        assert task_id == 1
        assert len(self.manager._tasks) == 1

        task = self.manager._tasks[task_id]
        assert task.id == task_id
        assert task.title == title
        assert task.description == description
        assert task.status == "pending"

    def test_add_task_without_description(self):
        """Test that adding a task without description works."""
        title = "Test Task"

        task_id = self.manager.add_task(title)

        # Verify the task was added with correct details
        assert task_id == 1
        task = self.manager._tasks[task_id]
        assert task.title == title
        assert task.description == ""

    def test_add_task_empty_title_error(self):
        """Test that adding a task with empty title raises ValueError."""
        with pytest.raises(ValueError, match="Title cannot be empty"):
            self.manager.add_task("")

        with pytest.raises(ValueError, match="Title cannot be empty"):
            self.manager.add_task("   ")

    def test_add_task_assigns_unique_ids(self):
        """Test that each task gets a unique ID."""
        task_id_1 = self.manager.add_task("Task 1", "Description 1")
        task_id_2 = self.manager.add_task("Task 2", "Description 2")

        assert task_id_1 == 1
        assert task_id_2 == 2
        assert task_id_1 != task_id_2

    def test_get_all_tasks_empty(self):
        """Test that get_all_tasks returns an empty list when no tasks exist."""
        tasks = self.manager.get_all_tasks()

        assert tasks == []
        assert len(tasks) == 0

    def test_get_all_tasks_with_tasks(self):
        """Test that get_all_tasks returns all tasks in the correct order."""
        # Add tasks
        task_id_1 = self.manager.add_task("Task 1", "Description 1")
        task_id_2 = self.manager.add_task("Task 2", "Description 2")
        task_id_3 = self.manager.add_task("Task 3", "Description 3")

        # Get all tasks
        tasks = self.manager.get_all_tasks()

        # Verify all tasks are returned in order
        assert len(tasks) == 3
        assert tasks[0].id == task_id_1
        assert tasks[1].id == task_id_2
        assert tasks[2].id == task_id_3

        # Verify task details
        assert tasks[0].title == "Task 1"
        assert tasks[1].title == "Task 2"
        assert tasks[2].title == "Task 3"

    def test_mark_complete_success(self):
        """Test that marking a task as complete works correctly."""
        # Add a task
        task_id = self.manager.add_task("Test Task", "Test Description")

        # Verify initial status
        task = self.manager.get_task(task_id)
        assert task.status == "pending"

        # Mark as complete
        result = self.manager.mark_complete(task_id)

        # Verify the result and status change
        assert result is True
        task = self.manager.get_task(task_id)
        assert task.status == "completed"

    def test_mark_complete_nonexistent_task(self):
        """Test that marking a non-existent task raises TaskNotFoundError."""
        with pytest.raises(TaskNotFoundError):
            self.manager.mark_complete(999)

    def test_update_task_success(self):
        """Test that updating a task works correctly."""
        # Add a task
        task_id = self.manager.add_task("Original Title", "Original Description")

        # Verify initial values
        task = self.manager.get_task(task_id)
        assert task.title == "Original Title"
        assert task.description == "Original Description"

        # Update the task
        new_title = "Updated Title"
        new_description = "Updated Description"
        result = self.manager.update_task(task_id, new_title, new_description)

        # Verify the result and updated values
        assert result is True
        task = self.manager.get_task(task_id)
        assert task.title == new_title
        assert task.description == new_description

    def test_update_task_partial(self):
        """Test that updating only title or description works correctly."""
        # Add a task
        task_id = self.manager.add_task("Original Title", "Original Description")

        # Update only the title
        new_title = "Updated Title"
        result = self.manager.update_task(task_id, title=new_title)

        # Verify the result and updated values
        assert result is True
        task = self.manager.get_task(task_id)
        assert task.title == new_title
        assert task.description == "Original Description"  # Should remain unchanged

        # Update only the description
        new_description = "Updated Description"
        result = self.manager.update_task(task_id, description=new_description)

        # Verify the result and updated values
        assert result is True
        task = self.manager.get_task(task_id)
        assert task.title == new_title  # Should remain unchanged
        assert task.description == new_description

    def test_update_task_nonexistent(self):
        """Test that updating a non-existent task raises TaskNotFoundError."""
        with pytest.raises(TaskNotFoundError):
            self.manager.update_task(999, "New Title", "New Description")

    def test_update_task_empty_title_error(self):
        """Test that updating a task with empty title raises ValueError."""
        # Add a task
        task_id = self.manager.add_task("Original Title", "Original Description")

        # Try to update with empty title
        with pytest.raises(ValueError, match="Title cannot be empty"):
            self.manager.update_task(task_id, title="")

    def test_delete_task_success(self):
        """Test that deleting a task works correctly."""
        # Add a task
        task_id = self.manager.add_task("Test Task", "Test Description")

        # Verify the task exists
        task = self.manager.get_task(task_id)
        assert task.title == "Test Task"

        # Delete the task
        result = self.manager.delete_task(task_id)

        # Verify the result and that the task no longer exists
        assert result is True
        assert len(self.manager._tasks) == 0
        with pytest.raises(TaskNotFoundError):
            self.manager.get_task(task_id)

    def test_delete_task_nonexistent(self):
        """Test that deleting a non-existent task raises TaskNotFoundError."""
        with pytest.raises(TaskNotFoundError):
            self.manager.delete_task(999)

    def test_delete_task_then_add_new(self):
        """Test that after deleting a task, a new task gets the next available ID."""
        # Add a task
        task_id_1 = self.manager.add_task("Task 1", "Description 1")

        # Delete the task
        result = self.manager.delete_task(task_id_1)
        assert result is True

        # Add a new task - it should get the next ID
        task_id_2 = self.manager.add_task("Task 2", "Description 2")
        assert task_id_2 == 2  # Next available ID after deletion