import pandas as pd
df = pd.read_csv('exam.csv')
print(df.head(3).to_html())
X = df[['hours']]
y = df['tot']
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
fontprop = fm.FontProperties(fname='malgun.ttf')
plt.scatter(X, y,label='Label',c='b',marker='o',s=20)
plt.xlabel('공부시간', fontproperties=fontprop)
plt.ylabel('총점', fontproperties=fontprop)
plt.show()
plt.figure()
import sklearn
from sklearn import *
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2, shuffle=True, random_state=0, stratify=None)
model = sklearn.linear_model.LinearRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
y_pred = model.predict(X_test)
print(sklearn.metrics.mean_squared_error(y_test, y_pred))
y_pred = model.predict(X)
plt.scatter(X, y,label='Label',c='b',marker='o',s=20)
plt.plot(X, y_pred,label='label', c='y', linestyle='solid', marker='.', markersize=10)
plt.xlabel('공부시간', fontproperties=fontprop)
plt.ylabel('총점', fontproperties=fontprop)
plt.show()
plt.figure()
def PolynomialRegression(degree=2) :
  return sklearn.pipeline.make_pipeline(
    sklearn.preprocessing.PolynomialFeatures(degree=degree,include_bias=False),
    sklearn.linear_model.LinearRegression())
model = PolynomialRegression(degree=3)
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
y_pred = model.predict(X)
plt.scatter(X, y,label='Label',c='b',marker='o',s=20)
plt.plot(X, y_pred,label='label', c='r', linestyle='solid', marker='.', markersize=10)
plt.xlabel('공부시간', fontproperties=fontprop)
plt.ylabel('총점', fontproperties=fontprop)
plt.show()
plt.figure()
