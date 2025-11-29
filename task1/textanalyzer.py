import re

def normalize_text(text: str) -> str:
    """Lowercase text and remove punctuation. Returns cleaned text."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    # Lowercase and strip out punctuation (keeps word characters and whitespace)
    clean = re.sub(r"[^\w\s]", "", text.lower())
    return clean.strip()
