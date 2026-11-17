
# HAPPY OR SAD - SENTENCE MOOD DETECTOR
# AIXcelerate Python Project


# DATASET
train_data = [
    ("I got full marks in the test today!", "Happy"),
    ("We won the college cricket match", "Happy"),
    ("My friends planned a surprise party for me", "Happy"),
    ("The food in the canteen was really tasty", "Happy"),
    ("I am so excited for the weekend trip", "Happy"),
    ("Our project got selected for the exhibition", "Happy"),
    ("I finally learned how to ride a bicycle", "Happy"),
    ("Mom made my favourite sweets today", "Happy"),
    ("I lost my phone on the bus", "Sad"),
    ("I failed in the mathematics exam", "Sad"),
    ("My best friend is moving to another city", "Sad"),
    ("It rained and our picnic was cancelled", "Sad"),
    ("I missed the last bus and felt very upset", "Sad"),
    ("My laptop stopped working before the submission", "Sad"),
    ("I felt lonely during the long holidays", "Sad"),
]


# LEVEL 1: COUNT THE MOODS

def count_moods(data):
    happy_count = 0
    sad_count = 0

    for sentence, mood in data:
        if mood == "Happy":
            happy_count += 1
        elif mood == "Sad":
            sad_count += 1

    return happy_count, sad_count


print("LEVEL 1: MOOD COUNT")
print(count_moods(train_data))


# LEVEL 2: GUESS THE MOOD

# Exactly 5 words for now - change according to your roll number
happy_words = ["won", "surprise", "excited", "selected", "great"]

sad_words = ["lost", "failed", "lonely", "upset", "cancelled"]


def clean_words(sentence):
    words = sentence.lower().split()
    cleaned = []

    for word in words:
        word = word.strip(".,!?;:'\"()[]{}")
        cleaned.append(word)

    return cleaned


def guess_mood(sentence):
    happy_count = 0
    sad_count = 0

    words = clean_words(sentence)

    for word in words:
        if word in happy_words:
            happy_count += 1

        elif word in sad_words:
            sad_count += 1

    if happy_count > sad_count:
        return "Happy"

    elif sad_count > happy_count:
        return "Sad"

    else:
        # Tie: choose Happy because it is our default prediction
        return "Happy"


# LEVEL 3: TEST THE PROGRAM

practice_data = [
    ("I won a medal in the sports meet", "Happy"),
    ("I lost my notebook before the exam", "Sad"),
    ("My friends gave me a lovely surprise", "Happy"),
    ("The train was late and I felt upset", "Sad"),
    ("Today was a great day", "Happy"),
]


print("\nLEVEL 3: PRACTICE TEST")

correct = 0

for sentence, actual_mood in practice_data:
    predicted_mood = guess_mood(sentence)

    print("\nSentence:", sentence)
    print("Actual mood:", actual_mood)
    print("Predicted mood:", predicted_mood)

    if predicted_mood == actual_mood:
        correct += 1

accuracy = (correct / len(practice_data)) * 100

print("\nCorrect predictions:", correct)
print("Total sentences:", len(practice_data))
print("Accuracy:", accuracy, "%")


# BONUS: LEARNING WORD SCORES

def learn_scores(data):
    scores = {}

    for sentence, mood in data:
        words = clean_words(sentence)

        for word in words:
            if word not in scores:
                scores[word] = 0

            if mood == "Happy":
                scores[word] += 1

            elif mood == "Sad":
                scores[word] -= 1

    return scores


def guess_mood_learned(sentence, scores):
    total_score = 0

    words = clean_words(sentence)

    for word in words:
        total_score += scores.get(word, 0)

    if total_score > 0:
        return "Happy"
    else:
        return "Sad"


# TRAIN AND TEST THE LEARNED MODEL

print("\nBONUS: LEARNED MOOD DETECTOR")

scores = learn_scores(train_data)

print("Learned word scores:", scores)

learned_correct = 0

for sentence, actual_mood in practice_data:
    predicted_mood = guess_mood_learned(sentence, scores)

    print("\nSentence:", sentence)
    print("Actual mood:", actual_mood)
    print("Learned prediction:", predicted_mood)

    if predicted_mood == actual_mood:
        learned_correct += 1

learned_accuracy = (
    learned_correct / len(practice_data)
) * 100

print("\nLearned model accuracy:", learned_accuracy, "%")

