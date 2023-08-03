import os
import json
import random
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
#from tensorflow.keras.models import load_model
lemmatizer = WordNetLemmatizer()
#intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
sentences = pickle.load(open('classes.pkl', 'rb'))


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize (word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)
    for W in sentence_words:
        for i, word in enumerate(words):
            if word == W:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words (sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res)
if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list




import random
def get_response(intents_list, intents_json):
    # Extract the predicted intent from the intents_list
    tag = intents_list[0]['intent']
    # Retrieve the list of intents from intents_json
    list_of_intents = intents_json['intents']
    # Search for a matching intent in the list_of_intents
    for i in list_of_intents:
        if i['tag'] == tag:
            # If a matching intent is found,
#return a random response from its list
           return random.choice(i['responses'])
           if i['tag'] != tag:
# If no matching intent is found, return a default responses written.
               print( "Sorry, I can't answer that. It's not relevant to me.")
print("Welcome to Assistant Shiblee College! \n Ask your Questions!")
while True:
    message=input("")
    ints = predict_class(message)
    res = get_response(ints, intents)
    print(res)