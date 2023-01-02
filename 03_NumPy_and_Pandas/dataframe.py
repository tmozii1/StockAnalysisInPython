# dataframe.py
import pandas as pd
df = pd.DataFrame({'KOSPI' : [1914, 1961, 2026, 2467, 2041], 'KOSDAQ' : [542, 682, 631, 798, 675]}, index=[2014, 2015, 2016, 2017, 2018])
print(df)

df.describe()
df.info()


# series -> dataframe
kospi = pd.Series([1914, 1961, 2026, 2467, 2041], index=[2014, 2015, 2016, 2017, 2018], name="KOSPI")
kosdaq = pd.Series([542, 682, 631, 798, 675], index=[2014, 2015, 2016, 2017, 2018], name="KOSDAQ")
df2 = pd.DataFrame({kospi.name: kospi, kosdaq.name: kosdaq})


# list -> dataframe
col = ['KOSPI', 'KOSDAQ']
index = [2014, 2015, 2016, 2017, 2018]
rows = []
rows.append([1914, 542])
rows.append([1961, 682])
rows.append([2026, 631])
rows.append([2467, 798])
rows.append([2041, 675])
df3 = pd.DataFrame(rows, columns=col, index=index)


# 순회
for i in df.index:
    print(i, df['KOSPI'][i], df['KOSDAQ'][i])