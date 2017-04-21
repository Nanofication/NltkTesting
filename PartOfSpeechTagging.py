# Part of Speech Tagging

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

sample_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

'''
POS tag list:

CC	coordinating conjunction
CD	cardinal digit
DT	determiner
EX	existential there (like: "there is" ... think of it like "there exists")
FW	foreign word
IN	preposition/subordinating conjunction
JJ	adjective	'big'
JJR	adjective, comparative	'bigger'
JJS	adjective, superlative	'biggest'
LS	list marker	1)
MD	modal	could, will
NN	noun, singular 'desk'
NNS	noun plural	'desks'
NNP	proper noun, singular	'Harrison'
NNPS	proper noun, plural	'Americans'
PDT	predeterminer	'all the kids'
POS	possessive ending	parent's
PRP	personal pronoun	I, he, she
PRP$	possessive pronoun	my, his, hers
RB	adverb	very, silently,
RBR	adverb, comparative	better
RBS	adverb, superlative	best
RP	particle	give up
TO	to	go 'to' the store.
UH	interjection	errrrrrrrm
VB	verb, base form	take
VBD	verb, past tense	took
VBG	verb, gerund/present participle	taking
VBN	verb, past participle	taken
VBP	verb, sing. present, non-3d	take
VBZ	verb, 3rd person sing. present	takes
WDT	wh-determiner	which
WP	wh-pronoun	who, what
WP$	possessive wh-pronoun	whose
WRB	wh-abverb	where, when
'''

# Part of speech tagging may mess up from time to time like nouns. Or if you're reading twitter.
# Depends no where you're using things from data sets

custom_sent_tokenizer = PunktSentenceTokenizer(sample_text)
# Training the tokenizer on that text

tokenized = custom_sent_tokenizer.tokenize(sample_text)

# def process_content():
#     try:
#         for i in tokenized:
#             words = nltk.word_tokenize(i)
#             tagged = nltk.pos_tag(words)
#
#             print(tagged)
#
#     except Exception as e:
#         print(str(e))
# Create tuples of each word and part of speech

# After splitting by words, you then do tagging
# Corporas are important



#### CHUNKING! What's the next step to figure out the meaning of the sentence?
# Words that modify or affect that noun

# Chunks put into noun phrases. Only group things together like chunks and break out from there
# Lets visualize

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            chunkGram = "rChunk: {<RB.?>*<VB.?><NNP><NN>?}"   # Any form of an adverb and we're looking for zero or 1 more of these

            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)

            chunked.draw()

            print(chunked)

            # NNP singular proper noun
            # NN Possible singular
            # Regex: Any characters except for a new line
            # question mark is zero or one
    except Exception as e:
        print(str(e))


# process_content()

#Chunk is extremely basic. It would group things possibly together and get very long

# Chinking, removal of some things.

# def process_content_chinking():
#     try:
#         for i in tokenized[5:]:
#             words = nltk.word_tokenize(i)
#             tagged = nltk.pos_tag(words)
#
#             # Chinking = }{
#             chunkGram = r"""Chunk: {<.*>+}
#                         }<VB.?|IN|DT|TO>+{"""
#
#             chunkParser = nltk.RegexpParser(chunkGram)
#             chunked = chunkParser.parse(tagged)
#
#             chunked.draw()
#
#             print(chunked)
#
#     except Exception as e:
#         print(str(e))
#
# process_content_chinking()

# Get comfortable with Regular Expressions. Regex

# You can classify names together. Name entity recognitions sometimes. Can miss names

# Named Entity Recognition ----------------------------------

# United States is a named Entity

def process_content():
    try:
        for i in tokenized[5:]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            namedEnt = nltk.ne_chunk(tagged)

            # White house is considered separate
            # Binary True sees white house as one entity

            # False positives and error rates are high for named entity recognition
            # Recommend just look for nouns and then do something with it to create an entity

            namedEnt.draw()
    except Exception as e:
        print(str(e))

process_content()