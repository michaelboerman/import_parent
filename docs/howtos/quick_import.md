# How to import a sibling package during tests

Use this recipe when a test file or script lives in a subdirectory and needs to
import code from a parent folder.

```python
from import_parent import add_parent_to_path

# Add the directory one level up.
add_parent_to_path(1)

# The parent package is now importable from this process.
import app
```

## When to choose the integer form

If you prefer counting directory levels instead of writing a path string, this
works too:

```python
add_parent_to_path(2)
```

This is useful when the relative path is not obvious from the current file's
location or when you want a compact, numeric expression.

## Notes

- The helper is idempotent, so adding the same path repeatedly will not create
  duplicate entries in `sys.path`.
- Use this only for small local tools or tests; for production packages, normal
  installation and package imports are still the preferred approach.