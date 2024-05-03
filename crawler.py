import requests
from lxml import html

class StocksItem:
    def __init__(self):
        self.symbol = None
        self.ltp = None
        self.open = None
        self.low = None
        self.previous_close = None

def parse_data(response):
    result_data = []

    tree = html.fromstring(response.content)
    rows = tree.xpath('//*[@id="headFixed"]/tbody/tr')

    for row in rows:
        data = [item.strip().replace('"', "").replace(",", "") for item in row.xpath('td//text()') if item.strip()]
        symbol = row.xpath('td/a/text()')[0]

        item = StocksItem()
        item.symbol = symbol
        item.ltp = data[1]
        item.open = data[-5]
        item.low = data[-3]
        item.previous_close = data[-1]

        result_data.append(item)

    return result_data

def main():
    url = "https://www.sharesansar.com/live-trading"
    response = requests.get(url)
    if response.status_code == 200:
        result_data = parse_data(response)
        for item in result_data:
            print(item.__dict__)

def crawl():
    url = "https://www.sharesansar.com/live-trading"
    response = requests.get(url)
    if response.status_code == 200:
        result_data = parse_data(response)
        return result_data
    else:
        return False

if __name__ == "__main__":
    main()
