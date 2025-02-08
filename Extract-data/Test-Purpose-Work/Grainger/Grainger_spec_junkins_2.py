from bs4 import BeautifulSoup
import json
import concurrent.futures
import pandas as pd
import requests

final_df = []



file_path = r"P:\Web-scrapings\Test-Purpose-Work\Grainger\Product-url.csv"
urls = pd.read_csv(file_path)['URL']
print(urls)



headers = {
	'authority': 'www.grainger.com',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
	'accept-language': 'en-US,en;q=0.8',
	'referer': 'https://www.grainger.com/product/102EW3',
	'sec-ch-ua': '"Not A(Brand";v="99", "Brave";v="121", "Chromium";v="121"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"Windows"',
	'sec-fetch-dest': 'document',
	'sec-fetch-mode': 'navigate',
	'sec-fetch-site': 'same-origin',
	'sec-gpc': '1',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}


def get_results(url):
	try:
		print("main_url-----------------------", url)
		response = requests.get(url, headers=headers)
		print("---------- : ", response)
		soup = BeautifulSoup(response.content, 'html.parser')
		title = soup.h1.text
		print(title)
		item_id = "rp_" + soup.find(class_="iYMkrn").find("dd").text
		manufacture_id = "rp_" + soup.select("dd.rOM8HV.hRRBwT")[1].text.strip()
		print(manufacture_id)
		price = soup.select_one("div.XCqnjh .HANkB").text.strip()
		print(price)
		data = [url, title, item_id, manufacture_id, price]

		final_df.append(data)
		script_tags = soup.find_all('script', {'type': 'application/ld+json'})
		for script_tag in script_tags:
			json_data = json.loads(script_tag.string)["isSimilarTo"]
			for i in json_data:
				required_url = i["url"]
				print("required_url ---------- ", required_url)
				response = requests.get(required_url, headers=headers)
				soup = BeautifulSoup(response.content, 'html.parser')
				title = soup.h1.text
				print(title)
				item_id = "rp_" + soup.select("div[data-testid='pdp-header'] dl .vDgTDH dd")[0].text.strip()
				manufacture_id = "rp_" + soup.select("div[data-testid='pdp-header'] dl .vDgTDH dd")[1].text.strip()
				print('manufacture_id -----', manufacture_id)
				price = soup.select_one("div.XCqnjh .HANkB").text.strip()
				print(price)
				data = [url, title, item_id, manufacture_id, price]
				final_df.append(data)
	except Exception as e:
		print(f"Error processing {url}: {e}")


# get_results("https://www.grainger.com/product/JUSTRITE-1-55-Gallon-Drum-Gallon-Drum-786V89")



with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
	# Submit each download task to the thread pool
	# start with 55000
	start_url = 88000
	futures = [executor.submit(get_results, url) for index, url in enumerate(urls[start_url:], start=start_url)]
	# Wait for all tasks to complete and retrieve the results
	results = [future.result() for future in concurrent.futures.as_completed(futures)]
	# Print the contents of each file
	for result in results:
		print(final_df)

	df = pd.DataFrame.from_records(final_df)
	df.to_csv('Grainger_116k2.csv', mode='a', header=not pd.io.common.file_exists('Grainger_116k2.csv'), index=False)
	print('save data into csv')
