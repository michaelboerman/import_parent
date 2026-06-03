# Why this utility exists

Python imports are resolved through `sys.path`, and that list is usually built
from the current environment and installed packages. In small local projects,
that can make sibling imports awkward when tests or scripts live in nested
folders.

`import_parent` exists to make this behavior explicit and local to one helper
call instead of spreading ad-hoc path manipulation across many files.

## Why not rely on editable installs alone?

Editable installs are excellent for normal package development, but they are not
always convenient for quick experiments, test utilities, or scripts that are
not meant to be packaged. This utility gives you a lightweight option for those
cases.

## Design goals

- Small and explicit: one small function with a clear purpose.
- Idempotent: repeated calls do not duplicate entries in `sys.path`.
- Easy to read: the code and docs explain why the path is being adjusted.

## Caveat

This helper changes process-level import behavior, so it is best used for
local development and tests rather than as the main mechanism for a published
library.