# You have to do a lot of preprocessing
# NLTK will only help pull apart and analyze text. Tag part of speech.
# It can also do stop words

# Stop words are you end the analyzing and leave
# Or words you don't need they are fluff: EX: "A, The, And, etc" Filler words

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "This is an example showing off stop word filtration."
stop_words = set(stopwords.words("english"))

words = word_tokenize(example_sentence)

filtered_sentence = []

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

# One liner: filterd_sentence = [w for w in words if not w in stop_words]

print(filtered_sentence)

# Useful for pulling database and processing times. Don't waste time on words that do not matter.