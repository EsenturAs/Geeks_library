import requests
from bs4 import BeautifulSoup as BS4

URL = 'https://ranobe.me'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}


def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request


def get_data(html):
    bs = BS4(html, "html.parser")

    # Сделал сам - не работало
    # items = bs.find_all('div', class_='site-content-center')
    # uploaded_list = []
    # for item in items:
    #     title = item.find('div', class_='FicTable_Title').get_text(strip=True)
    #     stat = item.find('div', class_='FicTable_Stat').get_text(strip=True)
    #     description = item.find('div', class_='FicTable_Description').get_text(strip=True)
    #     image = URL + item.find('div', class_='FicTable_Cover').find('img').get('src')


    items = bs.find_all('div', class_='FicTable')
    uploaded_list = []

    for item in items:
        # Заголовок
        title = item.find('div', class_='FicTable_Title').get_text(strip=True)
        # title = title_tag.find('a').get_text(strip=True) if title_tag else 'No title'

        # Статистика (главы и дата обновления)
        stat_tag = item.find('div', class_='FicTable_Stat')
        stat = stat_tag.get_text(strip=True) if stat_tag else 'No stats'

        # Описание
        description_tag = item.find('div', class_='FicTable_Description')
        description = description_tag.get_text(strip=True) if description_tag else 'No description'

        # Обложка
        cover_tag = item.find('div', class_='FicTable_Cover')
        image_tag = cover_tag.find('img') if cover_tag else None
        image = URL + image_tag['src'] if image_tag and 'src' in image_tag.attrs else 'No image'

        uploaded_list.append({
            'title': title,
            'stat': stat,
            'description': description,
            'image': image
        })
    return uploaded_list


def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        uploaded_list2 = []
        for page in range(1, 2):
            response = get_html('https://ranobe.me/catalog/', params={'page': page})
            uploaded_list2.extend(get_data(response.text))
        return uploaded_list2
    else:
        raise Exception('Error parsing')