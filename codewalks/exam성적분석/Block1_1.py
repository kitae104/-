import pandas as pd
df = pd.read_csv('exam.csv')
print(df.head(3).to_html())
print(df.info())
print(df.describe().to_html())
df = df.fillna(0)
print(df.query('math > 60 and science > 60'))
print(df.groupby('class', as_index=False).mean())
df['avg'] = (df.math + df.eng + df.science) / 3
print(df.head(3).to_html())
X = df['hours']
y = df['tot']
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
fontprop = fm.FontProperties(fname='malgun.ttf')
plt.scatter(X, y,label='Label',c='b',marker='o',s=20)
plt.xlabel('공부시간', fontproperties=fontprop)
plt.ylabel('총점', fontproperties=fontprop)
plt.show()
plt.figure()
plt.bar(X, y,label='Label',color='b',width=0.8)
plt.xlabel('공부시간', fontproperties=fontprop)
plt.ylabel('총점', fontproperties=fontprop)
plt.show()
plt.figure()
plt.hist(X,label=['공부시간'], bins=10, orientation='vertical', histtype='barstacked')
plt.xlabel('공부시간', fontproperties=fontprop)
plt.show()
plt.figure()
