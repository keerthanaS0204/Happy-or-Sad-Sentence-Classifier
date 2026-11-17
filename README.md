# Happy-or-Sad-Sentence-Classifier
Accuracy on the 5 practice sentences: 80%

1. Which sentence went wrong (or was closest to going wrong), and why?

The sentence "I lost my notebook before the exam" went wrong. My program predicted Happy instead of Sad because the word "lost" is not included in my sad_words list. Since neither of my clue words was found, the program followed the tie-breaking rule and predicted Happy.

2. One change that would make my program better:

I can improve my program by adding more ways to understand the meaning and context of sentences. This would help the program identify emotions more accurately.

Learning Questions

1. Total score of "good party today" and its mood:

good = +2
party = +1
today = 0

Total score = +3

Mood: Happy, because the total score is positive.

2. Total score of "bad exam day" and its mood:

bad = -2
exam = 0
day = -1

Total score = -3

Mood: Sad, because the total score is negative.

3. Why did "exam" get a score of 0, and is that good or bad?

The word "exam" appeared once in a Happy sentence and once in a Sad sentence. Therefore, its positive and negative scores cancelled each other, resulting in zero. This is useful because the word "exam" alone does not clearly indicate whether a sentence is Happy or Sad.

4. Why is "not good" labelled Happy by this method, and how could it be fixed?

The word "good" has a positive score of +2, while the word "not" has a score of 0. Therefore, the total score becomes +2, and the program predicts Happy. This is incorrect because the word "not" changes the meaning of "good". It can be fixed by identifying negative words such as "not" and reversing the score of the following word.

AI Declaration

I used an AI tool: Yes

If yes, what I asked it:

I used AI to understand the Python project instructions, learn how to write the functions, identify suitable clue words, understand the word-scoring method, debug my code and prepare the README documentation.

Reflection

The hardest part of this project was selecting clue words with a limited number of words and understanding why the program sometimes predicted the wrong mood. I learned how to use Python functions, lists, loops, conditional statements and string operations. I also learned how to calculate accuracy and understood for the first time how a computer can learn word scores from examples. This project helped me understand the basic idea of machine learning and its limitations.
