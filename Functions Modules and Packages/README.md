# Functions, Modules and Packages

## Description
This project refactors the vehicle processing application into reusable Python modules. It separates validation, calculation, and reporting logic to improve code organization, readability, and maintainability.

## Features
- Validate vehicle records
- Count vehicles by gate
- Calculate average TAT
- Generate vehicle summary report
- Modular project structure
- Clean imports between modules
- Type hints and docstrings

## Project Structure

- main.py
- validation.py
- calculation.py
- reporting.py
- __init__.py

## Concepts Used

- Functions (`def`)
- `return`
- Modules
- Packages
- `import`
- `__name__ == "__main__"`
- Type hints
- Docstrings

## How to Run

```bash
python main.py
```

## Output

```text
========== Vehicle Summary ==========

Total Records : 5
Valid Records : 4
Invalid Records : 1

Gate Wise Count
Gate-1 : 2
Gate-2 : 2

Average TAT : 23.25 minutes
```

## Learning Outcome

- Created reusable Python functions.
- Organized code into separate modules.
- Practiced imports and package structure.
- Improved code readability and maintainability.
- Applied type hints and documentation using docstrings.