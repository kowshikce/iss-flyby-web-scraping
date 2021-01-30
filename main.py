import requests
from collections import OrderedDict
from bs4 import BeautifulSoup
import json

if __name__ == '__main__':
    URL = 'https://spotthestation.nasa.gov/sightings/view.cfm?country=Bangladesh&region=None&city=Dhaka'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find('table', class_='table')

    # for iss in results:
    #     for data in iss.find_all('tr'):
    #         for text in data.find_all('td'):
    #             print(text.get_text())
    #

    # modified_data = [[y for y in x.children] for x in results]
    # print(type(modified_data[0]))
    # data = []
    # for row in results:
    #     cols = row.find_all('td')
    #     cols = [ele.text.strip() for ele in cols]
    #     data.append([ele for ele in cols if ele])
    #
    # print(data)

    data = []
    keys = [item.text.strip() for item in results.select('th') if item.text.strip().lower() != 'share event']
    for index in list(range(int(len(results.find_all('tr')) - 1))):
        d = OrderedDict()
        current_index = index + 1
        current_td = results.find_all('tr')[current_index].find_all('td')
        values = [(item.text.strip()) for item in current_td if item.text.strip() != '']
        for th, td in zip(keys, values):
            d[th] = td
        data.append(d)

    print(json.dumps(data))

    # print([item.text.strip() for item in results.select('th') if item.text.strip().lower() != 'share event'])
    # print([(item.text.strip()) for item in results.select('td') if item.text.strip() != ''])
    #
    # print(len(results.find_all('tr'))-1)
    #
    # # for data in results.find_all('tr')[1].children:
    # #     print(data)
    #
    # print(results.find_all('tr')[1].find_all('td'))
