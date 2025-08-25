def slugify(s: str) -> str:
    return (s or "").strip().lower().replace(" ", "-")
