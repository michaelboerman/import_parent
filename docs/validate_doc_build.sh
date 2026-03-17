#!/usr/bin/env bash
set -euo pipefail

# run from project root on macOS
python3 -m venv .docs-venv
source .docs-venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -e .
python3 -m pip install -r docs/requirements.txt
# build HTML into docs/_build/html
sphinx-build -b html docs docs/_build/html
echo "Local docs built at docs/_build/html"