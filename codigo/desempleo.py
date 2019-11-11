import pandas as pd

df1 = pd.read_html('https://datosmacro.expansion.com/paro/espana?sector=Tasa+de+desempleo&sc=T&anio=2019')[0]
df2 = pd.read_html('https://datosmacro.expansion.com/paro/belgica?sector=Tasa+de+desempleo&sc=T&anio=2019')[0]
df3 = pd.read_html('https://datosmacro.expansion.com/paro/uk?sector=Tasa+de+desempleo&sc=T&anio=2019')[0]
df4 = pd.read_html('https://datosmacro.expansion.com/paro/grecia?sector=Tasa+de+desempleo&sc=T&anio=2019')[0]
df5 = pd.read_html('https://datosmacro.expansion.com/paro/alemania?sector=Tasa+de+desempleo&sc=T&anio=2019')[0]
df6 = pd.read_html('https://datosmacro.expansion.com/paro/portugal?sector=Tasa+de+desempleo&sc=T&anio=2019')[0]
df7 = pd.read_html('https://datosmacro.expansion.com/paro/italia?sector=Tasa+de+desempleo&sc=T&anio=2019')[0]



frames = [df1, df2, df3, df4, df5, df6, df7]
result = pd.concat(frames)

result.to_csv('desempleo.csv', index=False)

print(result)