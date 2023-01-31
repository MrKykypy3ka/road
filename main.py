import requests
import json
from requests.structures import CaseInsensitiveDict


#resp = requests.post(url, headers=headers, data=data)
#print(resp.status_code)


def main():
    link = 'https://routing.api.2gis.com/carrouting/6.0.0/global?key=1967db2b-de7d-46b3-b63a-ab040702a18a'
    headers = json.load(open("headers.json", "r"))
    data = open("data.json", "r").read()

    question = requests.post(url=link, headers=headers, data=data).text
    result = json.loads(question)
    print(result)


if __name__ == "__main__":
        main()