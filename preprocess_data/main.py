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
    - Remove every HTML tag in a string

    Applies the non-greedy pattern '.*?' so that anything enclosed
    in an angle brackets such as '<h1>', '<p>' or <img src="..." />,
    is deleted while the surrounding text is left untouched

    - Replace HTML entities like &nbsp;, &amp;, &lt;, and &gt with other characters.

    Args:
        text (str): Raw text that contains HTML tags

    Returns:
        str: Cleaned text without HMTL tags and entities.
    """
    regrex_pattern = r"<.*?>"  # match anything beteen < >

    # 1. remove HTML tags
    text = re.sub(regrex_pattern, "", text)

    # 2. Replace common HTML entities
    html_entities = {
        "&nbsp;": " ",
        "&amp;": "&",
        "&lt;": "<",
        "&gt;": ">",
    }

    for entity, replacement in html_entities.items():
        text = text.replace(entity, replacement)

    return text


text = (
    "<h3>Let's come&nbsp;together &amp; <strong>win</strong> this match."
    " &lt;br&gt;We can do it!</h3>"
)
cleaned_text = clean_html_tags(text)

print(f"Before cleaning: \n\ttext: {text}\n")
print(f"After cleaning: \n\ttext: {cleaned_text}\n")

print(hex(ord("🤣")))
# print("Symbol 🤣's Unicode category is:", unicodedata.category("🤣"))
# print("Symbol 😭's Unicode category is:", unicodedata.category("😭"))


# print("Symbol 😊's Unicode category is:", unicodedata.category("😊"))
# print("Symbol 😱's Unicode category is:", unicodedata.category("😱"))


def clean_unicode(text: str) -> str:
    categories_to_keep = {"L", "N", "P"}  # keep letters, numbers and puntuations
    keep = []

    for ch in text:
        do_keep = ch.isspace()  # always keep spaces

        if not do_keep:
            for category in categories_to_keep:
                if unicodedata.category(ch).startswith(category):
                    do_keep = True
                    break

        if do_keep:
            keep.append(ch)

    return "".join(keep)
