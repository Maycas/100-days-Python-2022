# PROJECT 17 - THE QUIZ GAME

## Instructions

Create a Quiz Game with the following requirements:

### Question Class (`question_model.py`)

Create a Question class with a constructor that will initialise 2 attributes: `text` and `answer`.

### Create a bank of questions (`main.py`)

Using `data.py`, create a bank of Question objects.

### Quiz Brain Class (`quiz_brain.py`)

Create a Quiz Brain class with the following functionality:

- Ask the questions and get the user input.
- Check if an answer is correct.
- Check if we are at the end of the quiz.

This class will have the following attributes:

- `question_number`, the question the user is currently on.
- `questions_list`, the list with all the questions to be asked to the user.
- `score`, that will keep track of the right answers.

This class will also have the following method:

- `next_question()`, will pull the question from that list, depending on the question the user is on and use an
  input to show the user the question and ask for an answer.
- `still_has_questions()`, will return True if there are still questions to go through.
- `check_answer()`, will check if the given answer is correct and update the score accordingly.

### Integrate with Open Trivia DB

In order to get additional questions, generate some new questions from Open