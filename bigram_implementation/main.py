"""
N-gram  Model: Counting and Probabilities

Building a simple biagram (2-gram) model
"""

import collections

# 1. Training dataset
corpus = [
    "hello world",
    "hello there",
    "hello world today",
]

# 2. Tookenize and create biagrams (pairs of words)
biagrams = []
for text in corpus:
    # Add special <s> (start) and </s> (end) tokens
    tokens = ["<s>"] + text.split() + ["</s>"]
    # create pairs: (<s>, hello), (hello, words), (word, </s>), etc
    for i in range(len(tokens) - 1):
        biagrams.append((tokens[i], tokens[i + 1]))


print(f"All Biagrams: {biagrams}\n")

# 3. Count the co-occurrences
# How many times does each pair appear
biagram_count = collections.Counter(biagrams)
print("Biagram count: ", biagram_count, "\n")

# How many times does each context appear?
context_count = collections.Counter(pair[0] for pair in biagrams)
print("Context count", context_count)


# 4. Build the probablity table
# P(next_word | prev_word) = count(prev_word, next_word)  / count(prev_word)

probablities = {}
for word1, word2 in biagram_count:
    context_word = word1
    if context_word not in probablities:
        probablities[context_word] = {}

    # The core logic
    prob = biagram_count[(word1, word2)] / context_count[word1]
    probablities[context_word][word2] = prob

print("--- Probability Table ---")
import json

print(json.dumps(probablities, indent=2))


# 5. Make a prediction: What comes after "hello"?
print(f"\nPrediction after 'hello': {probablities['hello']}")
