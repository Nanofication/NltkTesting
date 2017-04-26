# You can use text classifications for any kinds of things
# Discerning if anything is spam

# This tutorial classifies if word is positive or negative.
# Only for 2 categories and if it is tagged

# Pickle is a a way to save python objects

import nltk
import random
from nltk.corpus import movie_reviews # Training data
import pickle

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)] # List of tuples

# documents = []
# for category in movie_reviews.categories():
#     for fileid in movie_reviews.fileids(category):
#         documents.append(list(movie_reviews.words(fileid), category))

# Naive bayes theorem
random.shuffle(documents)

all_words = []

for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words) # Frequency distribution
# print(all_words.most_common(15))

word_features = list(all_words.keys())[:3000]

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev), category) for(rev, category) in documents]

# Completing the Naive Bayes algorithm to categorize as positive or negative sentiment

training_set = featuresets[:1900] #Keep separate to avoid bias
testing_set = featuresets[1900:]

# We don't tell the machine in testing set what category it is. Machine takes set and compares to known categories
# Sometimes called "Stupid bayes" has a lot of flaws. Short algorithm that can be scaled
# Baye's algorithm - Posterior = prior occurences x likelihood/ evidence

"Old training code"
# classifier = nltk.NaiveBayesClassifier.train(training_set)


#Instead of training
classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

print("Naive Bayes Algo Accuracy: ", (nltk.classify.accuracy(classifier, testing_set)) * 100) # accuracy percentage
classifier.show_most_informative_features(15)

# None of these had grammar
# Next time improve accuracy and reliability

# First save classifier
# save_classifier = open("naivebayes.pickle", "wb")
# pickle.dump(classifier, save_classifier)
# save_classifier.close()

# Accuracy is unreliable. Algorithm's accuracy goes up and down everywhere. 