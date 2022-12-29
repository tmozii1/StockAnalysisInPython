from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt
yf.pdr_override()

date = '2018-05-04'

codes = [
    {'code':'AAPL', 'name':"Apple", 'color' : 'g'},
    {'code':'005930.KS', 'name':"Samsung", 'color' : 'b'},
    {'code':'META', 'name':"META", 'color' : 's--'},
    {'code':'MSFT', 'name':"Microsoft", 'color' : 'r--'},
    //{'code':'TSLA', 'name':"TESLA", 'color' : 'y'}
]

# 삼성전자 데이터 가져오기 
#sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
#sec = pdr.get_data_yahoo('AAPL', start=date)

for c in codes:
    data = pdr.get_data_yahoo(c['code'], start=date)
    dpc = (data['Close'] - data['Close'].shift(1)) / data['Close'].shift(1) * 100
    dpc.iloc[0] = 0
    dpc_cp = ((100 + dpc) / 100).cumprod() * 100 - 100
    plt.plot(data.index, dpc_cp, c['color'], label=c['name'])
    

# sec = pdr.get_data_yahoo(codes[0]['code'], start=date)

# # 등락율로 변경
# sec_dpc = (sec['Close']-sec['Close'].shift(1)) / sec['Close'].shift(1) * 100
# sec_dpc.iloc[0] = 0 # 일간 변동률의 첫 번째 값인 NaN을 0으로 변경한다.
# sec_dpc_cp = ((100+sec_dpc)/100).cumprod()*100-100 # 일간 변동률 누적곱 계산

# # 마이크로소프트 데이터 가져오기
# msft = pdr.get_data_yahoo(codes[1]['code'], start=date)
# msft_dpc = (msft['Close'] / msft['Close'].shift(1) -1) * 100
# msft_dpc.iloc[0] = 0
# msft_dpc_cp = ((100+msft_dpc)/100).cumprod()*100-100
 
# plt.plot(sec.index, sec_dpc_cp, 'b', label=codes[0]['name'])
# plt.plot(msft.index, msft_dpc_cp, 'r--', label=codes[1]['name'])
plt.ylabel('Change %') 
plt.grid(True)
plt.legend(loc='best')
plt.show()
