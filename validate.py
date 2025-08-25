#!/usr/bin/env python3
"""Basic data validation checks for the ReMBC mapping dataset."""
import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]

def main():
    inp = BASE / "data" / "processed" / "rembc_map_points.csv"
    df = pd.read_csv(inp)

    errors = []

    # Required fields
    required = ["community","school_name","year","initiative","lat","lon"]
    for col in required:
        if col not in df.columns:
            errors.append(f"Missing required column: {col}")

    # Check ranges
    if "year" in df.columns:
        bad_years = df[~df["year"].between(2000, 2100)]
        if not bad_years.empty:
            errors.append(f"Found {len(bad_years)} rows with invalid year range.")

    # Coordinates sanity
    if "lat" in df.columns and "lon" in df.columns:
        out_of_bounds = df[~(df["lat"].between(-90,90) & df["lon"].between(-180,180))]
        if not out_of_bounds.empty:
            errors.append(f"Found {len(out_of_bounds)} rows with invalid coordinates.")

    if errors:
        print("VALIDATION ERRORS:")
        for e in errors:
            print(" -", e)
    else:
        print("Validation passed ✔")

if __name__ == "__main__":
    main()
