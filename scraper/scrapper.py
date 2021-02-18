import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/SAMSUNG-QN32Q50RAFXZA-32Q50-Smart-TV2019/dp/B07W5QYD2K/ref=sr_1_5?dchild=1&field" \
      "-shipping_option-bin=3242350011&pf_rd_i=16225009011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=85a9188d-dbd5-424e-9512" \
      "-339a1227d37c&pf_rd_r=V4965KX83NYVADP8GM1C&pf_rd_s=merchandised-search-5&pf_rd_t=101&qid=1588978526&rnid" \
      "=1266092011&s=electronics&sr=1-5 "

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/85.0.4183.102 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

# title = soup.find(id="productTitle").get_text()
#
# print(title.strip())
