"""
THE LANGUAGE OF MACHINES
From Formal Grammars to the Chomsky Hierarchy

Educational demonstration project based on the accompanying presentation.
Run: python main.py
"""

import re


def derive(start, steps):
    """Apply each (left_side, right_side) production once and print the derivation."""
    current = start
    history = [current]
    for lhs, rhs in steps:
        if lhs not in current:
            raise ValueError(f"Cannot apply rule {lhs} -> {rhs}: '{lhs}' not found.")
        current = current.replace(lhs, rhs, 1)
        history.append(current if current else "ε")
    return history


def show_derivation(title, start, steps):
    print(f"\n{title}")
    print("-" * len(title))
    for index, value in enumerate(derive(start, steps)):
        if index == 0:
            print(value)
        else:
            print("=>", value)


def type3_demo():
    """Recognise strings over {a,b} that end with 'ab'."""
    print("\nTYPE 3 - REGULAR GRAMMAR")
    print("Language: strings over {a, b} that end with 'ab'")
    print("Grammar: S -> aS | bS | aA ; A -> b")
    print("Equivalent regular expression: (a|b)*ab")
    value = input("Enter a string containing only a and b: ").strip()

    if not re.fullmatch(r"[ab]*", value):
        print("Invalid input: use only a and b.")
    elif value.endswith("ab"):
        print(f"ACCEPTED: '{value}' belongs to the language.")
    else:
        print(f"REJECTED: '{value}' does not end with 'ab'.")


def type2_demo():
    """Generate a^n b^n using S -> aSb | epsilon."""
    print("\nTYPE 2 - CONTEXT-FREE GRAMMAR")
    print("Grammar: S -> aSb | ε")
    print("Language: { a^n b^n | n >= 0 }")
    try:
        n = int(input("Enter n (0 to 10): "))
        if not 0 <= n <= 10:
            print("Please enter a number from 0 to 10.")
            return
    except ValueError:
        print("Please enter a valid integer.")
        return

    steps = [("S", "aSb")] * n + [("S", "")]
    show_derivation(f"Derivation for a^{n}b^{n}", "S", steps)
    print(f"Generated string: {'a' * n + 'b' * n or 'ε'}")


def type1_demo():
    """Show the n=2 derivation for a^n b^n c^n from the presentation."""
    print("\nTYPE 1 - CONTEXT-SENSITIVE GRAMMAR")
    print("Language: { a^n b^n c^n | n >= 1 }")
    print("Demonstration uses n = 2 (aabbcc).")
    steps = [
        ("S", "aSBC"),
        ("S", "aBC"),
        ("CB", "BC"),
        ("aB", "ab"),
        ("bB", "bb"),
        ("bC", "bc"),
        ("cC", "cc"),
    ]
    show_derivation("Derivation for aabbcc", "S", steps)
    print("Generated string: aabbcc")


def type0_demo():
    print("\nTYPE 0 - UNRESTRICTED GRAMMAR")
    print("Type 0 production rules have no general length-preserving restriction.")
    print("They correspond to Turing machines and recursively enumerable languages.")
    print("Important: membership for arbitrary Type 0 grammars is undecidable.")
    print("This project explains the concept; it does not implement a universal")
    print("Type 0 grammar solver.")


def classify_grammar():
    """Classify the five example grammars from the presentation."""
    print("\nGRAMMAR CLASSIFICATION")
    print("The examples below are from the presentation.")
    examples = [
        ("G1", "S -> aS | b", "Type 3", "Right-linear productions."),
        ("G2", "S -> aSb | ab", "Type 2", "One variable on the left; not right-linear."),
        ("G3", "S -> SS | (S) | ε", "Type 2", "One variable on each left side."),
        ("G4", "S -> aSBC | aBC; CB -> BC; aB -> ab; ...",
         "Type 1", "Non-contracting rules with multi-symbol left sides."),
        ("G5", "S -> ABC; AB -> a; C -> c",
         "Type 0", "AB -> a is contracting."),
    ]
    for name, grammar, kind, reason in examples:
        print(f"\n{name}: {grammar}\nClassification: {kind}\nReason: {reason}")


def compare_hierarchy():
    print("\nCHOMSKY HIERARCHY")
    rows = [
        ("Type 3", "Regular", "Finite Automaton (DFA/NFA)", "Current state"),
        ("Type 2", "Context-Free", "Pushdown Automaton", "Stack"),
        ("Type 1", "Context-Sensitive", "Linear-Bounded Automaton", "Input-bounded tape"),
        ("Type 0", "Unrestricted", "Turing Machine", "Unbounded tape"),
    ]
    print(f"{'Type':<10} {'Grammar':<20} {'Machine':<30} Memory")
    print("-" * 82)
    for row in rows:
        print(f"{row[0]:<10} {row[1]:<20} {row[2]:<30} {row[3]}")
    print("\nInclusion: Type 3 ⊂ Type 2 ⊂ Type 1 ⊂ Type 0")


def main():
    while True:
        print("\n" + "=" * 58)
        print(" THE LANGUAGE OF MACHINES - PROJECT DEMONSTRATION")
        print("=" * 58)
        print("1. Type 3 - Regular string recognition")
        print("2. Type 2 - Context-free grammar derivation")
        print("3. Type 1 - Context-sensitive grammar derivation")
        print("4. Type 0 - Concept demonstration")
        print("5. Classify example grammars")
        print("6. Compare the Chomsky hierarchy")
        print("0. Exit")

        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            type3_demo()
        elif choice == "2":
            type2_demo()
        elif choice == "3":
            type1_demo()
        elif choice == "4":
            type0_demo()
        elif choice == "5":
            classify_grammar()
        elif choice == "6":
            compare_hierarchy()
        elif choice == "0":
            print("Thank you for using The Language of Machines project.")
            break
        else:
            print("Invalid choice. Please select 0 to 6.")


if __name__ == "__main__":
    main()
