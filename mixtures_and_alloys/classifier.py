# C: Файл для обучения модели и предсказания типа задачи

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from joblib import dump, load
from mixtures_and_alloys.tasks import tasks
from mixtures_and_alloys.answers import labels

# C: Функция для обучения модели и записи её в файл
def train_classifier():
    sentences = tasks

    # Метки классов
    y = np.array(labels)

    # Извлечение признаков с помощью CountVectorizer
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(sentences)

    # Обучение модели LogisticRegression
    classifier = OneVsRestClassifier(LogisticRegression())
    classifier.fit(X, y)

    # Сохранение модели
    try:
        dump(classifier, 'mixtures_and_alloys/classifier_model.pkl')
        dump(vectorizer, 'mixtures_and_alloys/vectorizer.pkl')
    except:
        dump(classifier, 'classifier_model.pkl')
        dump(vectorizer, 'vectorizer.pkl')

# C: Функция для загрузки пред обученной модели
def load_classifier():
    try:
        classifier = load('mixtures_and_alloys/classifier_model.pkl')
        vectorizer = load('mixtures_and_alloys/vectorizer.pkl')
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

