import re
import pandas as pd
import requests
import os
from bs4 import BeautifulSoup
from openpyxl import Workbook
from requests.adapters import HTTPAdapter
# from googletrans import Translator
# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Connection": "keep-alive",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}

# 模拟cookie，请求失败后重复次数
sess = requests.Session()
sess.mount('http://', HTTPAdapter(max_retries=3))
sess.mount('https://', HTTPAdapter(max_retries=3))


# 翻译功能    问题:translate.google.com网页打开不了
# def Translate(text):
#     translator = Translator(service_urls=['translate.google.cn', ])
#     trans = translator.translate(text, src='en', dest='zh-cn')
#     return trans.text


# 请求响应
def getText(url, timeout):
    # print(url)  # 输出请求地址
    try:
        return sess.get(url, timeout=timeout, headers=headers).text
    except:
        pass

    # 创建表格
def create_xlsx(filename="1.xlsx"):
    if os.path.exists("./" + filename) != True:  # 使用函数exists()对文件存在与否进行判断，存在为True,不存在为False.
        wb = Workbook()  # 创建一个工作簿   打开一个已有的workbook：wb = load_workbook('file_name.xlsx')
        wb.save(filename)  # 保存工作簿
    else:
        pass


# 地址传入，并用bs4来抓取页面指定内容
def getURL(html):
    soup = BeautifulSoup(html, 'lxml')
    text = soup.find('div', {"class": "documents-list", "id": "documents"})  # 通过bs4查找相关元素，提取至text中
    lenght = len(text.find_all("article"))  # 提取当前页面中text下所有article元素的集合，得到的是长度len()
    # 遍历循环，传出收集到的图片地址
    all = []
    for x in range(0, lenght):
        # name=re.compile(r"document[ ]+document-position-%d[ ]+"%(x))
        t = text.find('article', {"data-document-counter": str(x)})
        tt = t.find("header", {"class": re.compile(r"documentHeader[ ]*row")}).find("a")  # r表示原生字符串,即 不用对正则表达式中的反斜杠版再转义
        all.append(tt.get("href"))
    return all


    # 传入html的text文本内容
    #文件名称以及excel表格名称定义
def getContext(html, filename, excel="1.xlsx"):
    soup = BeautifulSoup(html, 'lxml')     # 用bs4来抓取页面指定内容
    # 使用正则表达式捕获指定信息，采用的是python的re模块，使用搜索操作。
    t = soup.find("div", {"class": re.compile(r"row[ ]*flex-column-reverse[ ]*flex-md-row")}).find("div", {
        "class": "col-md-7"}).find("dl", {"class": re.compile(r"row[ ]*dl-invert[ ]*document-metadata")})

    dt = t
    dd = t
    en_context = ""
    cn_context = ""
    en_keyword = ""
    cn_keyword = ""
    flag = "doc_" + filename.replace(":", "-").lower()
    title = soup.find("div", {"id": flag}).find("h2", {"itemprop": "name"}).text
    en_context += title + "\n\n"
    # cn_context += Translate(title) + "\n\n"   #去掉中文翻译
    image_name = filename.replace(":", "_") + ".jpg"
    while dt and dd:
        dt = dt.find_next("dt")
        dd = dd.find_next("dd")
        if dt == None and dd == None:
            break
        if "Publication" in dt.text or "Language" in dt.text or "Format" in dt.text or "Subject" in dt.text or "Genre" in dt.text or "Abstract" in dt.text or "Contributor" in dt.text:
            if "Subject" in dt.text:
                en_keyword = dd.text
                # cn_keyword = Translate(dd.text.strip().replace("\n", "，")) + "\n\n"   #去掉翻译
                # cn_context += Translate(dt.text) + cn_keyword
            # else:
           # 去掉中文翻译     # cn_context += Translate(dt.text).replace("出版物：", "出版：").replace("抽象：", "摘要：") + Translate(
                #     dd.text.strip().replace("\n", "，")) + "\n\n"
            en_context += dt.text + dd.text.strip().replace("\n", ", ").replace("  ", "") + "\n\n"
    saveExcel("", image_name, en_context, "", en_keyword, "", "0000/00/00", "", "", excel)


