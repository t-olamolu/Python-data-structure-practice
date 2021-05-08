def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
new_str = ""
    for letter in range(len(phrase)):
        if phrase[letter].isupper() and phrase[letter] == to_swap.upper():
            new_str += phrase[letter].lower()
        elif phrase[letter].islower() and phrase[letter] == to_swap.lower():
            new_str += phrase[letter].upper()
        else:
            new_str += phrase[letter]
    return new_str