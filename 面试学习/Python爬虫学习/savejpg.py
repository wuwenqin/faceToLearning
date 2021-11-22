import os
import re
from multiprocessing import *
from urllib.request import urlretrieve

import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Connection": "keep-alive",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}

sess=requests.Session()
sess.mount('http://', HTTPAdapter(max_retries=3))
sess.mount('https://', HTTPAdapter(max_retries=3))

def getText(url,timeout):
    try:
        return sess.get(url,timeout=timeout,headers=headers).text
    except:
        pass

def getURL(html):
    soup = BeautifulSoup(html, 'lxml')
    text=soup.find('div',{"class":"documents-list","id":"documents"})
    lenght=len(text.find_all("article"))
    all=[]
    for x in range(0,lenght):
        name=re.compile(r"document[  ]+document-position-%d[ ]+"%(x))
        # t=text.find('article',{"itemtype":"http://schema.org/Thing","class":name})
        t = text.find('article', {"data-document-counter": str(x)})
        tt=t.find("header",{"class":re.compile(r"documentHeader[ ]*row")}).find("a")
        all.append(tt.get("href"))
    return all


def save(path,filename):
    i=0
    while i<5:
        try:
            urlretrieve(path, filename)
            print(filename,"保存成功！")
            return
        except Exception as e:
            i+=1
    print(filename,"保存失败！！！")

def set_dir(filename="img"):
    if os.path.exists(filename)!=True:
        os.makedirs(filename)  # 用于递归创建目录。如果子目录创建失败或者已经存在，会抛出一个 OSError 的异常，Windows上Error 183 即为目录已经存在的异常错误。
# 如果第一个参数 path 只有一级，则 mkdir() 函数相同。
    else:
        pass

def getPage(html):
    soup=BeautifulSoup(html,"lxml")
    text=soup.find("div",{"id":"sortAndPerPage"}).find("div",{"class":"page-links"}).find("span",{"class":"page-entries"})
    all=int(text.find_next("strong").find_next("strong").find_next("strong").string)

    shang,mod=divmod(all,100)

    if mod==0:
        return shang
    else:
        shang+=1
        return shang

def download(project,url):
    paths=[]
    _url = "https://collections.nlm.nih.gov"
    get="&page={}"
    name="{}/img/".format(project)
    base_url=url+get

    html=getText(url+"&page=1",50)
    page=getPage(html)

    for x in range(1,page+1):
        url=base_url.format(x)
        text = getText(url,50)
        paths += getURL(text)   # 总地址上的所有图片地址
    print("总个数为：",len(paths))

    set_dir(name)

    pool = Pool(processes=20)
    for path in paths:
        if path.endswith("img")!=True:   # 判断后缀
            continue
        filename=name+path.split("/")[-1].replace(":","_")+".jpg"   # 构建文件名
        url=_url+path.replace("catalog","jpg")

        pool.apply_async(func=save,args=(url,filename))
    pool.close()
    pool.join()
    return

if "__main__"==__name__:
    all = {
        "陆军医学图书馆（美国）": "https://collections.nlm.nih.gov/?f%5Bdrep2.format%5D%5B%5D=&f%5Bdrep2.isMemberOfCollection%5D%5B%5D=DREPIHM&f%5Bdrep2.subjectAggregate%5D%5B%5D=Army+Medical+Library+%28U.S.%29&per_page=100&search_field=all_fields",

        "参展主题": "https://collections.nlm.nih.gov/?f%5Bdrep2.format%5D%5B%5D=&f%5Bdrep2.isMemberOfCollection%5D%5B%5D=DREPIHM&f%5Bdrep2.subjectAggregate%5D%5B%5D=Exhibits+as+Topic&per_page=100&search_field=all_fields",

        "比利时": "https://collections.nlm.nih.gov/?f%5Bdrep2.format%5D%5B%5D=&f%5Bdrep2.isMemberOfCollection%5D%5B%5D=DREPIHM&f%5Bdrep2.subjectAggregate%5D%5B%5D=Belgium&per_page=100&search_field=all_fields",

        "卫生": "https://collections.nlm.nih.gov/?f%5Bdrep2.format%5D%5B%5D=&f%5Bdrep2.isMemberOfCollection%5D%5B%5D=DREPIHM&f%5Bdrep2.subjectAggregate%5D%5B%5D=Hygiene&per_page=100&search_field=all_fields",

        "美国国立卫生研究院": "https://collections.nlm.nih.gov/?f%5Bdrep2.format%5D%5B%5D=&f%5Bdrep2.isMemberOfCollection%5D%5B%5D=DREPIHM&f%5Bdrep2.subjectAggregate%5D%5B%5D=National+Institute+of+Health+%28U.S.%29&per_page=100&search_field=all_fields",

        "军事护理": "https://collections.nlm.nih.gov/?f%5Bdrep2.format%5D%5B%5D=&f%5Bdrep2.isMemberOfCollection%5D%5B%5D=DREPIHM&f%5Bdrep2.subjectAggregate%5D%5B%5D=Military+Nursing&per_page=100&search_field=all_fields",
        #
        # "手术室": "https://collections.nlm.nih.gov/?f%5Bdrep2.format%5D%5B%5D=&f%5Bdrep2.isMemberOfCollection%5D%5B%5D=DREPIHM&f%5Bdrep2.subjectAggregate%5D%5B%5D=Operating+Rooms&per_page=100&search_field=all_fields",
        #
        # "育儿": "https://collections.nlm.nih.gov/?f%5Bdrep2.format%5D%5B%5D=&f%5Bdrep2.isMemberOfCollection%5D%5B%5D=DREPIHM&f%5Bdrep2.subjectAggregate%5D%5B%5D=Child+Care&per_page=100&search_field=all_fields",
        #
        # "筹款": "https://collections.nlm.nih.gov/?f%5Bdrep2.format%5D%5B%5D=&f%5Bdrep2.isMemberOfCollection%5D%5B%5D=DREPIHM&f%5Bdrep2.subjectAggregate%5D%5B%5D=Fund+Raising&per_page=100&search_field=all_fields",
        #
        # "日本": "https://collections.nlm.nih.gov/?f%5Bdrep2.format%5D%5B%5D=&f%5Bdrep2.isMemberOfCollection%5D%5B%5D=DREPIHM&f%5Bdrep2.subjectAggregate%5D%5B%5D=Japan&per_page=100&search_field=all_fields",
        #
        # "儿童发展": "https://collections.nlm.nih.gov/?f%5Bdrep2.format%5D%5B%5D=&f%5Bdrep2.isMemberOfCollection%5D%5B%5D=DREPIHM&f%5Bdrep2.subjectAggregate%5D%5B%5D=Child+Development&per_page=100&search_field=all_fields",
    }

    for k, v in all.items():
        print("------------------------------------分割线------------------------------------")
        download(k, v)
        print("------------------------------------分割线------------------------------------")