import requests
from bs4 import BeautifulSoup
from lxml import etree
def HtmlCsv():
    with open(r'C:/Users/Administrator/Desktop/index.html','r',encoding='gbk') as f:
        html = f.read()
    html = etree.HTML(html)
    title = html.xpath(r'/html/body/div/table/tbody/tr/td/div[1]/span/font/text()')[0]
    devlop = html.xpath(r'/html/body/div/table/tbody/tr/td/div[2]/table/tbody/tr[2]/td[2]/div/text()')[0].replace('/','-').strip()
    name = html.xpath(r'/html/body/div/table/tbody/tr/td/div[2]/table/tbody/tr[2]/td[4]/div/text()')[0].strip()
    id = html.xpath(r'/html/body/div/table/tbody/tr/td/div[2]/table/tbody/tr[2]/td[6]/div/text()')[0].strip()
    print(title,devlop,name,id)
HtmlCsv()