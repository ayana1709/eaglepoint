import re
from collections import Counter
def smart_text_analyzer(text):
    #this convert  to lowercase and remove punctuation
    clean_text = re.sub(r"[^\w\s]", "", text.lower())
    words = clean_text.split()
    total_words = len(words)
    if total_words == 0:
        return {
            "total_words": 0,
            "average_word_length": 0,
            "longest_words": [],
            "word_frequency": {}
        }
 # calculate  the longest and  the average word 
    total_length = sum(len(word) for word in words)
    average_length = round(total_length / total_words, 2)
    max_length = max(len(word) for word in words)
    longest_words = sorted(list({word for word in words if len(word) == max_length}))
    #  Counte the frequency of each word 
    word_frequency = dict(Counter(words))
    return {
        "total_words": total_words,
        "average_word_length": average_length,
        "longest_words": longest_words,
        "word_frequency": word_frequency
    }
text_input = "The quick brown fox jumps over the lazy dog the fox"
result = smart_text_analyzer(text_input)
print(result)
