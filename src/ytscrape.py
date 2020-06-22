from bs4 import BeautifulSoup
from typing import List

import requests
import pprint
import re


class YTScrape:
    _url: str

    def __init__(self, keyword: str):
        key = keyword.strip().replace(' ', '+')
        self._url = 'https://www.youtube.com/results?search_query=' + key

    def scrape(self) -> List:
        result = []

        soup = BeautifulSoup(requests.get(self._url).text, 'html.parser')
        data = soup.find_all(attrs={'class': 'yt-uix-tile-link'})

        if not data:
            return []

        for i in range(len(data)):
            href = data[i]['href']
            title = data[i]['title']
            if 'channel' not in href and '&list=' not in href:
                link = 'https://www.youtube.com' + href

                duration_raw = data[i].find_next_sibling().text

                duration1 = re.findall('-(.*?)\.', duration_raw)
                duration2 = re.findall('(.*?)\.', duration_raw)

                if duration1 and not duration2:
                    duration = duration1[0].strip()
                elif not duration1 and duration2:
                    duration = duration2[0].strip()
                else:
                    duration = duration1[0].strip()

                result.append([title, link, duration.split(' ')[-1]])

        return result

if __name__ == '__main__':
    test = YTScrape(input('Enter a search keyword: '))
    result = test.scrape()

    pprint.pprint(test.scrape())
