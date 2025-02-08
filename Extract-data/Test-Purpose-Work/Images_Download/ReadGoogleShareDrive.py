import gspread
from oauth2client.service_account import ServiceAccountCredentials
# Use the credentials file you obtained from Google Cloud Platform
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/PK/Downloads/credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1jTgsmpuqeKTeaikevOlfPo6w_9M0eE7uD4zhzg56rEI/edit#gid=0').sheet1

url_link = sheet.get_values()
i = 1
for url_count, product_urls in enumerate(url_link[i:2], start=i):
    product_url = product_urls[0]
    print("Url-Length...", url_count)
    print("Product-Urls......", product_url)


    for images_name, data in enumerate(img):
        response = requests.get(data)
        if response.status_code == 200:
            image_name = str(data).replace('/', 'tick').replace('\\', 'tick').split("tick")[-1].split(".")[0]
            file_name = f"{image_name}.png"
            file_path = os.path.join(folder_path, file_name)
            try:
                os.makedirs(folder_path, exist_ok=True)  # Create directory if it doesn't exist
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print(f"Image downloaded: {file_name}")
            except OSError as e:
                print(f"Error downloading image: {e}")
        else:
            print(f"Failed to download image: {data}")