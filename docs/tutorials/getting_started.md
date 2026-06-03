# Getting started

This tutorial shows the simplest way to use `import_parent` in a real project.

## 1. Install the package

If you are working from a checkout of this repository, install it in editable
mode so the package is available to your Python environment:

```bash
python3 -m pip install -e .
```

If you only want to use the published package, install it with:

```bash
python3 -m pip install import-parent
```

## 2. Add a parent directory to `sys.path`

Use the helper at the top of the script or test file that needs access to a
sibling package:

```python
from import_parent import add_parent_to_path

# example - fictional folder path of an upstream directory
add_parent_to_path("../helper_functions")
```

The call above resolves one parent directory relative to the current file and
adds that directory to `sys.path`.

## 3. Import the sibling module

After the path is added, normal imports work as expected:

```python
# example of an upstream directory
from helpers import format_message
```

This makes local development and tests easier without changing your project
layout or introducing fragile path handling in every file.