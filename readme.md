# import-parent

https://import-parent.readthedocs.io/

`import_parent` is a tiny helper for Python projects that need to import code
from a parent directory.

It adds a parent folder to `sys.path` relative to the caller, which is useful
for local tooling, test helpers, and small scripts that are not installed as
packages.

It works when used in .py files or .ipynb files, which typically have different default behaviour about local imports otherwise.

## Why this package exists

If your project layout is:

```text
project/
├── helper/
├── tests/
└── scripts/
```

and a file in `scripts/` (or any of its subfolders) needs to import a function from `helpers/` (or any of its subfolders), this package makes that import possible.

The relative import *may* be possible on some computers by running `from ..helper.file import function`, but that `..` notation is *not* possible in cloud-based IDEs like Posit Workbench, Posit Cloud, JupyterHub, GitHub Codespaces, etc., especailly when they are accessed from an enterprise account.

Using `add_parent_to_path` avoids the need for the following janky modification of `sys.path` otherwise needed to add a parent directory:
```python
import os
import sys
up_one_level = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if up_one_level not in sys.path:
    sys.path.append(up_one_level)
```

Heaven forbid you need to go up *two* levels, in which case that janky code gets even jankier.

## Installation

```sh
pip install import-parent
```

## Quick start

```python
from import_parent import add_parent_to_path

add_parent_to_path("..")
```

This resolves the parent directory of the current caller and prepends it to
`sys.path`, so sibling modules can be imported immediately.

## When to use it

Use this package when:

- you are working on local scripts or tests that should import a sibling package;
- you want a small, explicit alternative to repeated `sys.path` manipulation;
- you prefer not to install the project in editable mode for every experiment.

## Documentation

- Read the Docs: https://import-parent.readthedocs.io/
- Tutorials: see the getting-started guide in the docs.
- How-to recipes: use the task-focused examples in the docs.
- Explanation: learn why this helper exists and when it is appropriate.
- Reference: API details for `add_parent_to_path`.

## Notes

- The package name on PyPI is `import-parent` (with a hyphen).
- The Python import name is `import_parent` (with an underscore).

Questions and feedback: https://github.com/michaelboerman/import_parent/issues
