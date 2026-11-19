# The Language of Machines
## From Formal Grammars to the Chomsky Hierarchy

A beginner-friendly Python command-line project based on the presentation for **24CSE547 - Formal Languages and Automata Theory**.

## Project overview

This project demonstrates the four levels of the Chomsky hierarchy:

- **Type 0 - Unrestricted grammar:** explains the connection to Turing machines.
- **Type 1 - Context-sensitive grammar:** displays a derivation of `aabbcc` using the presentation's grammar.
- **Type 2 - Context-free grammar:** generates strings in the language `{ a^n b^n | n >= 0 }` using `S -> aSb | ε`.
- **Type 3 - Regular grammar:** checks whether a string over `{a,b}` ends with `ab`.

It also classifies the five example grammars and compares the memory used by the corresponding computational models.

## Requirements

- Python 3.8 or newer
- VS Code (recommended) or any Python terminal

No external Python packages are required.

## How to run in VS Code

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open **Terminal -> New Terminal**.
4. Run:

   ```bash
   python main.py
   ```

   On some Windows installations, use:

   ```bash
   py main.py
   ```

5. Select an option from the menu by entering its number.

## Demonstration steps

### Demo 1: Type 3
- Enter `1`.
- Enter `bab`.
- Expected result: `ACCEPTED`, because the string ends with `ab`.
- Try `abba`; expected result: `REJECTED`.

### Demo 2: Type 2
- Enter `2`.
- Enter `3`.
- The derivation ends with `aaabbb`.

### Demo 3: Type 1
- Enter `3`.
- The program displays the derivation ending in `aabbcc`.

### Demo 4: Grammar classification
- Enter `5`.
- The program displays G1 to G5 and their classifications.

### Demo 5: Hierarchy comparison
- Enter `6`.
- The program compares grammar types, machines, and memory.

## Project structure

```text
Language_of_Machines_Project/
├── main.py
└── README.md
```

## Important academic note

The Type 0 menu option is a conceptual explanation, not a general Type 0 grammar execution engine. In general, membership for unrestricted grammars is undecidable. The Type 1 and Type 2 derivations shown here follow the examples in the presentation.

## Learning outcomes

1. Understand alphabets, strings, languages, and grammar derivations.
2. Identify the four grammar classes in the Chomsky hierarchy.
3. Relate grammar classes to finite automata, pushdown automata, linear-bounded automata, and Turing machines.
4. Observe simple grammar derivations and string recognition using Python.

## Author / team details

Add the correct project team member names and USNs here before submission.
