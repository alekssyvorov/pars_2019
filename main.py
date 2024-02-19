import requests
import lxml
from bs4 import BeautifulSoup

session = requests.Session()
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

data = input("Input url categories ")
for i in range(1, 20):
    print(f"PAGE -> {i}")
    url = f"{data}p-{i}/"
    response = session.get(url, headers=header)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        all_products = soup.find('div', class_="products-layout__container products-layout--grid")
        products = all_products.find_all('div', class_="product-card")

        for j in range(len(products)):
            try:
                title_ = products[j].find("a", class_="product-card__title").text
                if " " in title_:
                    title_ = title_.replace(" ", "")
                price = products[j].find("div", class_="v-pb__cur discount").text
                with open("products.txt", "a", encoding="UTF-8") as file:
                    file.write(f"{title_}  {price}\n")
                print(title_, price)
            except:
                print(f"{title_} - знижки немає")

