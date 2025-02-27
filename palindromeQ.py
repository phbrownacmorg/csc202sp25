from Stack import Stack
from CircQ import Queue

def is_palindrome(s: str) -> bool:
    """Returns True iff S is a palindrome."""
    st: Stack[str] = Stack[str]()
    q: Queue[str] = Queue[str]()
    palindrome: bool = True

    for c in s:
        if c.isalpha(): # If c is interesting...
            st.push(c.lower())
            q.add(c.lower())

    while not st.isEmpty():
        if st.pop() != q.pop():
            palindrome = False
    # Post:
    assert q.isEmpty(), "Failed postcondition" # Should never trigger
    return palindrome

def main(args: list[str]) -> int:

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))