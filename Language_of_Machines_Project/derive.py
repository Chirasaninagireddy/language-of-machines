
def derive(start, steps):
    s = start
    print(s)

    for lhs, rhs in steps:
        i = s.index(lhs)
        s = s[:i] + rhs + s[i+len(lhs):]
        print("=>", s or "ε")


# Type 2: a^3 b^3
print("\nTYPE 2: Context-Free Grammar")
derive("S", [("S", "aSb")] * 3 + [("S", "")])


# Type 1: a^2 b^2 c^2
print("\nTYPE 1: Context-Sensitive Grammar")
derive("S", [
    ("S", "aSBC"),
    ("S", "aBC"),
    ("CB", "BC"),
    ("aB", "ab"),
    ("bB", "bb"),
    ("bC", "bc"),
    ("cC", "cc")
])
