# C: Файл для обучения модели и предсказания типа задачи
import copy

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from joblib import dump, load
from mixtures_and_alloys.tasks import tasks
tasks1 = copy.copy(tasks)
tasks = []
from collaboration.tasks import tasks
tasks2 = copy.copy(tasks)
from mixtures_and_alloys.tasktype import type_labels
l1 = copy.copy(type_labels)
type_labels = []
from collaboration.tasktype import type_labels
l2 = copy.copy(type_labels)
import mixtures_and_alloys.mathematics
import collaboration.mathematics

# C: Функция для обучения модели и записи её в файл
def train_classifier():
    sentences = tasks1 + tasks2

    # Метки классов
    y = np.array(l1 + l2)

    # Извлечение признаков с помощью CountVectorizer
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(sentences)

    # Обучение модели LogisticRegression
    classifier = OneVsRestClassifier(LogisticRegression())
    classifier.fit(X, y)

    # Сохранение модели
    dump(classifier, 'classifier_model.pkl')
    dump(vectorizer, 'vectorizer.pkl')

# C: Функция для загрузки пред обученной модели
def load_classifier():
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


def calculate(task):
    print(get_answer(task))
    if get_answer(task) == 0:
        return mixtures_and_alloys.mathematics.calculate(task)
    elif get_answer(task) == 1:
        return collaboration.mathematics.calculate(task)

