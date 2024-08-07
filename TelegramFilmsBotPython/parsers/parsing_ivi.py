import requests
from bs4 import BeautifulSoup as bs


class Ivi_Parsing:

    def __init__(self, user_params, link) -> None:
        self.user_params = user_params
        self.link = link
        self.content = []
        self.count = 0


    def parsing(self) -> str:
        response = requests.get(self.link, params = self.user_params)

        if self.link == "https://www.ivi.ru/collections/best-movies":
            cl = "pageSection pageSection_virtual collections__pageSection collections__pageSection_virtual"
        else:
            cl = "pageSection pageSection_virtual genre__pageSection genre__pageSection_virtual"

        if response.status_code == 200:
            soup = bs(response.text, "lxml")
            a = soup.find("section", class_ = cl).find_all('a')
            
            for item in a:

                try:
                    name = item.find("div", class_ = "nbl-slimPosterBlock__title").text
                    grade = item.find("div", class_ = "nbl-poster__propertiesRow").text
                    info = item.find("div", class_ = "nbl-poster__propertiesInfo").find_all("div", class_ = "nbl-poster__propertiesRow")

                    self.content.append({
                        "link" : "https://www.ivi.ru" + item.get("href"),
                        "name" : name,
                        "time" : info[1].text,
                        "grade" : grade,
                        "date-country" : info[0].text
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