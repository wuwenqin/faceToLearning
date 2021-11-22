# 							cookie模拟登录操作学习	

## 前言：

​	模拟登录：——爬取基于某些用户的用户信息。

需求：对古诗文网进行模拟登录。（网址：https://so.gushiwen.cn/user/login.aspx)

​			——点击登录按钮后会发起一个post请求

​			——post请求中会携带登录之前录入的相关登录信息（用户名、密码、验证码...）

​			——验证码：每次请求都会变化



​		首先，为什么要用cookie来模拟登录呢(不能直接爬取登录后的界面吗?)——

这是因为http/https 协议的特性：无状态，所以无法直接爬登陆后的界面。

如何解决上述问题？——这就要使用本次学习到的Cookie进行模拟登录 了，cookie是一个用来让服务器端记录客户端的相关状态，它保存在客户端中。

​	那么，如何获取cookie呢？有两种方法：

​	1.手动处理：通过抓包工具获取Cookie值，将该cookie封装到headers中(麻烦，不建议)

​	2.自动处理：

​	如何实现自动处理，那么需要先知道cookie值的来源在哪里？—— 模拟登录post请求后，由服务器端创建。

session会话对象:

​	作用：1.可以进行请求的发送。

​				2.如果请求过程中产生了cookie，则该cookie会被自动存储/携带在该session对象中。在使用session进行请求和发送的过程中产生了cookie，则cookie会被自动存储在session对象中

​	

​	—— 创建一个session对象 ： session=requests.Session()

​	——使用session对象进行模拟登录post请求的发送(cookie就会被存储在session中)

​	——session对象对个人主页对应的get请求进行发送(携带了cookie)





## 注意点：

​		可能会出现HttpConnectinPool的bug: 

​		原因： 	1.短时间内发起了高频的轻轻导致ip被禁 	
​						  2.http连接池中的连接资源被耗尽 

​		解决： 	1.使用代理 	

​						  2.headers中加入Connection:"**close**" 



代理是什么呢？以及如何使用代理？——  通过代理服务器，接受请求并进行转发，无法确定真实IP地址，就不会出现IP被禁的问题了。

免费的代理网址：https://www.kuaidaili.com/free/

如何使用，代码呈上

```java
import requests


headers={
"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
# "accept-encoding": "gzip, deflate, br", # 删除该列
"accept-language": "zh,en;q=0.9,zh-CN;q=0.8",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
}

    

#构建一个随机的ip池，防着被网站看拉黑
proxie_list=[
    {"http": "43.249.224.172:83"},
    {"http": "60.167.112.174:1133"},
    {"http": "60.186.40.211:9000"},
    {"http": "172.67.68.216:80"},
    {"http": "47.52.135.122:8118"},
    {"http": "121.4.103.166:7890"},
    {"http": "31.24.206.54:8080"},
    {"http": "185.56.209.114:52342"},
    {"http": "36.66.16.193:80"},
    {"http": "52.43.61.135:80"},
    {"http": "190.217.14.113:999"},
    {"http": "60.250.159.191:45983"},
    {"http": "190.217.231.8:999"},
    {"http": "37.110.36.79:8000"},
    {"http": "27.191.60.113:3256"},
    {"http": "179.1.130.23:999"},
    {"http": "45.174.79.189:999"},
    {"http": "203.190.43.158:8080"},
    {"http": "45.172.111.35:999"},
    {"http": "181.78.11.216:999"},

]

proxy=random.choice(proxie_list)#随机抽取一个ip来进行访问url
    
    

```





## 进行Cookie模拟登录测试：

​		如果使用手动将cookie封装到headers中，由于cookie有时效性在一段时间后会失效，这样需要多次更改cookie值，繁琐且麻烦。故这里不做叙述，使用自动注入cookie操作。

​		需要使用超级鹰来进行验证码识别，并使用Session存储登录状态，当进入个人主页时即可使用当前的Cookie模拟登录。

