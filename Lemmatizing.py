# Lemmatizing is like stemming but the end result is like a real word
# some form of synonym to the original word. Might be completely different but
# the meaning should be the same


from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# print(lemmatizer.lemmatize("cats"))
# print(lemmatizer.lemmatize("cacti"))
# print(lemmatizer.lemmatize("geese"))
# print(lemmatizer.lemmatize("rocks"))
# print(lemmatizer.lemmatize("python"))

print(lemmatizer.lemmatize("better"))
print(lemmatizer.lemmatize("better", pos = "a"))
print(lemmatizer.lemmatize("best", pos = "a"))
print(lemmatizer.lemmatize("run"))

print(lemmatizer.lemmatize("run","v"))