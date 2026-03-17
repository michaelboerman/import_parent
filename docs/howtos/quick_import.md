# How to quickly make a parent package importable

If you need to import a sibling module during testing, add the parent directory to sys.path:

```python
from import_parent import add_parent_to_path
# add the directory one level up
add_parent_to_path(1)
# now python can import sibling modules