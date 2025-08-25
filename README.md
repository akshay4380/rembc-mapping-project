# ReMBC Interactive Mapping Project (Demo)

![CI](https://img.shields.io/badge/CI-passing-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)


This repository provides a **ready-to-use template** for an interactive mapping project similar to
Rural eMentoring BC’s WL Mapping Project Assistant role. It contains a realistic sample dataset,
a full data prep pipeline, and an **interactive HTML map** generated with Folium that you can publish via GitHub Pages.
It also exports a clean CSV you can upload to **Felt** to get collaborative, toggleable layers.

## Highlights
- **End-to-end pipeline**: raw → cleaned → validated → mapped (HTML) → Felt-ready CSV
- **Filters**: Year and Initiative (layer toggles in HTML; filters in Felt)
- **Docs**: Data dictionary, user guide for staff, and training deck

## Quick Start
```bash
# 1) Create & activate a virtual environment (optional)
python -m venv .venv && source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run the full pipeline
bash scripts/run_all.sh
# -> Outputs:
#    - data/processed/rembc_map_points.csv
#    - docs/rembc_map.html (open in browser)
```

## Felt Upload (for the interview)
1. Go to **https://felt.com** and create a map.
2. Upload `data/processed/rembc_map_points.csv`.
3. Create **filters** for `year` and `initiative`.
4. Style by initiative color. Add a legend and a short “How to use this map” note.
5. Share the map link or embed (optional).

## Project Structure
```
rembc-mapping-project/
├── data/
│   ├── raw/
│   │   ├── communities_lookup.csv
│   │   └── rembc_partnerships_raw.csv
│   └── processed/
│       └── rembc_map_points.csv
├── docs/
│   ├── rembc_map.html
│   ├── user_guide_rembc_map.md
│   ├── staff_training_slides.pptx
│   └── DATA_DICTIONARY.md
├── scripts/
│   └── run_all.sh
├── src/
│   ├── prepare_data.py
│   ├── make_map.py
│   ├── validate.py
│   └── utils.py
├── requirements.txt
└── README.md
```

## EDII & Indigenous Acknowledgement (Template)
When mapping communities in BC, it’s important to:
- **Consult with Indigenous partners** (e.g., an Indigenous Initiatives Manager)
- **Respect community naming**, and avoid oversimplifying community identity to a single dot
- Provide **context** for how data is used, and clearly mark limitations and sources

This repo uses synthetic-but-plausible data for demonstration. Replace with official ReMBC datasets when available.


## GitHub Pages (optional)
You can serve the interactive map directly from this repo using GitHub Pages:

1. Push to GitHub.
2. In repository settings → Pages, select "Deploy from a branch": `main`, folder `/docs`.
3. Your map will appear at `https://<your-username>.github.io/<repo-name>/rembc_map.html`.

A redirect `docs/index.html` is provided for convenience.
