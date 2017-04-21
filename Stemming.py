# Stemming- form of data preprocessing. Kind of like normalization
# Take words and root stem of the word. Ex: Riding's Stem = Rid
# Rid can be used for Ride, Ridden

# Why use a stem? Have different word variations based on the stem. But the meaning of the word is unchanged

# I was taking a ride in the car.
# I was riding in the car.

# The 2 sentences means the exact same thing and use of the word is identical

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]

# for w in example_words:
#     print(ps.stem(w))

new_text = "It is very important to e pythonly while you are pythoning with python. All pythoners have pythoned poorly " \
           "at least once."

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))

# Depends on what you want to feed word. Or use word net to find synonyms.
# It may or may not use this that much. 