import pandas as pd
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from matplotlib import dates as mdates    
#from mplfinance import candlestick_ohlc
from mplfinance.original_flavor import candlestick_ohlc
from datetime import datetime
import mplfinance as mpf

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
last_page = '20'

df = pd.DataFrame()
sise_url = 'https://finance.naver.com/item/sise_day.nhn?code={0}'.format(code) 
for page in range(1, int(last_page)+1): 
    page_url = '{}&page={}'.format(sise_url, page)  
    html = requests.get(page_url, headers={'User-agent': 'Mozilla/5.0'}).text
    df = pd.concat([df, pd.read_html(html, header=0)[0]])

df = df.dropna()
# df = df.iloc[0:30]
df = df.rename(columns={'날짜':'Date', '시가':'Open', '고가':'High', '저가':'Low', '종가':'Close', '거래량':'Volume'})
df = df.sort_values(by='Date')
df.index = pd.to_datetime(df.Date)
df = df[['Open', 'High', 'Low', 'Close', 'Volume']]


# mpf.plot(df, title='Celltrion candle chart', type='candle')

# mpf.plot(df, title='Celltrion ohlc chart', type='ohlc')

kwargs = dict(title='Celltrion customized chart', type='candle',
    mav=(5, 20, 60), volume=True, ylabel='ohlc candles')
mc = mpf.make_marketcolors(up='r', down='b', inherit=True)
s  = mpf.make_mpf_style(marketcolors=mc)
mpf.plot(df, **kwargs, style=s)