# 保存到表格中
def saveExcel(id, image_file, en_data, cn_data, en_keyword, cn_keyword, image_time, author, _id, filename="1.xlsx"):
    data = {
        "id（留空）": id,
        "文件名": image_file,
        "英文图片内容说明": en_data,
        "图片说明": cn_data,
        "英文关键字": en_keyword,
        "中文关键字": cn_keyword,
        "图片创作时间": image_time,
        "图片作者署名": author,
        "id(分库名)": _id
    }
    data = pd.DataFrame(data, index=[0])
    df = pd.read_excel("./" + filename)
    df = df.append(data)
    df.to_excel("./" + filename, index=False)


def download(name, url):
    paths = []  # 存储地址的元组
    _url = "https://collections.nlm.nih.gov"  # 主地址
    get = "&page={}"  # 网址翻页操作
    excel = name + ".xlsx"  # 这是excel表格的名称，根据传入的name创建
    base_url = url + get  # 传入的地址为下面中all元组的地址加上"&page={}"
    print(base_url)   # 输出爬取地址:https://collections.nlm.nih.gov/?f%5Bdrep2.format%5D%5B%5D=&f%5Bdrep2.isMemberOfCollection%5D%5B%5D=DREPIHM&f%5Bdrep2.subjectAggregate%5D%5B%5D=Army+Medical+Library+%28U.S.%29&per_page=100&search_field=all_fields&page={}
    # url+"&page=1"会输出和https://collections.nlm.nih.gov&page=1不一样的地址
    # 这是因为传入的url为主程序main中all元组的地址
    html = getText(url + "&page=1", 50)  # 上面定义的函数getText(参数),请求服务器
    page = getPage(html)  # 使用getPage()获取页数
    # 循环,第一页到最后一页
    for x in range(1, page + 1):
        url = base_url.format(x)  # 格式化函数。按顺序排序
        text = getText(url, 50)  # 上面定义的函数getText(参数),
        paths += getURL(text)
    # print(paths)  输出的地址为: ['/catalog/nlm:nlmuid-101445564-img', '/catalog/nlm:nlmuid-101445565-img', '/catalog/nlm:nlmuid-101445539-img', '/catalog/nlm:nlmuid-101445567-img'...
    print("总个数为：", len(paths))  # 读取地址个数
    create_xlsx(excel)  # 创建excel表格
    # 循环输出得到的图片地址
    i = 0
    for path in paths:
        if path.endswith("img") != True:  # 确保图片为img格式
            continue
        filename = path.split("/")[-1]  # 以‘/ ’为分割符，保留最后一段
        i += 1
        url = _url + path  # 连接源地址以及图片地址，得到完整地址，进行数据保存
        # print(url)
        try:
            getContext(getText(url, 5), filename, excel)
            print(i, path, "保存成功")
        except Exception as e:
            print(e)
            print(i, path, "出现异常")


def getPage(html):
    soup = BeautifulSoup(html, "lxml")  # 抓取html页面的文本内容
    # 抓取soup元素下的指定内容
    text = soup.find("div", {"id": "sortAndPerPage"}).find("div", {"class": "page-links"}).find("span", {
        "class": "page-entries"})
    all = int(text.find_next("strong").find_next("strong").find_next("strong").string)  # 得到数值102
    # print(text.find_next("strong").find_next("strong").find_next("strong").string)  输出102，在text逐级向下，直至102
    shang, mod = divmod(all, 100)  # 返回商和余数，用shang来存取返回的商值，用mod存取返回的余数
    if mod == 0:
        return shang
    else:
        shang += 1
        return shang


