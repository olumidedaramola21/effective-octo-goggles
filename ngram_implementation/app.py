dataset = [
    "the vibrant colors and intricate patterns of kente cloth , a symbol of ghanaian royalty and prestige , tell stories of culture , history , and social status . woven on narrow looms by skilled artisans , each strip of kente is a testament to patience and artistry .",
    "bogolanfini , or mud cloth , from mali , is a textile steeped in tradition and symbolism . its distinctive patterns , created using fermented mud and natural dyes , tell stories of malian culture , history , and beliefs . the process of creating bogolanfini is as rich and complex as the designs themselves .",
]


# -- Tokenization Helper --
def tokenize_text(text: str) -> list[str]:
    """Converts text to lowercase and splits puntuations (',' and '.')
    so they are treated as separate tokens.
    """
    processed_text = text.lower()
    processed_text = processed_text.replace(",", " , ")
    processed_text = processed_text.replace(".", " . ")

    return processed_text.split()


# -- Core Counting Function
def count_word(all_tokens: list[str], word: str) -> int:
    """Count the number of total occurences of a single word (A) in the token list"""
    count = 0
    for token in all_tokens:
        if token == word:
            count += 1
    return count


def count_bigram(all_tokens: list[str], word_a: str, word_b: str) -> int:
    """Counts the occurences of specic biagraam (A | B) in the token list"""
    count = 0
    for i in range(len(all_tokens) - 1):
        if all_tokens[i] == word_a and all_tokens[i + 1] == word_b:
            count += 1
    return count


# -- Probablilty Calculation and Main Logic --
def calculate_bigram_prob(all_tokens: list[str], word_a: str, word_b: str) -> float:
    """Calculate the bigram probability P(B | A) using the core formula.
    P(B | A) = Count(A, B) / Count(A)
    """

    # Numerator: Count(A, B)
    count_ab = count_bigram(all_tokens, word_a, word_b)

    # Denominator: Count(A)
    count_a = count_word(all_tokens, word_a)

    # Avoid divisions by zero
    if count_a == 0:
        return 0.0

    return count_ab / count_a


# -- Main Execution --

# 1. combine and tokenize the entire dataset into one big list
all_tokens = []
for segment in dataset:
    all_tokens.extend(tokenize_text(segment))

# 2. Calculate and print each probability
print("--- Bigram Probability Calculations ---")

# A. P("," | "cloth")
prob_1 = calculate_bigram_prob(all_tokens, word_a="cloth", word_b=",")
print(f"P(',' | 'cloth') = {prob_1}  (Count('cloth ,') = 2 / Count('cloth') = 2)")

# B. P('cloth' | ',')
prob_2 = calculate_bigram_prob(all_tokens, word_a=",", word_b="cloth")
print(f"P('cloth' | ',') = {prob_2}  (Count(', cloth') = 0 / Count(',') = 8)")

# C. P('history' | 'culture')
prob_3 = calculate_bigram_prob(all_tokens, word_a="culture", word_b="history")
print(
    f"P('history' | 'culture') = {prob_3}  (Count('culture history') = 0 / Count('culture') = 2)"
)

# D. P('history' | ',')
prob_4 = calculate_bigram_prob(all_tokens, word_a=",", word_b="history")
print(f"P('history' | ',') = {prob_4}  (Count(', history') = 2 / Count(',') = 8)")
