# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

#!pip install pmdarima
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from datetime import datetime
from matplotlib import pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.graphics.tsaplots import plot_acf

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv('/kaggle/input/complete.csv')
# Any results you write to the current directory are saved as output.

comp = df[df['name']== "ABB"]
#comp

comp['date'] = comp['date'].apply(lambda x: pd.to_datetime(str(x), format='%Y%m%d'))
comp

df = comp[['date','close']]
df

df.plot(x='date', y='close')
plt.show()

window_size = 20
df['sma20'] = df.iloc[:,1].rolling(window=window_size).mean()

window_size = 50
df['sma50'] = df.iloc[:,1].rolling(window=window_size).mean()

window_size = 150
df['sma150'] = df.iloc[:,1].rolling(window=window_size).mean()

window_size = 200
df['sma200'] = df.iloc[:,1].rolling(window=window_size).mean()

df.head(window_size)

plt.figure(figsize=[15,10])
plt.grid(True)
plt.plot(df['close'],label='data')  #very noisy
plt.plot(df['sma20'],label='SMA 20 days')
#plt.plot(df['sma50'],label='SMA 50 days')
plt.plot(df['sma150'],label='SMA 150 days')
#plt.plot(df['sma200'],label='SMA 200 days')
plt.legend(loc=2)
plt.show()

plot_acf(df['close'])
plt.show()

plot_pacf(df['close'])
plt.show()


#testing 
data = df['close']
plt.plot(data, label='actual data')
plt.show()
logdata = np.log(data)
plt.plot(logdata, label='log data')
plt.show()

