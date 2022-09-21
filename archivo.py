from sklearn import tree

clf = tree.DecisionTreeClassifier()

x = [[190,95,44],[180,85,42],[160,60,37],[154,54,38],[165,66,40],[181,81,44],
[164,86,38],[162,60,36],[177,78,41],[175,76,40],[182,84,43]]

y = ['hombre', 'hombre', 'mujer', 'mujer', 'hombre', 'hombre', 'mujer', 'mujer', 'mujer', 'hombre', 'hombre']

clf = clf.fit(x ,y)

dato = [180,82,42]

pred = clf.predict([dato])
print(pred)

if pred == 'hombre':
    print("probablemente es un hombre")
else:
    print("Creo que es una mujer")