# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
import pandas as pd

# 和setttings.py
from openpyxl import Workbook


class PapaPipeline(object):
    def process_item(self, item, spider):
        return item
    pass

# 定义的 # 和setttings.py
class ggkk(object):

    def create_xlsx(self,filename="1.xlsx"):
        if os.path.exists("./" + filename) != True:  # 使用函数exists()对文件存在与否进行判断，存在为True,不存在为False.
            wb = Workbook()  # 创建一个工作簿   打开一个已有的workbook：wb = load_workbook('file_name.xlsx')
            wb.save(filename)  # 保存工作簿
        else:
            pass

    def write_content(self, item):
        # 提取内容
        excel="1.xlsx"
        Img=item["Img"]
        Title = item["Title"]
        Alter = item["Alter"]
        Date = item["Date"]
        Creator = item["Creator"]
        en_context=Title+"\n"+Alter+"\n"+Date+"\n"+Creator
        Location = item["Location"]
        Format = item["Format"]
        en_keyword=Format
        Dig = item["Dig"]
        self.create_xlsx("1.xlsx")
        saveExcel("", Img, en_context, "", en_keyword, "", "0000/00/00", "", "", excel)
        # # 用self.file.write（）写入
        # self.file.write('{},{},{},{},{},{},{},{}'.format(Img,Title,Alter,Date,Creator,Location,Format,Dig) + '\n')
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
