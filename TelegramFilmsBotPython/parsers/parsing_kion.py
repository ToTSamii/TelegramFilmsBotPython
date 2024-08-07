import requests
from bs4 import BeautifulSoup as bs


class Kion_Parsing:

    def __init__(self, user_params, link) -> None:
        self.user_params = user_params
        self.link = link
        self.content = []
        self.count = 0

    
    def parsing(self) -> str:
        response = requests.get(self.link, headers = self.user_params)

        if response.status_code == 200:
            soup = bs(response.text, "lxml")
            a = soup.find("section", class_ = "row").find_all('a')[1:]
            
            for item in a:

                try:
                    
                    name = item.find("div", class_ = "first-line mb-md-1 d-flex flex-nowrap justify-content-between").text
                    info = item.find("div", class_ = "second-line text-nowrap d-flex align-items-center p2-regular").text.split()
                    img = item.find("img").get("src")

                    self.content.append({
                        "link" : "https://kion.ru" + item.get("href"),
                        "name" : name,
                        "img_link" : img,
                        "grade" : info[0],
                        "status" : info[1][1:]
                    })

                    self.count += 1

                except:
                    continue

            return self.content
        
        else:
            print("Ошибка! Status_code: " + response.status_code)
            return ''
        
    
    def get_count(self) -> int:
        return self.count