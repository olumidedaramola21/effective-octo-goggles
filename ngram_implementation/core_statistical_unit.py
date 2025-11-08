from collections import Counter, defaultdict
import string


# -- Helper function --
def space_tokenize(text: str) -> list[str]:
    """Simple tookenization to remove lowercase, remove punctuations, and split"""
    text = text.lower()
    # remove basic puntuations but keep spaces for splitting
    for p in string.punctuation:
        text = text.replace(p, "")
    return text.split()


def generate_ngrams(text: str, n: int) -> list[tuple[str]]:
    """Generate n-grams from a given text. (used internally by get_ngram_count )"""
    tokens = space_tokenize(text)
    ngrams = []

    if len(tokens) < n:
        return ngrams
    for i in range(len(tokens) - n + 1):
        ngrams.append(tuple(tokens[i : i + n]))
    return ngrams


# -- Target Function Implementation:
def get_ngram_counts(dataset: list[str], n: int) -> dict[str, Counter]:
    """Computes the n-gram counts from a dataset.

    This function takes a list of text strings (paragraphs or sentences) as input
    constructs ngrams from each text, and creates a dictionary where:

    * Keys represent n-1 token long contexts `contexts`.
    * Values are counter objects `counts` such that `counts[next_tokens]`
    is the count of the `next_token` following context.

    """
    ngram_counts = defaultdict(Counter)

    for paragraph in dataset:
        # Generate all n-grams for the current paragraph
        ngrams = generate_ngrams(paragraph, n)
        for ngram in ngrams:
            # 1. The context is the first n-1 tokens (a tuple of strings)
            context_tuple = ngram[:-1]

            # 2. The next word is the last token (a string)
            next_word = ngram[-1]

            # 3. Convert the context tuple to single space-separated string
            # to match the desired output key format ("Table Mountain").
            context_string = " ".join(context_tuple)
            # 4. Use the deafultdict(Counter) to easily increment the count
            ngram_counts[context_string][next_word] += 1
    return dict(ngram_counts)


example_data = [
    "This is an example sentence.",
    "Another example sentence.",
    "Split a sentence."
]

# Bigram (n=2) counts
bigram_counts = get_ngram_counts(example_data, 2)
