import json
import pandas as pd

with open("C:/Users/lenovo/Desktop/web_page_test_result.txt", 'r', encoding='utf-8') as file:
    text = file.read()

test_dict = eval(text)

# df = pd.DataFrame(eval(text))

print(test_dict['data']['average']['firstView'])
