def search4vowels(phrase: str) -> set:
    """Display any vowels found in an asked-for phrase."""
    vowels = set('aeiou')
    return(vowels.intersection(set(phrase)))

def search4letters(phrase: str, letters: str='aeiou') -> set:
    """Return a set of 'letters' found in a given 'phrase'"""
    return set(letters).intersection(set(phrase))
