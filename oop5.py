import requests
import random 

class Unsplash:
    def __init__(self):
        self.url="https://api.unsplash.com/photos/?client_id="
        self.key="99r1PHzKB2sLFmXmfXJ2vbc6ZlxlyxlAwu8LK3--HKQ"

    def __get_image_params(self):
        response=requests.get(self.url+self.key)
        if response.status_code == 200:
            return response.json()
        raise Exception("{response.status_code} warning")
        

    def processing_image(self):
        data=random.choice(self.__get_image_params())
        if data['description'] is not None:
            description=data['description']
        else:
            description=data['all_description']

        information_image = f"Фотография из Unsplash {data['updated_at']}\n\
<b>Описания:</b> {description}\n\
<b>Популярность:</b> {data['likes']}\n\
<b>link:</b> <a href='{data['urls']['small']}'>image</a>\n\n\
<b>Автор:</b> {data['user']['username']}\n\
<b>Имя:</b> {data['user']['name']}\n\
<b>Место:</b> {data['user']['location']}\n\
<b>Twitter:</b> {data['user']['twitter_username']}\n\
<b>Instagram:</b> {data['user']['instagram_username']}"
        return information_image

    def __str__(self) -> str:
        return"Привет запроси у меня фотку" 
            