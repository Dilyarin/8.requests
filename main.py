from pprint import pprint
import requests

#Задача1
TOKEN = "2619421814940190"

def superhero_request():
    hero_list = ['Hulk', 'Captain America', 'Thanos']
    intelligence_rating = {}
    for name in hero_list:
        url = f"https://superheroapi.com/api/2619421814940190/search/{name}"
        response = requests.get(url,timeout=5)
        intelligence_rating[name] = int(response.json()['results'][0]['powerstats']['intelligence'])
    #pprint(intelligence_rating)
    max_int = max(intelligence_rating.items(), key=lambda x: x[1])

    print(f"Самый умный: {max_int[0]}. Его интеллект равен {max_int[1]}.")

if __name__ == '__main__':
    superhero_request()

#Задача2

class YandexDisk:

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net:443'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, disk_file_path: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path: str, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    token = "..."
    ya = YandexDisk(token)
    ya.upload_file_to_disk('/test.txt', 'test.txt')


