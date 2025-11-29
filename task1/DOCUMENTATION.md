# Task 1 — Smart Text Analyzer

**Language:** Python  
**Author:** <Your Name>  
**Date:** YYYY-MM-DD

---

## Table of Contents

1. [Overview](#overview)
2. [Requirements & Assumptions](#requirements--assumptions)
3. [Search Log (every search & resource)](#search-log-every-search--resource)
4. [Thought Process & Design Decisions](#thought-process--design-decisions)
5. [Step-by-step Implementation Log](#step-by-step-implementation-log)
6. [Problems Faced & Fixes](#problems-faced--fixes)
7. [Testing & Examples](#testing--examples)
8. [Why this solution is best](#why-this-solution-is-best)
9. [Performance & Complexity](#performance--complexity)
10. [How to run / repo structure](#how-to-run--repo-structure)
11. [Acknowledgements / References](#acknowledgements--references)

---

## Overview

Short one-paragraph summary of what the program does and what is delivered (code files, tests, README, etc).

---

## Requirements & Assumptions

- Input: plain string
- Normalize: remove punctuation, case-insensitive
- Word delimiting: whitespace-based `split()`
- Empty input handling: return zeros and empty structures
- Output format: JSON-like dict with keys `word_count`, `average_word_length`, `longest_words`, `word_frequency`

---

## Search Log (every search & resource)

> For each search: record timestamp, exact search query you typed, site(s) visited (full URL), short note explaining why you visited and what you learned from that page.

**EXAMPLE ENTRIES (replace with your real searches):**

- [2025-11-27 14:10:05] Search query: `"python split string by whitespace multiple spaces best practice"`

  - URL visited: https://docs.python.org/3/library/stdtypes.html#str.split
  - Why I visited: Confirm `str.split()` behavior with multiple spaces and tabs.
  - What I learned / took from it:
    - `str.split()` with no args splits on any whitespace and collapses consecutive whitespace.
    - Good to use for robust word splitting.

- [2025-11-27 14:22:33] Search query: `"python remove punctuation regex"`

  - URL visited: https://docs.python.org/3/library/re.html
  - URL visited: https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
  - Why I visited: Decide between `re` and `str.translate` for removing punctuation.
  - What I learned / took from it:
    - `str.translate` with `str.maketrans` is fast; `re.sub(r'[^\\w\\s]', '', s)` is readable.
    - I chose `re` because it's explicit and easy to show in documentation.

- [2025-11-27 14:40:00] Search query: `"collections.Counter usage python word frequency"`

  - URL visited: https://docs.python.org/3/library/collections.html#collections.Counter
  - Why I visited: Confirm `Counter` methods and how to convert to a regular dict for JSON.
  - What I learned / took from it:
    - `Counter` is perfect for frequency counting and can be turned into dict with `dict()`.

- [YYYY-MM-DD HH:MM:SS] Created repo & initial commit

  - Command: git init; git add .; git commit -m "chore: init repo"
  - Note: created folder structure

- [YYYY-MM-DD HH:MM:SS] Implemented normalize_text function

  - Files modified: task1/analyzer.py
  - Code snippet:
    ```py
    import re
    def normalize_text(s):
        s = s.lower()
        s = re.sub(r'[^\\w\\s]', '', s)
        return s.strip()
    ```
  - Note: implemented and ran quick manual test with sample string

- [YYYY-MM-DD HH:MM:SS] Implemented main analyze_text function

  - Command: ran `python -m pytest tests/test_analyzer.py`
  - Result: initial tests passed/failed (describe)

- [2025-11-27 15:13:00] Problem: average_word_length wrong for empty input
  - Cause: division by zero when there are 0 words
  - Fix: added guard `if word_count == 0: average = 0.0`
  - Trade-offs: none
