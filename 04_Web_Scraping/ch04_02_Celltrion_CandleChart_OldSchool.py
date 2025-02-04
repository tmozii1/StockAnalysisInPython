import pandas as pd
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from matplotlib import dates as mdates    
#from mplfinance import candlestick_ohlc
from mplfinance.original_flavor import candlestick_ohlc
from datetime import datetime

code = '353200'

# 종목명 구하기
url = 'https://finance.naver.com/item/sise.naver?code={0}'.format(code)
html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
bs = BeautifulSoup(html, 'lxml')
name = bs.find('div', 'wrap_company').h2.a.text

# matplotlib 폰트설정
plt.rc('font', family='AppleGothic') # For MacOS
# plt.rc('font', family='NanumGothic') # For Windows

url = 'https://finance.naver.com/item/sise_day.nhn?code={0}&page=1'.format(code)
html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
bs = BeautifulSoup(html, 'lxml') 
pgrr = bs.find('td', class_='pgRR')
s = str(pgrr.a['href']).split('=')
last_page = s[-1]  

last_page = '3'

df = pd.DataFrame()
sise_url = 'https://finance.naver.com/item/sise_day.nhn?code={0}'.format(code) 
for page in range(1, int(last_page)+1): 
    page_url = '{}&page={}'.format(sise_url, page)  
    html = requests.get(page_url, headers={'User-agent': 'Mozilla/5.0'}).text
    df = pd.concat([df, pd.read_html(html, header=0)[0]])

df = df.dropna()
df = df.iloc[0:10]
df = df.sort_values(by='날짜')
for idx in range(0, len(df)):
    dt = datetime.strptime(df['날짜'].values[idx], '%Y.%m.%d').date() 
    df['날짜'].values[idx] = mdates.date2num(dt)
ohlc = df[['날짜','시가','고가','저가','종가']]


print(ohlc)

plt.figure(figsize=(9, 6))
ax = plt.subplot(1, 1, 1)    
plt.title('{0} (mpl_finance candle stick)'.format(name))
candlestick_ohlc(ax, ohlc.values, width=0.7, colorup='red', colordown='blue') 
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)
plt.grid(color='gray', linestyle='--')
plt.show()
