# import requests
#
# def get_public_ip():
#     try:
#         response = requests.get('https://api.ipify.org?format=json')
#         return response.json()['ip']
#     except requests.RequestException as e:
#         print(f"Error getting public IP: {e}")
#         return None
#
# def get_proxy_ip(proxy):
#     try:
#         response = requests.get('https://api.ipify.org?format=json', proxies={"http": proxy, "https": proxy})
#         return response.json()['ip']
#     except requests.RequestException as e:
#         print(f"Error getting IP through proxy: {e}")
#         return None
#
#
# if __name__ == "__main__":
#     proxy = "https://catalog:kCVftpL8r8fsw7Wmb7@gate.smartproxy.com:7000"  # Replace with your proxy details
#
#     original_ip = get_public_ip()
#     if original_ip:
#         print(f"Original IP: {original_ip}")
#
#     proxy_ip = get_proxy_ip(proxy)
#     if proxy_ip:
#         print(f"IP through proxy: {proxy_ip}")
#
#     if original_ip and proxy_ip and original_ip != proxy_ip:
#         print("Proxy is working.")
#     else:
#         print("Proxy is not working.")


import requests


def check_proxy(proxy):
    url = 'http://httpbin.org/ip'  # A service that returns the client's IP address
    proxies = {
        'http': proxy,
        'https': proxy,
    }

    try:
        response = requests.get(url, proxies=proxies, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("Proxy is working. Your IP:", response.json()['origin'])
    except requests.exceptions.RequestException as e:
        print("Proxy is not working:", e)


if __name__ == '__main__':
    # Replace 'http://your-proxy:port' with your actual proxy
    proxy = 'https://catalog:kCVftpL8r8fsw7Wmb7@gate.smartproxy.com:7000'
    check_proxy(proxy)
