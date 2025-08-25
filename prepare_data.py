#!/usr/bin/env python3
"""Prepare data for the ReMBC interactive map.

Reads:
  data/raw/rembc_partnerships_raw.csv
  data/raw/communities_lookup.csv

Writes:
  data/processed/rembc_map_points.csv
"""

import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]

def normalize_text(s: str) -> str:
    return (s or "").strip()

def main():
    raw_path = BASE / "data" / "raw" / "rembc_partnerships_raw.csv"
    comm_path = BASE / "data" / "raw" / "communities_lookup.csv"
    out_path = BASE / "data" / "processed" / "rembc_map_points.csv"

    df = pd.read_csv(raw_path)
    comm = pd.read_csv(comm_path)

    # Normalize community names (basic trim); left join to add lat/lon
    df["community"] = df["community"].astype(str).map(normalize_text)
    comm["community"] = comm["community"].astype(str).map(normalize_text)

    merged = df.merge(comm, on="community", how="left", validate="m:1")

    # Basic quality checks
    missing_coords = merged[merged["lat"].isna() | merged["lon"].isna()]
    if not missing_coords.empty:
        print("WARNING: Some communities are missing coordinates:")
        print(missing_coords[["community"]].drop_duplicates().to_string(index=False))

    # Sort for readability
    merged = merged.sort_values(["year","community","school_name"]).reset_index(drop=True)

    # Reorder columns for Felt/Tableau friendliness
    cols = [
        "community","school_name","year","initiative","students_reached","modality","notes",
        "health_authority","lat","lon"
    ]
    merged = merged[cols]

    out_path.parent.mkdir(parents=True, exist_ok=True)
    merged.to_csv(out_path, index=False)
    print(f"Wrote {len(merged)} rows -> {out_path}")

if __name__ == "__main__":
    main()
