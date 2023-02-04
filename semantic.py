import spacy

nlp = spacy.load('en_core_web_md')

# Example 1 - Word simlarity
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

print(nlp("dog").similarity(nlp("puppy")))

# Note:
# Cat and Monkey are animals and a higher similarity index
# Cat and banana have low similarity as they are rarely related
# Same words have high similarity of 1 as expected
# Dog and puppy has good similarity
#  
# Example 2
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Example 3 - Sentence simlarity
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go","Hello, there is my car","I\'ve lost my car in my car","I\'d like my boat back","I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# Note: The above excerise can also used with simpler en_core_web_sm model
# The main difference is en_core_web_sm model doesn't support vector semantic
# support. That means we cannot compare sentences like in exampel 3

