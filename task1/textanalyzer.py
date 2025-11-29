from collections import Counter
from typing import Dict, Any

def analyze_text(text: str) -> Dict[str, Any]:
    """
    Analyze text and return:
      - word_count
      - average_word_length (2 decimals)
      - longest_words (list)
      - word_frequency (dict)
    """
    clean = normalize_text(text)
    words = clean.split()
    word_count = len(words)

    if word_count == 0:
        return {
            "word_count": 0,
            "average_word_length": 0.0,
            "longest_words": [],
            "word_frequency": {}
        }

    total_chars = sum(len(w) for w in words)
    avg_len = round(total_chars / word_count, 2)

    max_len = max(len(w) for w in words)
    # use a set to avoid duplicates, then sort for consistent output
    longest_words = sorted({w for w in words if len(w) == max_len})

    freq = dict(Counter(words))

    return {
        "word_count": word_count,
        "average_word_length": avg_len,
        "longest_words": longest_words,
        "word_frequency": freq
    }
