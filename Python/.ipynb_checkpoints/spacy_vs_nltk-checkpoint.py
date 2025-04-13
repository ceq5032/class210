import spacy
import nltk
from nltk.corpus import wordnet as wn
from collections import Counter

# Load spaCy model
nlp = spacy.load("en_core_web_lg")

# Read the file
filepath = 'hughes-txt/batmanforever.txt'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Process with spaCy
spacy_doc = nlp(text)

# Print token info
for token in spacy_doc:
    print(token.text, "---->", token.pos_, ":::::", token.lemma_)

# Collect verb lemmas
def wordCollector(words):
    return [token.lemma_ for token in words if token.pos_ == "VERB"]

myWords = wordCollector(spacy_doc)
print(myWords)

# Frequency analysis
word_freq = Counter(myWords)
ranked = word_freq.most_common()
topTen = word_freq.most_common(10)
lastTen = word_freq.most_common()[:-11:-1]

print(topTen)
print(lastTen)

# Write full ranking to file
with open("verbFreq.txt", "w", encoding='utf-8') as o:
    for r in ranked:
        o.write(str(r) + "\n")

# Process for WordNet and sorting
setOfWords = set(myWords)
lowerCased = [w.lower() for w in setOfWords]
sortedWords = sorted(lowerCased)
print(sortedWords)

# WordNet synsets count
for w in myWords:
    synsets = len(wn.synsets(w))
    print("The word", w, "belongs to", synsets, "synsets in WordNet.")


