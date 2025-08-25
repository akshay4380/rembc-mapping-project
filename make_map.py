#!/usr/bin/env python3
"""Build an interactive HTML map using Folium for local preview and GitHub Pages.

Reads:
  data/processed/rembc_map_points.csv

Writes:
  docs/rembc_map.html
"""

import folium
from folium.plugins import MarkerCluster
import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]

COLOR_BY_INITIATIVE = {
    "High School Mentoring": "blue",
    "Rural Pre-Health Stream": "green",
    "REAP Presentation": "red",
}

def add_legend(map_obj):
    legend_html = '''
     <div style="position: fixed; 
                 bottom: 30px; left: 30px; width: 220px; z-index:9999; font-size:14px;
                 background-color: white; padding: 10px; border: 2px solid #444; border-radius: 8px;">
     <b>Initiative Legend</b><br>
     <i style="background: blue; width: 10px; height: 10px; float: left; margin-right: 8px;"></i> High School Mentoring<br>
     <i style="background: green; width: 10px; height: 10px; float: left; margin-right: 8px;"></i> Rural Pre-Health Stream<br>
     <i style="background: red; width: 10px; height: 10px; float: left; margin-right: 8px;"></i> REAP Presentation<br>
     <hr style="margin: 6px 0;">
     <div>Use the layer control (top-right) to toggle by Year and Initiative.</div>
     </div>
     '''
    map_obj.get_root().html.add_child(folium.Element(legend_html))

def main():
    inp = BASE / "data" / "processed" / "rembc_map_points.csv"
    out = BASE / "docs" / "rembc_map.html"

    df = pd.read_csv(inp)

    # Center roughly on BC
    m = folium.Map(location=[54.0, -125.0], zoom_start=4)

    # Create LayerGroups by Year and Initiative for toggling
    years = sorted(df["year"].dropna().unique().tolist())
    initiatives = sorted(df["initiative"].dropna().unique().tolist())

    # A group for each (Year, Initiative) to allow granular toggling
    layer_groups = {}
    for y in years:
        for init in initiatives:
            name = f"{y} — {init}"
            layer_groups[(y, init)] = folium.FeatureGroup(name=name, show=False).add_to(m)

    # Also add a cluster per year to keep map tidy
    clusters_by_year = {y: MarkerCluster(name=f"{y} — All initiatives", show=(y==years[-1])) for y in years}
    for y, cluster in clusters_by_year.items():
        cluster.add_to(m)

    for _, row in df.iterrows():
        y = int(row.get("year", 0))
        init = row.get("initiative", "Unknown")
        lat = row.get("lat")
        lon = row.get("lon")
        color = COLOR_BY_INITIATIVE.get(init, "gray")

        if pd.isna(lat) or pd.isna(lon):
            continue

        popup = folium.Popup(html=f"""
            <b>{row['school_name']}</b><br>
            Community: {row['community']}<br>
            Year: {y}<br>
            Initiative: {init}<br>
            Students reached: {int(row['students_reached']) if pd.notna(row['students_reached']) else 'N/A'}<br>
            Modality: {row.get('modality','N/A')}<br>
            Notes: {row.get('notes','')}
        """, max_width=300)

        marker = folium.CircleMarker(
            location=[lat, lon],
            radius=6,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.85,
            popup=popup
        )

        # Add to granular layer and to year's cluster
        marker.add_to(layer_groups[(y, init)])
        marker.add_to(clusters_by_year[y])

    # Add all clusters to map
    # (FeatureGroups already added)

    folium.LayerControl(collapsed=False).add_to(m)
    add_legend(m)

    out.parent.mkdir(parents=True, exist_ok=True)
    m.save(str(out))
    print(f"Wrote map -> {out}")

if __name__ == "__main__":
    main()
