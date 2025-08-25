# Contributing

Thank you for considering a contribution!

## How to update data
1. Edit `data/raw/rembc_partnerships_raw.csv`.
2. If adding a *new community*, add it to `data/raw/communities_lookup.csv` with `lat`/`lon`.
3. Run `bash scripts/run_all.sh` to regenerate processed data and the HTML map.

## Development
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
bash scripts/run_all.sh
```

## Validation
`python src/validate.py` must pass with **no errors** before opening a PR.
