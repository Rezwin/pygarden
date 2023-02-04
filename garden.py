# This is a program using spacy (Python NLP library) to do an
# entity recognition for few example garden path sentences

import spacy

# import english model
nlp = spacy.load('en_core_web_sm')

gardenpathSentences = [ "The complex houses five married and single soldiers and their families.",
                        "The horse raced past the american barn fell.",
                        "The old man the boat.",
                        "John pushed through the door fell.",
                        "I told the girl the cat scratched Bill would help her."]

# iterate through the setences, tokenzie and identify entities
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print([(token.orth_) for token in doc])
    print([(i, i.label_, i.label) for i in doc.ents])

# spaCy (unusal) entity meanings
# CARDINAL 
#    Numerals that do not fall under another type
#    e.g: [(five, 'CARDINAL', 397)]
# NORP 
#    Nationalities or religious or political groups.
#    e.g: [(american, 'NORP', 381)]

