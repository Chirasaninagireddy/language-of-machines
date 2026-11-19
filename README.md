
# The Language of Machines
### From Formal Grammars to the Chomsky Hierarchy

## Project Overview

This project demonstrates the Chomsky Hierarchy using Python. It explains the four types of formal grammars and their corresponding computational models through practical examples and derivation simulations.

## Course Details

- Course: Formal Languages and Automata Theory
- Course Code: 24CSE547
- Project: The Language of Machines

## Objectives

- Understand formal grammars and languages.
- Explore the four types of the Chomsky Hierarchy.
- Simulate grammar derivations using Python.
- Understand the relationship between grammars and computational machines.

## Chomsky Hierarchy

| Type | Grammar | Computational Model |
|---|---|---|
| Type 0 | Unrestricted | Turing Machine |
| Type 1 | Context-Sensitive | Linear-Bounded Automaton |
| Type 2 | Context-Free | Pushdown Automaton |
| Type 3 | Regular | Finite Automaton |

## Project Implementation

### Type 3 - Regular Grammar
Recognises strings over {a, b} that end with `ab`.

### Type 2 - Context-Free Grammar
Uses the production rule:

`S → aSb | ε`

Generates strings such as `aaabbb`.

### Type 1 - Context-Sensitive Grammar
Demonstrates the derivation of:

`aabbcc`

### Type 0 - Unrestricted Grammar
Explains unrestricted production rules and their relationship with Turing machines.

## Slide 15 - Python Demonstration

The `derive.py` program simulates grammar derivations.

**Type 2 Output:**
```text
S
=> aSb
=> aaSbb
=> aaaSbbb
=> aaabbb
```

**Type 1 Output:**
```text
S
=> aSBC
=> aaBCBC
=> aaBBCC
=> aabBCC
=> aabbCC
=> aabbcC
=> aabbcc
```

## Technologies Used

- Python 3
- Visual Studio Code
- Git
- GitHub

## How to Run

1. Clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run:

```bash
python derive.py
```

## Project Structure

```text
language-of-machines/
│
├── main.py
├── derive.py
└── README.md
```

## Learning Outcomes

- Understanding formal language concepts.
- Classifying grammars using the Chomsky Hierarchy.
- Simulating grammar derivations in Python.
- Connecting theoretical concepts with practical programming.

## Conclusion

This project provides a practical demonstration of formal grammars and the Chomsky Hierarchy. It shows how different grammar types generate languages and how computational models recognise them.
