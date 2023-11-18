# C: Файл для обучения модели и предсказания типа задачи

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from joblib import dump, load
from collaboration.tasks import tasks
from collaboration.answers import labels

# C: Функция для обучения модели и записи её в файл
def train_classifier():
    open("classifier_model.pkl", "w")
    open("vectorizer.pkl", "w")
    sentences = tasks

    # Метки классов
    y = np.array(labels)

    # Извлечение признаков с помощью CountVectorizer
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(sentences)
    print(1)

    # Обучение модели LogisticRegression
    classifier = OneVsRestClassifier(LogisticRegression())
    print(2)
    classifier.fit(X, y)
    print(3)

    # Сохранение модели
    try:
        dump('collaboration/classifier_model.pkl')
        dump('collaboration/vectorizer.pkl')
    except:
        dump(classifier, 'classifier_model.pkl')
        dump(vectorizer, 'vectorizer.pkl')

# C: Функция для загрузки пред обученной модели
def load_classifier():
    try:
        classifier = load('collaboration/classifier_model.pkl')
        vectorizer = load('collaboration/vectorizer.pkl')
    except:
        classifier = load('classifier_model.pkl')
        vectorizer = load('vectorizer.pkl')

    return classifier, vectorizer

# C: Функция для предсказания типа задачи (метки)
def get_answer(task):
    # C: Загрузка модели
    classifier, vectorizer = load_classifier()

    # C: Очистка задачи от лишних символов
    task = ''.join(task.split('-'))

    # C:  Классификация задачи путем предсказания метки
    new_sentence = [task]
    new_X = vectorizer.transform(new_sentence)
    prediction = classifier.predict(new_X)[0]
    return prediction

