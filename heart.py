from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
import numpy as np
X = []
y = []
def plus_value(place, splitter):
    df = open(place, 'r').read().split('\n')
    for i in df:
        mas = i.split(splitter)
        dop = []
        for j in range(len(mas)):
            if j != 13:
                if mas[j] == '?' or mas[j] == '':
                    dop.append(0)
                else:
                    dop.append(float(mas[j]))
            else:
                if mas[j] == '':
                    y.append(0.0)
                else:
                    y.append(float(mas[j]))
        X.append(dop)
    del X[-1]
    pass
plus_value('heart/processedCleveland.data', ',')
plus_value('heart/processedHungarian.data', ',')
plus_value('heart/processedSwitzerland.data', ',')
plus_value('heart/processedVa.data', ',')
plus_value('heart/reprocessedHungarian.data', ' ')
#NeuroNetClassifier
values = []
for i in range(50):
    corrects = 0
    all = 0
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2))
    clf.fit(X_train, y_train)
    for j in range(len(X_test)):
        all += 1
        if clf.predict([X_test[j]]) == y_train[j]:
            corrects += 1
    values.append(corrects/all)
print('Вероятность правильного прогноза с RC:', np.mean(values))
age = float(input('Возраст>> '))
sex = float(input('Пол (1 - мужчина, 0 - женщина)>> '))
cp = float(input('Тип боли в груди (1-4)>> '))
trest = float(input('Кровяное давление в состоянии покоя>> '))
chol = float(input('Холесторал сыворотки в мг/дл>> '))
fbs = float(input('Уровень сахора в крови натощак>> '))
restecg = float(input('Результаты электрокардиографии в покое>> '))
thalach = float(input('Максимальная частота сердечных колебаний>> '))
exang = float(input('Стенокардия, вызванная физической нагрузкой (1 - да, 0 - нет)>> '))
oldpeak = float(input('Депрессия, вызванная физическими упражнениями, по сравнению с отдыхом>> '))
slope = float(input('Hаклон пикового сегмента ST при нагрузке>> '))
ca = float(input('Kоличество крупных сосудов (0-3), окрашенных флюороскопией>> '))
thal = float(input('3 = нормально; 6 = фиксированный дефект; 7 = обратимый дефект>> '))
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2)).fit(X, y)
print('Уровень сердечного заболевания:', int(clf.predict([[age, sex, cp, trest, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])[0]))