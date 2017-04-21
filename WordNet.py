# WordNet - Largest capabilitied Corpora

from nltk.corpus import wordnet

syns = wordnet.synsets("program")



print(syns[0])
#Synset
print(syns[0].lemmas())

# Just the word
print(syns[0].lemmas()[0].name())

# Definition

print(syns[0].definition())

# Examples
print(syns[0].examples())

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        print("l: ", l)
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())


#print(set(synonyms))
#print(set(antonyms))

# Similarities

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")

#wup = wu and palmer wrote a paper on semantic similarities
print(w1.wup_similarity(w2)) # returns 0.90909 this is about 90% similar

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("car.n.01")

#wup = wu and palmer wrote a paper on semantic similarities
print(w1.wup_similarity(w2)) # returns 0.6956

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("cat.n.01")

#wup = wu and palmer wrote a paper on semantic similarities
print(w1.wup_similarity(w2)) # returns 0.32


# Synsets are used to rewrite things. Business may sell you term papers for school
# You can just buy a term paper and then use nlp to switch words around then sell again
# This is horrible

# School can use nlp to reverse and check if paper has been switching synonyms around
# Catch people cheating on term papers
# Also for people who make newsbots that want to edit things or write articles and switch few things around


