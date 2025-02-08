from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()

url = "http://www.sunsirs.com/futures-price-2023-0927-daily.html"

# Open the URL
driver.get(url)

# Find the table element by its XPath
table = driver.find_element(By.XPATH, "//table[@class='xnn-tablea no_select']")

# Get the table HTML
table_html = table.get_attribute('outerHTML')

# Read HTML table
dfs = pd.read_html(table_html)

# If there are multiple tables on the page, choose the relevant one by index
df = dfs[0]

print(df)
df.to_excel('RowData.xlsx', index=False)
print('save data into dataframe')

total_rows = len(df)
print("Total number of rows (daily data points):", total_rows)

df.columns = df.iloc[0]

df = df.iloc[1:]

df.index.name = None
df.reset_index(drop=True, inplace=True)

max_closing_price = df['09-28'].max()
commodity_highest_price = df.loc[df['09-28'].idxmax()]['Commodity']
print(f"Commodity with the highest daily closing price: {commodity_highest_price} - Price: {max_closing_price}")

df_sorted = df.sort_values('09-27')

previous_day_lowest_price = df_sorted.loc[df_sorted['09-27'].idxmin()]['09-27']
commodity_lowest_price = df_sorted.loc[df_sorted['09-27'].idxmin()]['Commodity']
print(f"Commodity with the lowest daily closing price for the previous day: {commodity_lowest_price} - Price: {previous_day_lowest_price}")

driver.quit()

