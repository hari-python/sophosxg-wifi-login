import requests

# ENTER YOU CREDENTIALS HERE
username = "replace this string"
password = "replace this string"

# Login domain details
domain = "replace this string" # eg: https://example.com

# replace port number with your port number
port = 8090 # you can find it in the login url eg : https://example.com:8090/httpclient.html 




headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
login_data = {
    "mode": 191,
    "username": username,
    "password": password,
    # in between here, there was something with key value "a", I couldn't find it in html so i just ignored. But script works fine
    "producttype": 0
}

with requests.Session() as re:
    resp = re.get(
        f"{domain}:{port}/httpclient.html", headers=headers,)
    print(resp.status_code)
    resp2 = re.post(f"{domain}:{port}/login.xml",
                    headers=headers, data=login_data)
    print(resp2.status_code)