```java
#!/usr/bin/env python
# coding:utf-8

import requests
from lxml import etree
import os
from fake_useragent import UserAgent
import random
import xlwt
from hashlib import md5
import session3

class Chaojiying_Client(object):#超级鹰验证码识别代码，不用管，也不用编辑

    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()



# ua=UserAgent(verify_ssl=False)#随机进行UA伪装
# headers={'User-Agent':ua.random}#随机进行UA伪装
# #构建一个随机的ip池，防着被网站看拉黑
# proxie_list=[
#     {"http": "43.249.224.172:83"},
#     {"http": "60.167.112.174:1133"},
#     {"http": "60.186.40.211:9000"},
#     {"http": "172.67.68.216:80"},
#     {"http": "47.52.135.122:8118"},
#     {"http": "121.4.103.166:7890"},
#     {"http": "31.24.206.54:8080"},
#     {"http": "185.56.209.114:52342"},
#     {"http": "36.66.16.193:80"},
#     {"http": "52.43.61.135:80"},
#     {"http": "190.217.14.113:999"},
#     {"http": "60.250.159.191:45983"},
#     {"http": "190.217.231.8:999"},
#     {"http": "37.110.36.79:8000"},
#     {"http": "27.191.60.113:3256"},
#     {"http": "179.1.130.23:999"},
#     {"http": "45.174.79.189:999"},
#     {"http": "203.190.43.158:8080"},
#     {"http": "45.172.111.35:999"},
#     {"http": "181.78.11.216:999"},
#
# ]
#
# proxy=random.choice(proxie_list)#随机抽取一个ip来进行访问url
#
#
# url="https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"
# page_text=requests.get(url=url,headers=headers,proxies=proxy).text
# tree=etree.HTML(page_text)
# code_img_src="https://so.gushiwen.cn"+tree.xpath("//*[@id='imgCode']/@src")[0]
# img_data=requests.get(url=code_img_src,headers=headers,proxies=proxy).content
# with open("./code.jpg","wb") as fp:
#     fp.write(img_data)
#
#
# #登录后的页面处理
# log_url="https://so.gushiwen.cn/user/collect.aspx"
#
# data={
#     "__VIEWSTATE": "mIT87jvLWqmA71nGBN6MfatXvvLvR6jAvtyY61i3gRxJqMjw7NqxPc2HCqPqIOYLqfPqSvhgVLnPFvmM6zbRwL90Z12kCUaCM6RuXi0seSG6ijxPQhRGjnbQPTo=",
#     "__VIEWSTATEGENERATOR": "C93BE1AE",
#     "from": "http://so.gushiwen.cn/user/collect.aspx",
#     "email": "13226181132@163.com",
#     "pwd": "wan@@cys1019",
#     "code": result
# }
# log_page_text=requests.get(url=log_url,headers=headers,proxies=proxy,data=data).text
# with open("gushicidengluhaod.html","w",encoding="utf-8") as fp:
#     fp.write(log_page_text)
#
#
#
#
#
#
#
#
# if __name__ == '__main__':
#         chaojiying = Chaojiying_Client('13226181132', '123456789..', '924695')	#用户中心>>软件ID 生成一个替换 96001
#         im = open('code.jpg', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
#         result=chaojiying.PostPic(im, 1902)["pic_str"]
#         print(chaojiying.PostPic(im, 1902))											#1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
#         print(result)






# ua=UserAgent(verify_ssl=False)#随机进行UA伪装
# headers={'User-Agent':ua.random}#随机进行UA伪装
#构建一个随机的ip池，防着被网站看拉黑
proxie_list=[
    {"http": "43.249.224.172:83"},
    {"http": "60.167.112.174:1133"},
    {"http": "60.186.40.211:9000"},
    {"http": "172.67.68.216:80"},
    {"http": "47.52.135.122:8118"},
    {"http": "121.4.103.166:7890"},
    {"http": "31.24.206.54:8080"},
    {"http": "185.56.209.114:52342"},
    {"http": "36.66.16.193:80"},
    {"http": "52.43.61.135:80"},
    {"http": "190.217.14.113:999"},
    {"http": "60.250.159.191:45983"},
    {"http": "190.217.231.8:999"},
    {"http": "37.110.36.79:8000"},
    {"http": "27.191.60.113:3256"},
    {"http": "179.1.130.23:999"},
    {"http": "45.174.79.189:999"},
    {"http": "203.190.43.158:8080"},
    {"http": "45.172.111.35:999"},
    {"http": "181.78.11.216:999"},

]
proxy=random.choice(proxie_list)#随机抽取一个ip来进行访问url

headers={
"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-language": "zh,en;q=0.9,zh-CN;q=0.8",
"connection":"close",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
}

# 创建一个session对象，用来存放cookie
session = requests.Session()
global __VIEWSTATE
global __VIEWSTATEGENERATOR

# 通过超级鹰提取验证码图片信息
def getCode(getImg_url):
    page_text = session.get(url=getImg_url, headers=headers).text
    tree = etree.HTML(page_text)
    code_img_src = "https://so.gushiwen.cn" + tree.xpath("//*[@id='imgCode']/@src")[0]
    img_data = session.get(url=code_img_src, headers=headers).content
    with open("./code.jpg", "wb") as fp:
        fp.write(img_data)

    global __VIEWSTATE
    global __VIEWSTATEGENERATOR
    # 获得动态变化的请求值
    __VIEWSTATE = tree.xpath("//*[@id='__VIEWSTATE']/@value")[0]
    __VIEWSTATEGENERATOR = tree.xpath("//*[@id='__VIEWSTATEGENERATOR']/@value")[0]
    chaojiying = Chaojiying_Client('13226181132', '123456789..', '924695')  # 用户中心>>软件ID 生成一个替换 96001
    im = open('code.jpg', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    result = chaojiying.PostPic(im, 1902)["pic_str"]  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    print(chaojiying.PostPic(im, 1902))
    return result


#登录后的页面处理
def log_download(log_url,result):
    # post请求的data数据
    data={
        "__VIEWSTATE": __VIEWSTATE,
        "__VIEWSTATEGENERATOR": __VIEWSTATEGENERATOR,
        "from": "http://so.gushiwen.cn/user/collect.aspx",
        "email": "13226181132@163.com",   # 邮箱
        "pwd": "wan@@cys1019",  # 密码
        "code": result,   # 验证码
        "denglu": "登录"
    }
    print(data)
    #使用session进行post请求的发送
    log_page_text=session.post(url=log_url,headers=headers,data=data)
    print(log_page_text.status_code)

    personernal_page_link="https://so.gushiwen.cn/user/collect.aspx?type=s&id=2253759&sort=t"
    personernal_page=session.get(url=personernal_page_link,headers=headers).text


    with open("gushicidengluhaod1.html","w",encoding="utf-8") as fp:
        fp.write(personernal_page)


if __name__ == '__main__':
        getImg_url="https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"
        result=getCode(getImg_url)
        log_url = "https://so.gushiwen.cn/user/login.aspx"
        log_download(log_url,result)


```























