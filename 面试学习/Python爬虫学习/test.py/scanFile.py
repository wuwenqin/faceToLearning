import requests
from bs4 import BeautifulSoup
from lxml import etree
import os
from fake_useragent import UserAgent
import random
import xlwt

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
         "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
         "Accept-Encoding":"gzip, deflate",
         "Accept-Language":"zh,en;q=0.9,zh-CN;q=0.8",
         "Connection":"keep-alive",
         }

post_headers={
    'Host':'www.qhdsdyyy.com',
    # 'Referer':'http://www.qhdsdyyy.com/ProductInfoCategory?categoryId=497585&PageInfoId=0',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'ASP.NET_SessionId=moqjy30c2twqhyh2u4y10y1d; __RequestVerificationToken=bk4zf55YKJ-cOO_eL0bsUcR_SZzfOc9P0kxVMpe82Y_Z5KpAqMMkKAl7Di8aW7mJdxj_2b8_9DYiRq-JfaDmIsrKBdqioGL-tcL8I0i9S2U1; UM_distinctid=17d3726dedc5a3-0ad01e5b13757-57b1a33-144000-17d3726deddb54; acw_tc=717165b616373481036901114eca82639e444c24b5c9a44453262849d1; CNZZDATA1278919793=459396911-1637299817-https%253A%252F%252Fwww.baidu.com%252F%7C1637348104; SERVERID=7c96c87e4cb8634682f7ea3100d5bf87|1637348104|1637348104' # 需要登陆后捕获cookie并调用
}

data_search={
"dataType": "product",
"key":"",
"pageIndex": "1",
"pageSize": "6",
"selectCategory": "497585",
"selectId":"",
"dateFormater": "yyyy-MM-dd",
"orderByField": "createtime",
"orderByType": "desc",
"templateId": "0",
"postData": "[]",
"es": "false",
"setTop": "true",
"__RequestVerificationToken": "Rh3N5k3AvcDEt-c20sowXjDwY8jY4GcIkJel395TOAl2_PU8kjIJe1W3p2MBvMp-8CCx9ZZ0z8ZBtJkFclJznfv0X_Sf7bQU3v1XP_lTmHM1",
}

# 获取各个科室的链接地址
def fir_pageURL(html):
    base_url = "http://www.qhdsdyyy.com"
    response = requests.get(html, headers=headers).text
    tree = etree.HTML(response)  # 树结构下的html
    hospitalDepartments = tree.xpath("//ul[@class='w-category-list']/li")
    first_pageUrl = []  # 各个科室的链接地址
    for url in hospitalDepartments:  # 循环提取每一个科室的链接地址，放入first_pageUrl数组中
        urlAttr = url.xpath("@data-url")[0]
        # print(urlAttr) # 显示提取的地址
        true_url = base_url + urlAttr  # 拼接之后才是真实地址
        first_pageUrl.append(true_url)  # 将科室的链接地址放入数组中
    return first_pageUrl


def get_page(url):
    try:
        response=requests.post(url=url,headers=post_headers,data=data_search).text
        if(requests.status_codes):
            print(response)
    except requests.ConnectionError as e:
        print('Error',e.args)


if __name__ == '__main__':
    html="http://www.qhdsdyyy.com/zjtd"
    # fir_pageURL=fir_pageURL(html)
    # for e in fir_pageURL:
    #     print(e)
    url="http://www.qhdsdyyy.com/Designer/Common/GetData"
    # post_data=""
    get_page(url)
