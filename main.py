#main
import record
#import moduleswitcher as ms
import pyttsx3
import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

#Importing custom modules
import variables
import variablescpp
import template
import templatecpp
import functions
import functionscpp
import string
import stringcpp
import classes as classmodule
import classescpp
import objects
import objectscpp

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))
model = load_model('food_chatbot.h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
        return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i in list_of_intents:
            if i['tag'] == tag:
                result = random.choice(i['responses'])
                break
    return result

eng = pyttsx3.init()
print("Welcome to Voice Coding!")
eng.say("Welcome to Voice Coding!")
eng.runAndWait()
eng.say("Please Choose Your Programming Language")
eng.runAndWait()
langinp=int(input("1. Python\n2. C++"))
if langinp==1:
    print("Speak something to write your code in Python")
    eng.say("Speak to write your code in Python")
    eng.runAndWait()
    check=1
    while check:
        msg = record.recorder().lower()
        ints = predict_class(msg.lower())
        res = get_response(ints, intents)
        if res == 'variables':
            check=variables.enter(msg)
        elif res == 'templates':
            check=template.enter(msg)
        elif res == 'functions':
            check=functions.enter(msg)
        elif res == 'strings':
            check=functions.enter(msg)
        elif res == 'classes':
            check = classmodule.enter(msg)
        elif res == 'objects':
            check = objects.enter(msg)
        else:
            print("Couldn't determine user intent. Please try again.")
            eng.say("Couldn't determine user intent. Please try again.")
            eng.runAndWait()
            continue
elif langinp==2:
    print("Speak something to write your code in C++")
    eng.say("Speak to write your code in C plus plus.")
    eng.runAndWait()
    check=1
    while check:
        msg = record.recorder()
        ints = predict_class(msg.lower())
        res = get_response(ints, intents)
        if res == 'variables':
            check=variablescpp.enter(msg)
        elif res == 'templates':
            check=templatecpp.enter(msg)
        elif res == 'functions':
            check=functionscpp.enter(msg)
        elif res == 'strings':
            check=stringcpp.enter(msg)
        elif res == 'classes':
            check = classescpp.enter(msg)
        elif res == 'objects':
            check = objectscpp.enter(msg)
        else:
            print("Couldn't determine user intent. Please try again.")
            continue
else:
    print("Please select a valid language.")

