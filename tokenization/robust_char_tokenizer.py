class RobustCharTokenizer:
    """
    A more robust character-level tokenizer.

    It includes a special "<unk>" token to handle
    characters that were not in the training text.
    """

    def __init__(self) -> None:
        # Define our special tokens
        self.pad_token = "<pad>"  # We add padding for later
        self.unk_token = "<unk>"  # for "unknown" chars

        # Mappings will built later
        self.char_to_id = {}
        self.id_to_char = {}

        # Get the IDs for special tokens
        self.pad_id = 0
        self.unk_id = 1

        self.vocab_size = 0

    def build_vocab(self, text):
        """
        Builds the vocabulary from a string of text

        Args:
            text (_type_): _description_
        """

        # 1. Get all the unique characters
        unique_chars = sorted(list(set(text)))

        # 2. Reset mappings and add special tokens first
        self.char_to_id = {self.pad_token: self.pad_id, self.unk_token: self.pad_id}
        self.id_to_char = {self.pad_id: self.pad_token, self.unk_id: self.unk_token}

        # start indexing from 2 (since 0 and 1 are taken)
        idx = 2
        for char in unique_chars:
            # Add the char if it's not a special token
            if char not in self.char_to_id:
                self.char_to_id[char] = idx
                self.id_to_char[idx] = char
                idx += 1

        self.vocab_size = len(self.char_to_id)
        print(f"Vocabulary build. Size: {self.vocab_size}")

    def encode(self, text: str) -> list[int]:
        """
        Converts a string of characters into a list of integers

        Args:
            text (str): _description_

        Returns:
            list[int]: _description_
        """
        return [self.char_to_id.get(ch, self.unk_id) for ch in text]

    def decode(self, idx: list[int]) -> str:
        """
        Convert a list of integers into string of characters

        Args:
            idx (list[int]): _description_

        Returns:
            str: _description_
        """

        return "".join([self.id_to_char.get(id, self.unk_token) for id in idx])


if __name__ == "__main__":

    # 1. Define our training text
    text = "The cat sat on the mat"

    # 2. Create and train the tokenizer
    tokenizer = RobustCharTokenizer()
    tokenizer.build_vocab(text)

    # 3. See the vocabulary (note <pad> and <unk>)
    print("\n-- Vocabulary --")
    print(tokenizer.char_to_id)

    # 4. Test encoding
    print("\n-- Encoding --")
    text_to_encode = "cat"
    encoded = tokenizer.encode(text_to_encode)
    print(f"{text_to_encode} -> {encoded}")

    # 5. Test Decoding
    print("\n--- Decoding ---")
    decoded = tokenizer.decode(encoded)
    print(f"{encoded} -> {decoded}")

    # 6. Show the robust test
    print("\n--- Robustness Test ---")
    unknown_text = "A dog?!"
    print(f"Original text: '{unknown_text}'")

    encoded_unknown = tokenizer.encode(unknown_text)
    print(f"Encoded: {encoded_unknown}")

    decoded_unknown = tokenizer.decode(encoded_unknown)
    print(f"Decoded: '{decoded_unknown}'")

    # Let's see which token is the <unk> id
    print(f"(Note: <unk> id is {tokenizer.unk_id})")
