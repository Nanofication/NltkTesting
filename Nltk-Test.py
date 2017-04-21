from nltk.tokenize import sent_tokenize, word_tokenize


# Tokenizers - Word tokenizers and sentence tokenizers.
# Word tokenizer separates by words
# Sentence tokenizer separates by sentences
# Lexicons and Corporas

# Corpora is body of text: Example medical journals, presidential speeches, IEnglish Language

# Lexicon - Words and their meanings

# Investor-speak ... regular english - speak

# Investor speak 'bull' - someone who is positive about the market
# English speak 'bull' - scary animal you don't wanting running at you

# You can potentially use nltk's own ML to make your own word recognizers

example_text = "Hello Mr. Smith, how are you doing today? The weather is great and python is awesome. The sky is pinkesh-blue. " \
               "You should not eat cardboard"

# print(sent_tokenize(example_text)) # This captured this as a sentence. It also recognizes Mr. Smith as one thing
#
# print(word_tokenize(example_text)) # This split by word and treats punctuations as its word but also recognizes Mr. successfully

for i in word_tokenize(example_text):
    print(i)