if "__main__" == __name__:
    all = {
        #     左边为名称name，右边为地址url
        "陆军医学图书馆（美国）": "https://collections.nlm.nih.gov/?f%5Bdrep2.format%5D%5B%5D=&f%5Bdrep2.isMemberOfCollection%5D%5B%5D=DREPIHM&f%5Bdrep2.subjectAggregate%5D%5B%5D=Army+Medical+Library+%28U.S.%29&per_page=100&search_field=all_fields",

        "参展主题":"https://collections.nlm.nih.gov/?f%5Bdrep2.format%5D%5B%5D=&f%5Bdrep2.isMemberOfCollection%5D%5B%5D=DREPIHM&f%5Bdrep2.subjectAggregate%5D%5B%5D=Exhibits+as+Topic&per_page=100&search_field=all_fields",

        "比利时":"https://collections.nlm.nih.gov/?f%5Bdrep2.format%5D%5B%5D=&f%5Bdrep2.isMemberOfCollection%5D%5B%5D=DREPIHM&f%5Bdrep2.subjectAggregate%5D%5B%5D=Belgium&per_page=100&search_field=all_fields",

        "卫生":"https://collections.nlm.nih.gov/?f%5Bdrep2.format%5D%5B%5D=&f%5Bdrep2.isMemberOfCollection%5D%5B%5D=DREPIHM&f%5Bdrep2.subjectAggregate%5D%5B%5D=Hygiene&per_page=100&search_field=all_fields",

        "美国国立卫生研究院":"https://collections.nlm.nih.gov/?f%5Bdrep2.format%5D%5B%5D=&f%5Bdrep2.isMemberOfCollection%5D%5B%5D=DREPIHM&f%5Bdrep2.subjectAggregate%5D%5B%5D=National+Institute+of+Health+%28U.S.%29&per_page=100&search_field=all_fields",

        "军事护理":"https://collections.nlm.nih.gov/?f%5Bdrep2.format%5D%5B%5D=&f%5Bdrep2.isMemberOfCollection%5D%5B%5D=DREPIHM&f%5Bdrep2.subjectAggregate%5D%5B%5D=Military+Nursing&per_page=100&search_field=all_fields",

        "手术室":"https://collections.nlm.nih.gov/?f%5Bdrep2.format%5D%5B%5D=&f%5Bdrep2.isMemberOfCollection%5D%5B%5D=DREPIHM&f%5Bdrep2.subjectAggregate%5D%5B%5D=Operating+Rooms&per_page=100&search_field=all_fields",

        "育儿":"https://collections.nlm.nih.gov/?f%5Bdrep2.format%5D%5B%5D=&f%5Bdrep2.isMemberOfCollection%5D%5B%5D=DREPIHM&f%5Bdrep2.subjectAggregate%5D%5B%5D=Child+Care&per_page=100&search_field=all_fields",

        "筹款":"https://collections.nlm.nih.gov/?f%5Bdrep2.format%5D%5B%5D=&f%5Bdrep2.isMemberOfCollection%5D%5B%5D=DREPIHM&f%5Bdrep2.subjectAggregate%5D%5B%5D=Fund+Raising&per_page=100&search_field=all_fields",

        "日本":"https://collections.nlm.nih.gov/?f%5Bdrep2.format%5D%5B%5D=&f%5Bdrep2.isMemberOfCollection%5D%5B%5D=DREPIHM&f%5Bdrep2.subjectAggregate%5D%5B%5D=Japan&per_page=100&search_field=all_fields",

        "儿童发展":"https://collections.nlm.nih.gov/?f%5Bdrep2.format%5D%5B%5D=&f%5Bdrep2.isMemberOfCollection%5D%5B%5D=DREPIHM&f%5Bdrep2.subjectAggregate%5D%5B%5D=Child+Development&per_page=100&search_field=all_fields",
    }

    for k, v in all.items():
        print("------------------------------------分割线------------------------------------")
        download(k, v)
        print("------------------------------------分割线------------------------------------")
