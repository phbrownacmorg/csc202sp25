from Stack import Stack

def match_delims(instring: str) -> bool:
    """Match the delimiters (), {}, and [].  Return True iff the delimiters are balanced."""
    matched = True
    st: Stack[str] = Stack[str]()
    openers: str = "([{"
    closers: str = ")]}"
    """Return True iff INSTRING has matching delimiters ( ()[]{} )."""
    for c in instring:
        if c in openers:                       # For an opening delimiter,
            st.push(closers[openers.index(c)]) # push the matching closer
        elif c in closers:
            matched = matched and (not st.isEmpty()) and (c == st.pop())
    matched = matched and st.isEmpty() # No unmatched delimiters left over
    return matched

def main(args: list[str]) -> int:
    instring: str = input('Please enter a string that includes delimiters ((,),[,],{,}): ')
    print('The string "' + instring + '"', end=' ')
    if match_delims(instring):
        print('contains', end=" ")
    else:
        print('does NOT contain', end=' ')
    print('balanced delimiters.')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))