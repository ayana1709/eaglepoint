# Task 1 —› Smart Text Analyzer

---

## Step One — Every Search I Made

- https://www.gauthmath.com/solution/vOOwDrmJzIh/A-Write-a-program-in-python-that-can-calculate-the-average-word-length-
- https://stackoverflow.com/questions/52029013/python-program-for-word-count-average-word-length-word-frequency-and-frequency
- https://www.geeksforgeeks.org/python/text-analysis-in-python-3/
- https://medium.com/data-and-beyond/build-python-project-a-text-analyzer-tool-686c9647a54c

---

## Step Two — My Thought Process

When researching different methods from different websites i selected a hybrid method taking the best practices and develop combined approach to solve the problem.

### Key Points

1. case insensetive and counter
2. regex cleaning
3. handle longest words
4. error handling method and code efficiency

### Alternatives I Used From Them

- -->Manually counting characters inside a loop
- --->Using dictionary only for frequency
- --->Splitting without cleaning punctuation

---

## Step Three — Step-by-Step Solution Process

**First**, I made all the text lowercase and removed punctuation using regex. This ensures that the analysis treats words like “Hello” and “hello” the same, and ignores symbols that could interfere with counting.  
**Commit:** `feat: implement normalize_text function`

**Next**, I split the cleaned text into words, counted the total number of words, and calculated the average word length. This gives a quick overview of the text’s structure.  
**Commit:** `feat: add analyze_text function`

**After that**, I focused on the longest words and word frequency. I found all words with the maximum length, removed duplicates using set(), sorted them for clarity, and used Counter to count how often each word appears. This approach is simpler and faster than manual loops.  
**Commit:** `refactor: reorganize tests for analyze_text function and improve documentation`

**Finally**, I combined everything into a single, clean function called smart_text_analyzer. I tested it with text containing punctuation, mixed case, empty input, and multiple longest words.  
**Commit:** `feat: implement smart_text_analyzer function to analyze and process input text`

### Problem Faced

At first, using str.replace() missed some punctuation symbols, empty input caused division by zero when calculating the average word length, and duplicates appeared in the longest words list. I fixed these by switching to regex, adding a guard for empty input, and using set() + sorted() for the longest words.

---

## Step Four — Why My Solution Is Best

- Cleans text accurately using regex
- Case-insensitive and consistent processing
- Uses Counter for fast word-frequency counting
- Efficient longest-word detection with no duplicates
- Handles empty input safely (no errors)
- Lightweight and optimized — runs in O(n) time
