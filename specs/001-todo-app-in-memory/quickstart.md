# Quickstart Guide: In-Memory Python Console Todo App

## Prerequisites
- Python 3.13+
- UV package manager

## Setup
1. Clone the repository
2. Navigate to the project directory
3. Install dependencies using UV:
   ```bash
   uv sync
   ```
4. Run the application:
   ```bash
   uv run python src/todo/main.py
   ```

## Available Commands
- `add "title" "description"` - Add a new task
- `list` - View all tasks
- `update id "new title" "new description"` - Update a task
- `complete id` - Mark a task as complete
- `delete id` - Delete a task
- `help` - Show available commands
- `quit` - Exit the application

## Example Usage
```
> add "Buy groceries" "Milk, bread, eggs"
Added task #1: Buy groceries

> list
1. [ ] Buy groceries - Milk, bread, eggs

> complete 1
Task #1 marked as complete

> list
1. [x] Buy groceries - Milk, bread, eggs

> quit
```

## Running Tests
```bash
uv run pytest
```