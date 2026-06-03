# API reference

The public API is intentionally small.

## `add_parent_to_path`

```{automodule} import_parent
:members: add_parent_to_path
:show-inheritance:
```

### Accepted input forms

- `add_parent_to_path("..")` resolves a parent path using the caller's file
  location.
- `add_parent_to_path(1)` uses an integer number of levels to move upward.

The function returns the resolved directory that was added to `sys.path`.
