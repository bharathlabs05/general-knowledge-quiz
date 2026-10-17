"""A small, beginner-friendly general knowledge quiz."""


def main():
    """Ask three questions and report the player's final score."""
    score = 0
    total_questions = 3

    print("=" * 42)
    print("       GENERAL KNOWLEDGE QUIZ")
    print("=" * 42)
    print("Answer each question. Capitalization and extra spaces do not matter.\n")

    # Question 1: capture, sanitize, compare, and update the score.
    answer_1 = input("1. What is the capital of France? ").strip().lower()
    if answer_1 == "paris":
        print("Correct!\n")
        score += 1
    else:
        print("Not quite. The answer is Paris.\n")

    # Question 2: the score only changes when the answer is correct.
    answer_2 = input("2. What is the largest planet in our solar system? ").strip().lower()
    if answer_2 == "jupiter":
        print("Correct!\n")
        score += 1
    else:
        print("Not quite. The answer is Jupiter.\n")

    # Question 3: use the same input and scoring pattern again.
    answer_3 = input("3. What is the chemical formula for water? ").strip().lower()
    if answer_3 == "h2o":
        print("Correct!\n")
        score += 1
    else:
        print("Not quite. The answer is H2O.\n")

    print("=" * 42)
    print(f"Quiz complete! Your final score is {score}/{total_questions}.")
    print("=" * 42)


if __name__ == "__main__":
    main()
