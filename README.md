# DSA 210 Term Project: Silver Prices vs. FED Interest Rates

## Project Motivation
This project analyzes the historical relationship between Federal Reserve (FED) interest rate decisions and silver spot prices over a 5-year period (2021-2026) to understand how macroeconomic tightening and easing cycles influence precious metal markets.

## Dataset & Enrichment
- **Silver Spot Prices:** Sourced dynamically using the `yfinance` API.
- **FED Interest Rates:** Sourced directly from the Federal Reserve Bank of St. Louis (FRED) database.
- **Enrichment:** The FRED dataset was enriched by calculating daily rate differentials and creating a categorical indicator (`Rate_Category`) to track whether the FED increased, decreased, or held interest rates stable.

## Statistical Methodology & Feedback Implementation
In response to instructor feedback, this analysis has been strictly upgraded to meet rigorous statistical standards:
1. **Extended EDA:** Beyond basic time-series tracking, we added distribution visualizations (KDE charts) and an asset correlation heatmap to map dependencies clearly.
2. **Normality Verification:** We implemented the **Shapiro-Wilk test** to check the mathematical assumptions of our data. Since the daily returns heavily violated normality ($p < 0.05$), standard parametric T-tests were deemed inappropriate.
3. **Advanced Non-Parametric Testing:** To safely evaluate the hypothesis without assuming normality, a **Mann-Whitney U Test** was executed alongside a **Spearman Rank Correlation Test** to measure monotonic trends.

## How to Reproduce
1. Clone this repository.
2. Install the required dependencies: `pip install -r requirements.txt`
3. Open and view the executed cells within the `dsa210_project.ipynb` Jupyter Notebook.

## Academic Integrity & AI Disclosure
This project was completed individually as a sole author. In compliance with the course guidelines, Generative AI (Gemini) was utilized as an expert coding and statistical assistant to resolve MacOS SSL fetching issues, structure the multi-plot Seaborn visualizations, properly configure the non-parametric SciPy test syntax, and format this documentation.
