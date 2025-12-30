"""Integration tests for the main CLI functionality."""
import io
import sys
from unittest.mock import patch, MagicMock
from src.todo.main import main


def test_add_task_via_cli():
    """Test adding a task through the CLI interface."""
    # Simulate user input for the add command
    user_inputs = [
        'add "Test Task" "Test Description"',
        'quit'
    ]

    # Mock the input function to return our test inputs
    with patch('src.todo.main.input', side_effect=user_inputs):
        # Capture the printed output
        captured_output = io.StringIO()
        with patch('sys.stdout', new=captured_output):
            main()

        output = captured_output.getvalue()

        # Verify that the task was added successfully
        assert "Added task #1: Test Task" in output


def test_list_tasks_via_cli():
    """Test viewing tasks through the CLI interface."""
    # Simulate user input to add and then list tasks
    user_inputs = [
        'add "Task 1" "Description 1"',
        'add "Task 2" "Description 2"',
        'list',
        'quit'
    ]

    # Mock the input function to return our test inputs
    with patch('src.todo.main.input', side_effect=user_inputs):
        # Capture the printed output
        captured_output = io.StringIO()
        with patch('sys.stdout', new=captured_output):
            main()

        output = captured_output.getvalue()

        # Verify that the tasks were added and then listed
        assert "Added task #1: Task 1" in output
        assert "Added task #2: Task 2" in output
        assert "1. [ ] Task 1 - Description 1" in output
        assert "2. [ ] Task 2 - Description 2" in output


def test_complete_task_via_cli():
    """Test marking a task as complete through the CLI interface."""
    # Simulate user input to add and then complete a task
    user_inputs = [
        'add "Task 1" "Description 1"',
        'complete 1',
        'list',
        'quit'
    ]

    # Mock the input function to return our test inputs
    with patch('src.todo.main.input', side_effect=user_inputs):
        # Capture the printed output
        captured_output = io.StringIO()
        with patch('sys.stdout', new=captured_output):
            main()

        output = captured_output.getvalue()

        # Verify that the task was added, marked as complete, and shown in the list
        assert "Added task #1: Task 1" in output
        assert "Task #1 marked as complete" in output
        assert "1. [x] Task 1 - Description 1" in output


def test_update_task_via_cli():
    """Test updating a task through the CLI interface."""
    # Simulate user input to add and then update a task
    user_inputs = [
        'add "Task 1" "Description 1"',
        'update 1 "Updated Task 1" "Updated Description 1"',
        'list',
        'quit'
    ]

    # Mock the input function to return our test inputs
    with patch('src.todo.main.input', side_effect=user_inputs):
        # Capture the printed output
        captured_output = io.StringIO()
        with patch('sys.stdout', new=captured_output):
            main()

        output = captured_output.getvalue()

        # Verify that the task was added, updated, and shown in the list with new details
        assert "Added task #1: Task 1" in output
        assert "Task #1 updated successfully" in output
        assert "1. [ ] Updated Task 1 - Updated Description 1" in output


def test_delete_task_via_cli():
    """Test deleting a task through the CLI interface."""
    # Simulate user input to add and then delete a task
    user_inputs = [
        'add "Task 1" "Description 1"',
        'delete 1',
        'list',
        'quit'
    ]

    # Mock the input function to return our test inputs
    with patch('src.todo.main.input', side_effect=user_inputs):
        # Capture the printed output
        captured_output = io.StringIO()
        with patch('sys.stdout', new=captured_output):
            main()

        output = captured_output.getvalue()

        # Verify that the task was added, deleted, and no longer appears in the list
        assert "Added task #1: Task 1" in output
        assert "Task #1 deleted successfully" in output
        assert "No tasks found." in output  # Since we deleted the only task