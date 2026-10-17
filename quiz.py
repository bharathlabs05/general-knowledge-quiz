"""A beginner-friendly, three-question general knowledge quiz."""

QUESTIONS = (
    ("What is the capital of France?", "paris", "Paris"),
    ("What is the largest planet in our solar system?", "jupiter", "Jupiter"),
    ("What is the chemical formula for water?", "h2o", "H2O"),
)


def ask_question(question_number, question_text, expected_answer, answer_to_show):
    """Ask one question and return True when the answer is correct."""
    user_answer = input(f"{question_number}. {question_text} ").strip().lower()

    if user_answer == expected_answer:
        print("Correct!\n")
        return True
    else:
        print(f"Not quite. The correct answer is {answer_to_show}.\n")
        return False


def show_results(score, total_questions):
    """Display the final score, accuracy, and a short message."""
    accuracy = score / total_questions * 100

    print("=" * 42)
    print(f"Final score: {score}/{total_questions}")
    print(f"Accuracy: {accuracy:.0f}%")

    if score == total_questions:
        print("Excellent work - a perfect score!")
    elif score >= 2:
        print("Great job!")
    elif score == 1:
        print("Good start - keep practicing!")
    else:
        print("Keep practicing - you will get there!")

    print("=" * 42)


def main():
    """Run the quiz from start to finish."""
    score = 0
    total_questions = len(QUESTIONS)

    print("=" * 42)
    print("       GENERAL KNOWLEDGE QUIZ")
    print("=" * 42)
    print("Answer three questions. Extra spaces and capitalization do not matter.\n")

    for question_number, question in enumerate(QUESTIONS, start=1):
        question_text, expected_answer, answer_to_show = question
        if ask_question(question_number, question_text, expected_answer, answer_to_show):
            score += 1

    show_results(score, total_questions)


if __name__ == "__main__":
    main()
