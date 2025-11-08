import string


def space_tokenize(text: str) -> list[str]:
    """Simple tokenization:  convert to lowercase and split by whitespace"""
    return text.lower().split()


def generate_ngrams(text: str, n: int) -> list[tuple[str]]:
    """
    Generate n-grams from a given text.

    Args:
        text: The input text string
        n: The size of the n-grams (e.g., 2 for bigrams, 3 for for trigrams.)

    Returns:
        A list of n-grams, each represented by a tuple of tokens.
    """

    # 1. tokenize the text
    tokens = space_tokenize(text)

    # 2. Construct the list 0f n_grams.
    ngrams = []

    for i in range(len(tokens) - n + 1):
        # slice the tokens list from the current index "i" up to "i + n"
        # to get the sequence of "n" tokens.
        ngram_list = tokens[i : i + n]

        # convert the list of strings to tuple of strings (the required format)
        ngrams.append(tuple(ngram_list))
    return ngrams


# demo dataset
dataset = [
    "Table mountain is tall.",
    "Jide is hunger and wants food.",
    "The power of language models",
]

all_unigrams = []
all_bigrams = []
all_trigrams = []
