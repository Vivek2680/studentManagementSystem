# studentManagementSystem

A simple command-line application to manage student records and their marks, built with Python.

## Features

- Add one or more students with their marks
- View all student records
- Search for a specific student
- Update a student's marks
- Delete a student record

## Requirements

- Python 3.x
- No external libraries required

## Usage

Run the script directly:

```bash
python students.py
```

You'll be presented with a menu:

```
1. Add Student
2. Show Student
3. Search Student
4. Update Student
5. Delete Student
6. Exit
```

### Menu Options

| Option | Description |
|--------|-------------|
| 1 | Add one or more students. Enter a blank name to stop adding. |
| 2 | Display all students and their marks. |
| 3 | Search for a student by name and view their marks. |
| 4 | Overwrite a student's marks with a new value. |
| 5 | Remove a student record entirely. |
| 6 | Exit the program. |

## Data Format

Students are stored in memory as a dictionary:

```python
{
  "Alice": [85, 90],
  "Bob": [72]
}
```

A student can have multiple marks if added more than once via the **Add Student** option.

## Input Validation

- Marks must be integers between **0 and 100** (inclusive).
- Non-numeric mark input is caught and prompts re-entry.
- Out-of-range marks are rejected with an error message.

## Notes

- Data is stored **in memory only** , all records are lost when the program exits.
- The **Update** option replaces all existing marks for a student with a single new value.
- Student names are **case-sensitive** (`"alice"` and `"Alice"` are treated as different students).
