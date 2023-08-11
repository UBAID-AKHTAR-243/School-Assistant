import json

from flask import Flask,request, jsonify
import random
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer

with open("intents.json", "w") as f:
    json.dump("intents", f)
    
intents = json.loads(open('intents.json').read())
    

lemmatizer = WordNetLemmatizer()
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


def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
           return random.choice(i['responses'])
    message=input("")
    intents_list = predict_class(message)
    result = get_response(intents_list, intents)
    return result

    
    


