# User Guide — ReMBC Interactive Map

This guide explains how to use and maintain the ReMBC interactive map.

## Who it's for
- **Staff** who want to see where and when ReMBC engaged with communities/schools
- **Funders & partners** who want to understand reach and equity impact
- **Students & educators** who are curious about programming in their region

## Using the HTML map (docs/rembc_map.html)
- Open in any modern browser
- Use the **top-right Layer Control** to toggle `Year — All initiatives` or specific `Year — Initiative` layers
- Click points to see **school name**, **community**, **year**, **initiative**, **students reached**, and **notes**

## Using Felt (optional)
1. Open **Felt** and create a new map.
2. Upload `data/processed/rembc_map_points.csv` (drag-and-drop).
3. Add **filters** for `year` and `initiative`.
4. Style by **initiative** (consistent colours).
5. Add a **legend** and a short **How to Use** note.
6. Share with staff or make it public for funders.

## Updating the dataset
1. Open `data/raw/rembc_partnerships_raw.csv` and add rows (one row per activity).
2. If a new **community** is added, also add it to `data/raw/communities_lookup.csv` with lat/lon.
3. Re-run: `bash scripts/run_all.sh` → this regenerates the processed CSV and HTML map.

## Quality checklist before publishing
- All new communities have **lat/lon**
- Years are valid (YYYY between 2000 and 2100)
- No duplicate rows or misspellings in community names
- Legend matches initiative colours
- EDII check: Is the context respectful and accurate? Do we need a community review?

## Support
If the HTML map doesn’t render:
- Clear browser cache, or open in incognito
- Ensure the CSV has no invalid coordinates
- Re-run the pipeline
