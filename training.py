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
with open("intents.json", "w") as f:
    json.dump("intents", f)

intents = json.loads(open('intents.json').read())


words = []  # All tokenized words of  a pattern (one sentence).
classes = []  # list of names of all tags
documents = []  # list of sentences .Each sentence has tokenized words  .
ignore_letters = ['?', '!', '.', ',']
# intents_json is variable of  (intents.json file after read and saved)
for intent in intents["intents"]:
    # mean key named "patterns" of single intent.
    # pattern mean one sentence in the "patterns" key wali line main.
    for pattern in intent["patterns"]:
        # list of tokenized words in one sentence in "patterns" (single key).
        # because word_tokenize returns list
        words_list_of_pattern = nltk.word_tokenize(pattern)
        # extend() adds  all but only elements(not list itself) of other list in first list altogether in one turn.
        words.extend(words_list_of_pattern)
        documents.append((words_list_of_pattern, intent["tag"]))
    if intent["tag"] not in classes:
        classes.append(intent["tag"])
words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
# set() removes any duplicate element.
# sorted() arrange elements in  list in  Alphabetical ascending order.
words = sorted(set(words))
classes = sorted(set(classes))
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

training_data = []
# creates a list of number of zeros equal to length of classes(no. of tags)
output_empty = [0] * len(classes)
# documents means all documents in all patterns.
for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)
    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training_data.append([bag, output_row])
random.shuffle(training_data)
training_data_array = np.array(training_data)

# first_list of array is first(dimension or column) and we will take it as train_x
train_x = list(training_data_array[:, 0])
# 2nd_list of array is 2nd (dimension or column) and we will take it as y_train
train_y = list(training_data_array[:, 1])

model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))
optimizer = tf.keras.optimizers.SGD(learning_rate=0.1)
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
epochs = 331
hist = model.fit(np.array(train_x), np.array(train_y), epochs=epochs, batch_size=5, verbose=1)
model.save('chatbot_model.h5', hist)
print("Done")
