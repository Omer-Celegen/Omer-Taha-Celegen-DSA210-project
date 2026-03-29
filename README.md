# Omer-Taha-Celegen-DSA210-project

Project Proposal: Impact of FED Interest Rate Decisions on Silver/USD Prices (2021-2026)
Motivation: 
The main goal of this project is to analyze the correlation between Federal Reserve (FED) interest rate announcements and the price fluctuations of silver per ounce. Since silver is a non-yielding asset, it is highly sensitive to interest rate changes. I want to investigate how consistently silver prices react to these macroeconomic shifts over the last 5 years.

Data Source & Collection: 
I will collect data from two primary sources:
+2

Silver Spot Prices: Historical daily silver prices (XAG/USD) will be extracted from the Yahoo Finance API using the yfinance library in Python.

FED Interest Rate Data: Official interest rate decision dates and rates will be collected from the Federal Reserve’s official website or the FRED (Federal Reserve Economic Data) database.

Data Characteristics: 

Time Frame: Last 5 years (approximately 2021 to 2026) to capture various economic cycles (COVID-19 recovery, high inflation period, and rate hikes).

Sample Size: Daily silver price data will provide approximately 1,250 to 1,300 data points.

Enrichment: I will enrich the silver price dataset by merging it with the FED's categorical "Rate Increase/Decrease/Stable" data.

Data Analysis & Methods: I will perform Exploratory Data Analysis (EDA) to visualize price trends around FED meeting dates. I plan to use Hypothesis Testing to see if there is a statistically significant price change following rate hikes. Finally, I will apply Machine Learning models (like Linear Regression or Random Forest) to see if interest rates can predict silver price movements.
+2
