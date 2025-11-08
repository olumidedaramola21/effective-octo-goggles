class SimpleCharTokenizer:
    """
    A minimal character-level tokenizer that does exactly:
    "cat" -> ["c", "a", "t"] -> [3, 2, 5] (example IDs)

    This simple version assumes that any text it needs to encode or decode
    will ONLY use characters it has seen in `build_vocab`
    """

    def __init__(self):
        # The dictionary mapping: char -> int
        self.char_to_id = {}
        # The dictionary mapping: int -> char
        self.id_to_char = {}
        self.vocab_size = 0

    def build_vocab(self, text: str):
        """
        Builds the vocabulary from a string of text

        Args:
            text (str): string of text
        """
        # 1. Get all the unique characters from the text
        unique_chars = sorted(list(set(text)))

        print(f"Found {len(unique_chars)} unique characters.")

        # 2. Reset the mappings
        self.char_to_id = {}
        self.id_to_char = {}

        # 3. Create the mappings
        for i, char in enumerate(unique_chars):
            self.id_to_char[i] = char
            self.char_to_id[char] = i

        # 4. store the vocab style
        self.vocab_size = len(unique_chars)

    def encode(self, text):
        """
        Converts a string of characters into a list of integers.

        - Crashes if the character is not in vocab
        Args:
            text (_type_): _description_
        """
        return [self.char_to_id[char] for char in text]

    def decode(self, ids: list[int]) -> str:
        """
        Converts a list of integers back into a string.

        Args:
            text (_type_): _description_
        """
        return "".join([self.id_to_char[id] for id in ids])


if __name__ == "__main__":

    # 1. Define the training text
    text = "The cat sat on the mat"

    # 2. Create and train the tokenizer
    tokenizer = SimpleCharTokenizer()
    tokenizer.build_vocab(text)

    # 3. see the vocabulary
    print("-- Vocabulary --")
    print(f"Vocab Size: {tokenizer.vocab_size}")
    print(tokenizer.char_to_id)

    # 4. Test encoding
    print("\n--- Encoding ---")
    text_to_encode = "cat"
    encoded = tokenizer.encode(text_to_encode)
    print(f"'{text_to_encode}' -> {encoded}")

    # 6. Show the failure case
    print("\n--- Failure Test ---")
    try:
        tokenizer.encode("dog")
    except KeyError as e:
        print("Tried to encode 'dog', but failed!")
        print(f"Error: {e} not in vocabulary")
