# The Evolution of Todo - Phase I

A professional, spec-driven Todo application built with Python 3.13 and modern development workflows. This project demonstrates the transition from a simple in-memory CLI app to a robust system.

## 🚀 Features (Phase I)
- **Add Tasks**: Create tasks with titles and descriptions.
- **View Tasks**: Display all tasks with unique IDs and status indicators.
- **Update Tasks**: Modify existing task details.
- **Mark Complete**: Toggle task completion status.
- **Delete Tasks**: Remove tasks by their ID.
- **Robust Error Handling**: Prevents crashes from invalid IDs or empty inputs.

## 🛠 Tech Stack
- **Language**: Python 3.13+
- **Package Manager**: [UV](https://github.com/astral-sh/uv) (Extremely fast Python package installer)
- **Methodology**: Spec-driven development using **Spec-Kit Plus** and **Constitution-based coding**.
- **Testing**: Pytest for Unit and Integration testing.

## 📁 Project Structure
```text
src/
└── todo/
    ├── main.py       # CLI Interface & User Loop
    ├── manager.py    # Business Logic (TodoManager)
    ├── models.py     # Data Structures (Task Dataclass)
    └── exceptions.py # Custom Error Definitions
specs/                # Spec-Kit Plus history and documentation
tests/                # Automated test suite
