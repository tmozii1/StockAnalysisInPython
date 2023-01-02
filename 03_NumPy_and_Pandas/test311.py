import numpy as np
a = np.array([[1, 2], [3, 4]])

import pandas as pd
s = pd.Series([0.0, 3.6, 2.0, 5.8, 4.2, 8.0])

s.index = pd.Index([0.0, 1.1, 2.2, 3.3, 4.4, 5.5])
s.index.name = 'my_idx'
s.name = "my_series"

s[5.9] = 5.5

ser = pd.Series([6.7, 7.7], index=[6.0, 7.0])
s = s.append(ser)

s.describe() # 설명
s.drop(7.0) # 삭제

print(s)

import matplotlib.pyplot as plt
plt.title("ELL")
plt.plot(s, 'bs--')
plt.xticks(s.index)
plt.yticks(s.values)
plt.grid(True)
plt.show()