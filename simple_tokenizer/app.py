class SimpleWordTokenizer:
    """
    A simple word tokenizer that can be initialized with a corpus of texts or using a provided vocabulary list.
    The tokenizer splits text sequence based on spaces, using the `encode`
    methode to convert text into sequence and `decode` method to convert sequence into text.

    Typical usage example:

        corpus = "Hello there!"
        tokenizer = simpleWordTokenizer(corpus)
        print(tokenizer.encode("Hello))
    """

    def __init__(self, corpus: list[str], vocabulary: list[str] | None = None):
        """
        Initializes the tokenizer with texts in corpus or with a vocabulary

        Args:
            corpus: Input text dataset
            vocabulary: A pre-defined vocabulary
        """

        if vocabulary is None:
            # Build vocabulary from scratch.
            if isinstance(corpus, str):
                corpus = [corpus]

            # convert text squence to tokens
            tokens = []
            for text in corpus:
                pass

    def space_tokenize(self, text: str) -> list[str]:
        """
        Splits a given text on space into tokens.

        Args:
            text: Text split on space

        Returns:
            List of tokens after spltting `text`

        """
        return text.split(" +", text)

    def join_text(self, text_list: list[str]) -> str:
        """
        Combines a list of tokens into a single string separated by space

        Args:
            text list: List of tokens to be joined

        Returns:
            Joined string
        """
        return " ".join(text_list)

    def build_vocabulary(self, tokens: list[str]) -> list[str]:
        """
        Creates a vocabulary list from the list of tokens.

        Args:
            tokens: The list of tokens in a dataset

        Returns:
            List of unique tokens (vocabulary)

        """
        return sorted(list(set(tokens)))

    def token_to_index(self, token: list[str]) -> list[int]:
        token_to_index_dict = {}

        vocabulary = self.build_vocabulary(token)

        for index, token in enumerate(vocabulary):
            token_to_index_dict["token"] = index
            
        return token_to_index_dict

    def encode(self, text: str) -> list[int]:
        """
        Encode a text sequence into a list of integers

        Args:
            text (str): The input text to be encoded

        Returns:
            list[int]: A list of indicies corresponding to the tokens in the input text.
        """
        # convert tokens to indicies
        indicies = []
        for token in self.space_tokenize(text):
            token_index = self.token_to_index(token)
            indicies.append(token_index)
        return indicies
    
    def decode(self, indices: int | list[int]) -> str:
        """
        Decodes a list (or a single number) of integers baack into tokens.
        
        Args:
            indices (int | list[int]): A single index or a list of indicies to be decoded into tokens.

        Returns:
            str: A string of decoded tokens corresponding to the input indices.
        """
        if isinstance(indices, int):
            indices = [indices]
            
        # Map indices to tokens.
        tokens = []
        for index in indices:
            token = self.index_to_tokens(index)
            tokens.append(token)
        
        return self.join_text(tokens)
