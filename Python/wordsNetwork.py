import spacy
import os
import pandas as pd
import nltk
from nltk.corpus import wordnet as wn


spacy.cli.download("en_core_web_lg")
nltk.download('wordnet')


nlp = spacy.load("en_core_web_lg")


collPath = "python"
allDataFrames = []


def wordCollector(words, unit):
    wordList = []
    nodeAtts = []
    synsetCounts = []
    unitList = []
    for token in words:
        if token.pos_ == "NOUN":
            synsets = len(wn.synsets(token.lemma_))
            wordList.append(token.lemma_)
            nodeAtts.append(token.pos_)
            synsetCounts.append(synsets)
            unitList.append(unit)

    data = {
        'words': wordList,
        'nodeTypes': nodeAtts,
        'synsetCount': synsetCounts,
        'units': unitList
    }
    df = pd.DataFrame(data)
    return df


for file in os.listdir(collPath):
    if file.endswith("batmanforever.txt"):
        filepath = os.path.join(collPath, file)
        name, _ = os.path.splitext(file)
        with open(filepath, 'r', encoding='utf8') as f:
            readFile = f.read()
            spacyRead = nlp(readFile)
            myDataFrame = wordCollector(spacyRead, name)
            allDataFrames.append(myDataFrame)


outputFilePath = 'networkData.tsv'
fullDataFrame = pd.concat(allDataFrames, ignore_index=True)
fullDataFrame.to_csv(outputFilePath, sep='\t', index=False)
print('I just saved a DataFrame as a TSV file.')
