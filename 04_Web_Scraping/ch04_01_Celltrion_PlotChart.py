# ch04_01_Celltrion_PlotChart.py
import pandas as pd
import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from matplotlib import font_manager

# matplotlib 폰트설정
plt.rc('font', family='AppleGothic') # For MacOS
# plt.rc('font', family='NanumGothic') # For Windows
print(plt.rcParams['font.family'])



code = '353200'

# 종목명 구하기
url = 'https://finance.naver.com/item/sise.naver?code={0}'.format(code)
html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
bs = BeautifulSoup(html, 'lxml')
name = bs.find('div', 'wrap_company').h2.a.text

# 4.4.3 맨 뒤 페이지 숫자 구하기
url = 'https://finance.naver.com/item/sise_day.nhn?code={0}&page=1'.format(code)
html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
bs = BeautifulSoup(html, 'lxml')
pgrr = bs.find('td', class_='pgRR')
s = str(pgrr.a['href']).split('=')
last_page = s[-1]  
print(last_page)

# 4.4.4 전체 페이지 읽어오기
df = pd.DataFrame()
sise_url = 'https://finance.naver.com/item/sise_day.nhn?code={0}'.format(code)  
for page in range(1, int(last_page)+1):
    url = '{}&page={}'.format(sise_url, page)  
    html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
    df = pd.concat([df, pd.read_html(html, header=0)[0]])

# 차트 출력을 위해 데이터프레임 가공하기
df = df.dropna()
df = df.iloc[0:60]  # ①
df = df.sort_values(by='날짜')  # ②

# # 날짜, 종가 컬럼으로 차트 그리기
plt.title('{0} (close)'.format(name))
plt.xticks(rotation=45)  # ③
plt.plot(df['날짜'], df['종가'], 'co-')  # ④
plt.grid(color='gray', linestyle='--')
plt.show()
