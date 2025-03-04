from typing import final

import requests
from bs4 import BeautifulSoup


class PriceService:
    def __init__(self):
        pass

    def get_price_table(self):
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
            url = f"https://crypto.com/price"
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                tr_list = soup.find("div", class_="css-bl4fde").find("table").find("tbody").find_all("tr")
                return tr_list
            else:
                return None
        except Exception as e:
            print(e)

    def get_price(self, external_price_table, label):

        try:
            for tr in external_price_table:
                if label == tr.find("td", class_="css-1sem0fc").find("a", class_="chakra-link").find("div", class_="css-uooi3e").find("div", class_="css-87yt5a").find("p").text:
                    price_block = tr.find("td", class_="css-1m7ejhk")
                    usd_price = price_block.find_all("p", class_="chakra-text")[0].text.replace('$', '').replace(',', '')
                    change_24_h = price_block.find_all("p", class_="chakra-text")[-1].text
                    return usd_price, change_24_h
        except Exception as e:
            print(f"Get prices error {e}")

        return "0"