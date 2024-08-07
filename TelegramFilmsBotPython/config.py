import fake_useragent

TOKEN = ""

user = {"user-agent" : fake_useragent.UserAgent().random}

kion_links = {
    "popular_now" : "https://kion.ru/video/filter/mainNowPopularMixable?apiProvider=mgw",
    "new" : "https://kion.ru/video/filter/mainNew?apiProvider=mgw",
    "fantastic" : "https://kion.ru/video/filter/glo_shelf_blender_1371",
    "comedy" : "https://kion.ru/video/filter/glo_shelf_blender_1415",
    "action" : "https://kion.ru/video/filter/glo_shelf_blender_1453"
}


ivi_links = {
    "best" : "https://www.ivi.ru/collections/best-movies",
    "comedy" : "https://www.ivi.ru/movies/comedy",
    "fantastic" : "https://www.ivi.ru/movies/fantastika",
    "action" : "https://www.ivi.ru/movies/boeviki",
    "adventures" : "https://www.ivi.ru/movies/adventures"
}


premier_links = {
    "comedy" : "https://premier.one/catalog/v1.1/tv?system=hwi_vod_id&types=&genres=&countries=&years=&plots=&foreign=false&orderBy=id&typeFeed=cardgroup&cardgroup=120&picture_type=card_group&page=1&per_page=32&device=web&platform=browser",
    "drama" : "https://premier.one/catalog/v1.1/tv?system=hwi_vod_id&types=&genres=&countries=&years=&plots=&foreign=false&orderBy=id&typeFeed=cardgroup&cardgroup=119&picture_type=card_group&page=3&per_page=32&device=web&platform=browser",
    "fantastic" : "https://premier.one/catalog/v1.1/tv?system=hwi_vod_id&types=&genres=&countries=&years=&plots=&foreign=false&orderBy=id&typeFeed=cardgroup&cardgroup=125&picture_type=card_group&page=3&per_page=32&device=web&platform=browser",
    "adventures" : "https://premier.one/catalog/v1.1/tv?system=hwi_vod_id&types=&genres=&countries=&years=&plots=&foreign=false&orderBy=id&typeFeed=cardgroup&cardgroup=344&picture_type=card_group&page=3&per_page=32&device=web&platform=browser",
    "detektiv" : "https://premier.one/catalog/v1.1/tv?system=hwi_vod_id&types=&genres=&countries=&years=&plots=&foreign=false&orderBy=id&typeFeed=cardgroup&cardgroup=144&picture_type=card_group&page=3&per_page=32&device=web&platform=browser"
}