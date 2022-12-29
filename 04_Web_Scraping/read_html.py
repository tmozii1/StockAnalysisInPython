import pandas as pd
list = pd.read_html('상장법인목록.xls')
list[0]

# 종목코드를 000700 0이 들어간 6자리로 변경
list[0].종목코드 = list[0].종목코드.map('{:06d}'.format)

df = pd.read_html('https://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13')[0]
df.종목코드 = df.종목코드.map('{:06d}'.format)
df = df.sort_values(by='종목코드')
