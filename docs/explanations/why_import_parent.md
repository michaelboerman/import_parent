# Why this utility exists

This project provides a tiny, explicit helper to avoid brittle sys.path hacks sprinkled through test suites and scripts. It aims to be:

- Small and explicit.
- Idempotent: adding the same path multiple times is avoided.
- Documented so maintainers understand why sys.path is modified.