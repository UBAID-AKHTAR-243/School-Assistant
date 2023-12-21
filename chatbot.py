import tensorflow as tf
import nltk
import random
import pickle
import json
import numpy as np
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD
nltk.download('wordnet')
nltk.download('punkt')
lemmatizer = WordNetLemmatizer()
from tensorflow.keras.models import load_model
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
sentences = pickle.load(open('classes.pkl', 'rb'))


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag_1 = [0] * len(words)
    for W in sentence_words:
        for i, word in enumerate(words):
            if word == W:
                bag_1[i] = 1
    return np.array(bag_1)


def predict_class(user_input):
    bow = bag_of_words(user_input)
    res_1 = model.predict(np.array([bow]))[0]
    error_threshold = 0.25
    results = [[i, r] for i, r in enumerate(res_1)
               if r > error_threshold]
    results.sort(key=lambda x: x[1], reverse=True)
    predicted_intent_list = []
    for r in results:
        predicted_intent_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return  predicted_intent_list


def get_response(predicted_intent_list, intents):
    tag = predicted_intent_list[0]['intent']
    # Retrieve the list of intents from intents_json
    list_of_intents = intents['intents']
    # Search for a matching intent in the list_of_intents
    for i in list_of_intents:
        if i['tag'] == tag:
            # If a matching intent is found,
            # return a random response from its list
            return random.choice(i['responses'])
print('Welcome to Shiblee College! \n Ask your Questions!')
