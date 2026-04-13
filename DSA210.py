#Omer Taha Celegen 34321


import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

#AI helped to import ssl library to fix SSL issues on MacOS when fetching data from FRED
import ssl





# Mac SSL Fix & Visual Setup 
# #AI helped in here to fix SSL issues on MacOS when fetching data from FRED
ssl._create_default_https_context = ssl._create_unverified_context
sns.set_theme(style="whitegrid")

# 1. Data Collection
start, end = "2021-01-01", "2026-01-01"

# Acquiring the Silver prices from yahoo's finance library    
# AI helped to change "XAGUSD=X" to SI=F in order to have more stable and accurete data for silver prices.
silver = yf.download("SI=F", start=start, end=end, progress=False)['Close']
silver = pd.DataFrame(silver).rename(columns={silver.columns[0]: 'Silver_Price'})

# Fetch FED Rates directly from FRED with pandas
fed = pd.read_csv("https://fred.stlouisfed.org/graph/fredgraph.csv?id=FEDFUNDS", index_col=0, parse_dates=True)
fed.columns = ['Interest_Rate']

# 2. Merging & Enrichment the datasets
fed = fed.loc[start:end]
fed['Rate_Category'] = fed['Interest_Rate'].diff().apply(lambda x: 'Increase' if x > 0 else ('Decrease' if x < 0 else 'Stable'))
data = silver.join(fed, how='left').ffill().dropna()

# 3. Exploratory Data Analysis (EDA) with matplotlib and seaborn
fig, ax1 = plt.subplots(figsize=(12, 6))
ax1.plot(data.index, data['Silver_Price'], color='blue', label='Silver Price')
ax1.set_ylabel('Silver Price (USD)', color='blue', fontweight='bold')

ax2 = ax1.twinx()
ax2.step(data.index, data['Interest_Rate'], color='red', alpha=0.5, label='FED Rate')
ax2.set_ylabel('FED Interest Rate (%)', color='red', fontweight='bold')

plt.title('Silver Price vs FED Interest Rate (2021-2026)', fontweight='bold')
plt.show()

# 4. Hypothesis Testing
#AI helped me to skip the first row with ".dropna()" code and "pct.change()"" to calculate silver prices quickly and avoid from unnecessary long complex codes.
data['Returns'] = data['Silver_Price'].pct_change()
inc = data[data['Rate_Category'] == 'Increase']['Returns'].dropna()
others = data[data['Rate_Category'] != 'Increase']['Returns'].dropna()

t_stat, p_val = stats.ttest_ind(inc, others, equal_var=False)

# Final Output for GitHub Documentation
print(f"T-Statistic: {t_stat:.4f} | P-Value: {p_val:.4f}")
print(f"Result: {'Significant' if p_val < 0.05 else 'Not Significant'}")