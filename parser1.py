import requests

from bs4 import BeautifulSoup

class Parser:
    def __init__(self,url,domain):
        self.url=url
        self.domain=domain
        self.headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
            }
   
    def __get_html(self):
        response=requests.get(self.url,headers=self.headers)
        if response.status_code==200:
            return response.text
        return f"Error:{response.status_code}"
    
    def __processing(self):
        soup=BeautifulSoup(self.__get_html(),"lxml").find(
            "div",{"class":"blockquote-classic"}
        ).text

        text = ""

        for i in soup.split():
            text = text + ' ' + i.strip()
        
        return text
    
    def run_parser(self):
        sum=input("введите сумму: ")
        if int(sum)>10000000:
            return "Сумма не должна превышать 1млн"
        self.url=self.url+sum
        soup=self.__processing()
        return soup
    

pr=Parser("https://kursolog.com/kzt/kgs/","https://kursolog.com")
print(pr.run_parser())