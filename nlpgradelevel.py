'''

Code for computing the grade level of the text through natural langauge processing.
Learned for this tutorial:  https://www.geeksforgeeks.org/readability-index-pythonnlp/

'''

import spacy
from textstat.textstat import textstatistics,legacy_round
import re

def break_sentences(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    return list(doc.sents)
 
def word_count(text):
    sentences = break_sentences(text)
    words = 0
    for sentence in sentences:
        words += len([char for char in sentence])
    return words
 
def sentence_count(text):
    sentences = break_sentences(text)
    return len(sentences)
 
def avg_sentence_length(text):
    words = word_count(text)
    sentences = sentence_count(text)
    average_sentence_length = float(words / sentences)
    return average_sentence_length
 
def syllables_count(word):
    return textstatistics().syllable_count(word)

def avg_syllables_per_word(text):
    syllable = syllables_count(text)
    words = word_count(text)
    ASPW = float(syllable) / float(words)
    return legacy_round(ASPW, 1)
 
def difficult_words(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    words = []
    sentences = break_sentences(text)
    for sentence in sentences:
        words += [str(token) for token in sentence]

    diff_words_set = set()
     
    for word in words:
        syllable_count = syllables_count(word)
        if word not in nlp.Defaults.stop_words and syllable_count >= 2:
            diff_words_set.add(word)
 
    return len(diff_words_set)


def flesch_reading_ease(text):
    """
        Implements Flesch Formula:
        Reading Ease score = 206.835 - (1.015 × ASL) - (84.6 × ASW)
        Here,
          ASL = average sentence length (number of words
                divided by number of sentences)
          ASW = average word length in syllables (number of syllables
                divided by number of words)
    """
    FRE = 206.835 - float(1.015 * avg_sentence_length(text)) -\
          float(84.6 * avg_syllables_per_word(text))
    return legacy_round(FRE, 2)


def get_literacy_level(text):
    
    lit_score = flesch_reading_ease(text)
    if lit_score >= 70:
        literacy_level = "Basic"
    elif lit_score >= 30: 
        literacy_level = "Intermediate"
    elif lit_score < 30:
        literacy_level = "High"

    return literacy_level, lit_score 

#Regular expressions
def count_key_words(keys, abstract):
    '''
    Finds all occurences of the search terms in the abstract
    '''
    search = re.findall(keys, abstract)
    total_occurrences = len(search)
    # unique_occurrences = len(set(search))

    return total_occurrences


    



