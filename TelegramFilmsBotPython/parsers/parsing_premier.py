import requests


class Premier_Parsing:

    def __init__(self, user_params, link) -> None:
        self.user_params = user_params
        self.link = link
        self.content = []
        self.count = 0


    def parsing(self) -> str:
        response = requests.get(self.link, params = self.user_params)
        if response.status_code == 200:
            items = response.json()["result"]["items"]

            for item in items:
                try:

                    self.content.append({
                        "description" : str(item["description"]),
                        "name" : str(item["name"]),
                        "img_link" : str(item["picture"]),
                        "grade" : str(item["rating"]["kinopoisk"]),
                        "trailer_url" : str(item["trailer_url"])
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