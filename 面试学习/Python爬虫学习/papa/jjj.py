import re

import pandas as pd
import requests
import os
from bs4 import BeautifulSoup
from googletrans import Translator
from openpyxl import Workbook
from requests.adapters import HTTPAdapter

def create_xlsx(filename="1.xlsx"):
    if os.path.exists("./" + filename) != True:  # 使用函数exists()对文件存在与否进行判断，存在为True,不存在为False.
        wb = Workbook()  # 创建一个工作簿   打开一个已有的workbook：wb = load_workbook('file_name.xlsx')
        wb.save(filename)  # 保存工作簿
    else:
        pass

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

if "__main__" == __name__:

        print("------------------------------------分割线------------------------------------")

        print("------------------------------------分割线------------------------------------")