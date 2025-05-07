from collections.abc import Sequence
from typing import Iterable, TypeVar

T = TypeVar('T')

def seqsearch(val: T, seq: Iterable[T]) -> int:
    """Search for an item VAL in a sequence SEQ.  Return the index of VAL in
       SEQ.  Raise a ValueError if VAL is not in SEQ."""
    idx: int = 0
    found: bool = False
    for item in seq:
        if item == val:
            found = True
            break
        else:
            idx += 1
    if not found:
        raise ValueError('{0} not found in sequence'.format(val))
    return idx

def binsearch(val: T, seq: Sequence[T]) -> int:
    """Search for an item VAL in a sequence SEQ, using a binary search.  Return
       the index of VAL in SEQ.  Raise a ValueError if VAL is not in SEQ."""
    # Pre
    assert hasattr(val, '__lt__') and hasattr(val, '__gt__')
    idx: int = len(seq) // 2
    if len(seq) < 1:
        raise ValueError('{0} not found in sequence'.format(val))
    elif val != seq[idx]:
        if val < seq[idx]: # Go left
            idx = binsearch(val, seq[:idx])
        elif val > seq[idx]: # Go right
            idx = (idx+1) + binsearch(val, seq[idx+1:])
    return idx

# Standard sequence operators (adapter so I can plug in any desired search algorithm)
def search(val: T, seq: Sequence[T]) -> int:
    return binsearch(val, seq)

def contains(val: T, seq: Sequence[T]) -> bool:
    """Returns a boolean indicating whether VAL is contained in SEQ.
       Does not raise an error if VAL is absent."""
    found = True
    try:
        search(val, seq)
    except ValueError:
        found = False
    return found

def index(val: T, seq: Sequence[T]) -> int:
    return search(val, seq)