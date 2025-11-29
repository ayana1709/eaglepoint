import pytest
from analyzer import analyze_text

def test_given_example():
    inp = "The quick brown fox jumps over the lazy dog the fox"
    res = analyze_text(inp)
    assert res["word_count"] == 10
    assert res["average_word_length"] == 3.7
    assert set(res["longest_words"]) == {"quick", "brown", "jumps"}
    assert res["word_frequency"]["the"] == 2
    assert res["word_frequency"]["fox"] == 2

def test_empty_input():
    res = analyze_text("")
    assert res["word_count"] == 0
    assert res["average_word_length"] == 0.0
    assert res["longest_words"] == []
    assert res["word_frequency"] == {}

def test_punctuation_and_case():
    inp = "Hello!!! HeLLo, HELLO."
    res = analyze_text(inp)
    assert res["word_count"] == 3
    assert res["word_frequency"]["hello"] == 3

def test_ties_for_longest():
    inp = "one three seven twelve"
    res = analyze_text(inp)
    # 'twelve' (6) and 'three'(5) -> only 'twelve' is longest
    assert res["longest_words"] == ["twelve"]
