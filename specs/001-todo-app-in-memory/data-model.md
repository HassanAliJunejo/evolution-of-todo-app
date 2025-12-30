# Data Model: In-Memory Python Console Todo App

## Task Entity

### Fields
- **id**: int (auto-incremented, unique identifier)
- **title**: str (task title, non-empty)
- **description**: str (task description, can be empty)
- **status**: str (either "pending" or "completed", default "pending")

### Relationships
- The Task entity is managed by the TodoManager class
- Each Task has a unique ID within the TodoManager's collection

### Validation Rules
- ID must be a positive integer
- Title must not be empty or None
- Status must be either "pending" or "completed"
- Description can be empty but not None

### State Transitions
- A Task starts with status "pending"
- A Task can transition from "pending" to "completed" when marked as complete
- A Task cannot transition back from "completed" to "pending" in this implementation

## TodoManager Entity

### Fields
- **tasks**: dict[int, Task] (collection of tasks indexed by ID)
- **next_id**: int (counter for auto-incrementing task IDs)

### Relationships
- Contains multiple Task entities
- Responsible for all CRUD operations on Task entities

### Validation Rules
- No two tasks can have the same ID
- The next_id counter must always be greater than any existing task ID