#!/usr/bin/env bash
set -euo pipefail

# Run full pipeline
python3 src/prepare_data.py
python3 src/validate.py
python3 src/make_map.py

echo "All done. Open docs/rembc_map.html in a browser."
