#%%
import nltk
#%%
wn.synset( 'net.v.02' ).lemmas()

#%%
for lem in wn.synset('net.v.02').lemmas():
    print(lem.name())
#%%
for synset in wn.synsets('clear'):
    print(synset,": ", synset.lemma_names(), ": ", len(synset.lemma_names()))
#%%
for synset in wn.synsets('clear'):
    print(synset.lemma_names(), ": Part of Speech: ", synset.pos(), ":Definition: ", synset.definition())
#%%
spooky_words = ['creep', 'eldritch', 'horror', 'cry', 'scream', 'ghost', 'scare']
for w in spooky_words:
    synsets = len(wn.synsets(w))
    print("The word ", w, "belongs to ", synsets, "synsets in WordNet.")
#%%
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

filepath = 'hughes-txt/batmanforever.txt'
f = open(filepath, 'r', encoding='utf8').read()
# tokenList = f.split()
tokenList = word_tokenize(f)

#%%
lowercaseTokens = [token.lower() for token in tokenList]
uniqueTokens = set(lowercaseTokens)
print(uniqueTokens)
#%%
import nltk
nltk.data.path.append('/Users/chelseaquijas/nltk_data/')
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

#%%
import nltk
nltk.help.upenn_tagset('VBD')
#%%
from nltk.tokenize import word_tokenize
#%%
text = "this is an example sentence for tokenization and POS tagging."
#%%
tokens = word_tokenize(text)
#%%
uniqueTokens = list(set(tokens))
#%%
from nltk import pos_tag
POStagged = pos_tag(uniqueTokens)
#%%
tagsIwant = ['VBD', 'VBN', 'VBZ']
shortList = [word for word, tag in POStagged if tag in tagsIwant]
print(len(shortList))            
print(shortList)
#%%
import nltk
#%%
for w in shortList:
    lemma = wn.morphy(w)
    print(f"word: {w} | Wordnet Lemma: {lemma}")
    synsets = wn.synsets(lemma)
    if synsets:
        print(f" Word: {w}, Number of Synsets (Ambiguity): {len(synsets)}")
#%%
import os
cwd = os.getcwd()
print(cwd)
#%%
filepath = 'batmanforever.txt'
print(filepath)
#%%
f = open(filepath, 'r', encoding='utf8').read()
print(f)
#%%
os.listdir(cwd)


coll = os.path.join(cwd, 'hughes-txt')
os.listdir(coll)
#%%
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
#%%
file_path = 'batmanscript1.txt'
#%%
with open(file_path, 'r') as file:
    text = file.read()
#%%
sentences = sent_tokenize(text)
#%%
tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]
#%%
print(tokenized_sentences[:5])
#%%
import nltk
from nltk import FreqDist, ConditionalFreqDist
from nltk.tokenize import word_tokenize
#%%
file_path = 'batmanscript1.txt'
#%%
with open(file_path, 'r') as file:
    text = file.read()
#%%
words = word_tokenize(text)
#%%
pairs = [('text_section', word) for word in words]
#%%
cfd = ConditionalFreqDist(pairs)
#%%
print(cfd.conditions())
print(cfd['text_sectiobn'])

print(cfd['text_section'].most_common(5))
#%%
import matplotlib.pyplot as plt
#%%
cfd['text_section'].plot()
#%%
print(cfd['custom_condition'].most_common(5))
#%%
