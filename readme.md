# import-parent

A small utility for importing Python modules using paths relative to the
calling script — without modifying your project structure.

Modifies `sys.path`, which is maybe kinda janky, but it works and will make life easier than having to run `pip install -e .` in every project.

Questions? Ask at 

---

## Installation

`pip install import-parent`

## Usage

`from import_parent import import_parent`
