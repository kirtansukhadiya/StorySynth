import os #To get enviroment elements
import requests

# Proxy configuration with login and password
proxy_host = 'gw.dataimpulse.com'
proxy_port = 823
proxy_login = os.getenv("PROXY_LOGIN") #Retriving Enviroment element
proxy_password = os.getenv("PROXY_PASSWORD") #Retriving Enviroment element
proxy = f'http://{proxy_login}:{proxy_password}@{proxy_host}:{proxy_port}'

proxies = {
    'http': proxy,
    'https': proxy
}

url = "https://chatgpt.com"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
cookies = {'your_cookie_key': 'your_cookie_value'}
response = requests.get(url, headers=headers, cookies=cookies)

