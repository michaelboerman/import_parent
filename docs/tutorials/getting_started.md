# Getting started — Add import_parent to your project path

This tutorial shows how to use add_parent_to_path in a project.

Steps:
1. Install the package in editable mode during development:
   ```bash
   python3 -m pip install -e .
   ```

2. Add the following code to your project:
   ```python
   from import_parent import add_parent_to_path
   add_parent_to_path(1)  # adds the parent directory to sys.path
   ```