# import-parent

A small utility for importing Python modules using paths relative to the
calling script — without modifying your project structure.

Modifies `sys.path`, which is maybe kinda janky, but it works and will make life easier than having to run `pip install -e .` in every project.

Questions? Ask at https://github.com/michaelboerman/import_parent/issues

---

## Installation

```sh
pip install import-parent
```

## Usage

```python
from import_parent import add_parent_to_path
add_parent_to_path("..")
```

## Notes

- the name on PyPI is `import-parent` (with a hyphen), but when you load it in python, you need to use `import_parent` (with an underscore)
