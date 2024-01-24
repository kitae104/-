import pandas as pd
df = pd.read_csv('exam.csv', header=0)
print(df.head(3).to_html())
X = df['hours']
y = df['tot']
import statsmodels.api as sm
model = sm.OLS(X, y)
res = model.fit()
print(res.summary())
