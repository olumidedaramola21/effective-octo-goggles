"""
Docstring for main

1. How to remove HTML tag using regular expression
2. How to replace common HTML entries with thier corresponding characters
3. How unicode categories work and how they can be used to filter text.

- Implement a function to strip HTML tags from raw text
- Extend the function to clean common HTML entites like &lt;, &gt; and &amp.
- Use the `unicodedata` package to explore character categories.
- Adapt a cleaning function to keep letters, number, punctuations, whitespace while removing emojis and other symbols.
"""

import re  # for defining and working with regular expressions
import unicodedata  # for working with unicode characters

# regex pattern (r<.*?>)


def clean_html_tags(text: str) -> str:
    """
    Remove every HTML tag in a string

    Applies the non-greedy pattern '.*?' so that anything enclosed
    in an angle brackets such as '<h1>', '<p>' or <img src="..." />,
    is deleted while the surrounding text is left untouched

    Args:
        text (str): Raw text that contains HTML tags

    Returns:
        str: plain text with all HTML tags.
    """
    regrex_pattern = r"<.*?>"  # match anything beteen < >
    return re.sub(regrex_pattern, "", text)


text = (
    "<h3>Let's come together to <strong>win</strong> this match."
    " <br>We can do it!</h3>"
)
cleaned_text = clean_html_tags(text)

print(f"Before cleaning: \n\ttext: {text}\n")
print(f"After cleaning: \n\ttext: {cleaned_text}\n")
