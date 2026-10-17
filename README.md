# General Knowledge Quiz

A small command-line quiz built with Python as Project 4 in the DecodeLabs Python Programming internship track.

The program asks three general knowledge questions, checks each answer, and prints the final score out of three.

## Features

- Three questions in a simple, repeatable question flow
- Case-insensitive answers
- Leading and trailing whitespace is ignored
- One point is added only when an answer is correct
- Clear feedback after each answer and a final score using an f-string
- No third-party packages required

## Requirements

- Python 3.8 or newer

## Run the quiz

Open a terminal in this folder and run:

```bash
python quiz.py
```

On Windows, you can also use:

```powershell
py -3 quiz.py
```

## How it works

For each question, the program reads the user's answer with `input()`, removes surrounding whitespace with `.strip()`, and normalizes capitalization with `.lower()`. It compares the result to the expected answer with `==`. An `if`/`else` branch prints feedback, and the integer `score` increases only for a correct answer. The final score is displayed with an f-string.

## Project structure

```text
general-knowledge-quiz/
├── quiz.py       # Quiz logic and command-line interface
├── README.md     # Setup and project overview
└── .gitignore    # Common Python and editor-generated files
```
