import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opts = Options()
opts.add_argument("--headless")
opts.add_argument("--no-sandbox")
browser = webdriver.Chrome()
browser.maximize_window()




def send_email(msg):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = ["nkmishra@nextgenesolutions.com", "nirbhay@raptorsupplies.com", "tajender@raptorsupplies.com"]
    smtp_username = "raptorsupplyuk@gmail.com"
    smtp_password = "unwkbryielvgwiuk"
    message = MIMEMultipart()
    message["From"] = smtp_username
    message["To"] = ','.join(sender_email)
    message["Subject"] = "Script Execution Completed"
    body = msg
    message.attach(MIMEText(body, "plain"))
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, sender_email, message.as_string())
    print("Email sent successfully")


send_email("Your web scraping script has been started")


mylst = [

    'https://www.bahco.com/int_en/special-grips-for-sheet-metals-with-nickel-finish-pb_2967_.html',
]

for url in mylst:
    browser.get(url)
    time.sleep(1)
    print(url)
    title = browser.find_element(By.CLASS_NAME, "page-title").text.strip()
    print(title)


send_email("Your web scraping script has completed ")


