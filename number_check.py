import requests

def number_checker(phone):
    payload = {"Phone": phone}
    headers = {
        "Accept": "application/json",
        "galaxy-ap-name": "f5778850-ab32-401e-bca1-377606919ae0",
        "galaxy-ap-password": "54e01deb091c4df2bef74481b5093453",
        "galaxy-search-type": "Person",
        "Content-Type": "application/json"
    }
    url = "https://devapi.endato.com/PersonSearch"
    response = requests.post(url, json=payload, headers=headers)
    return response.json()


