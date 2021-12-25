# 										Requests模块学习

## 一.认识Requests	

​		① requests是什么呢？——在源码中，它是这样解释的：“Requests is an HTTP library, written in Python, for human beings.”(Requests 是一个用 Python 编写的 **HTTP 库**，供人类使用)。

​		② 那么，requests既然是一个便于使用的**HTTP库**，它有什么好处呢？——这里需要了解到，**Requests继承了urllib2的所有特性。且Requests支持HTTP连接保持和连接池，支持使用cookie保持会话，支持文件上传，支持自动确定响应内容的编码，支持国际化的 URL 和 POST 数据自动编码。**

​		③ 并且，requests的**底层实现实际上是urllib3**(对其进行的一个封装)。



## 二.安装Requests

​		通过**Windows系统中的cmd窗口或PyCharms软件中的Terminal**中输入以下命令即可：

```python
pip install requests
```



## 三.Requests中的基本请求（headers参数 和 parmas参数）

​		① 基本GET请求

​		（1）直接使用get请求网址

```python
response = requests.get("http://www.baidu.com/")
```

​		（2）除了网址，添加headers和查询参数

```python
 
import requests
 
kw = {'wd':'长城'}
 
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
 
# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
response = requests.get("http://www.baidu.com/s?", params = kw, headers = headers)
 
# 查看响应内容，response.text 返回的是Unicode格式的数据
print response.text
 
# 查看响应内容，response.content返回的字节流数据
print respones.content
 
# 查看完整url地址
print response.url
 
# 查看响应头部字符编码
print response.encoding
 
# 查看响应码
print response.status_code
```

​		也可以通过控制台输入，获取想要查询的对象，将之put到url中：

```python
import requests

content=input("请输入您要检索的内容")
url="https://www.sogou.com/tx?ie=utf-8&query={content}"
headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3877.400 QQBrowser/10.8.4506.400"
}
page_text=requests.get(url=url,headers=headers).text
print(page_text)
```

​		ps:	① 这里可以先通过查看响应内容的字符编码encoding，然后在给encoding赋予对应的字符编码，解决乱码问题。

​				  ② 使用response.text 时，Requests会基于HTTP响应的文本编码自动解码响应内容，大多数Unicode字符集都能被无缝的解码。

​				  ③ 使用response.content时，返回的是服务器响应数据的原始二进制字节流，可以用来保存图片等二进制文件。

------



​	② 基本POST请求(data参数)

​		(1) 直接使用POST请求

```python
response = requests.post("http://www.baidu.com/", data = data)
```

​		(2) 传入data数据。对于POST请求来说，比如登录注册、有道翻译模块类的，需要传入用户名、密码等数据。这时可以通过data这个参数传递。

```python
import requests
 
formdata = {
    "type":"AUTO",
    "i":"i love python",
    "doctype":"json",
    "xmlVersion":"1.8",
    "keyfrom":"fanyi.web",
    "ue":"UTF-8",
    "action":"FY_BY_ENTER",
    "typoResult":"true"
}
 
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
 
headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
 
response = requests.post(url, data = formdata, headers = headers)
 
# 字符串类型
print response.text
 
# 如果是json文件可以直接显示，字典类型
print response.json()
```

也可以通过控制台输入数据，将数据传入到data参数中即可。

```python
import requests
import json

content=input("请输入您要检索的内容")
url="https://fanyi.baidu.com/sug"
headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}
data={
    "kw":content
}
page_text=requests.post(url=url,data=data,headers=headers)
print("打印text")
print(page_text.text)#拿到的是文本字符串
print("打印json")
print(page_text.json())#此时拿到的直接就是json数据
```



诸如其他HTTP请求类型：PUT、DELETE、HEAD以及OPTIONS也如上述类似：

```python
r = requests.put('http://httpbin.org/put', data = {'key':'value'})
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')
```



​	④ 请求中的IP代理(proxies参数)

```python
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
response=requests.get("http://www.baidu.com",proxies=proxy)
print(response.text)
```

 

​	⑤ Cookie

​		如果一个响应中包含cookie，那么我们可以通过cookie参数拿到数据：

```python
 
import requests
 
response = requests.get("http://www.baidu.com/")
 
# 7. 返回CookieJar对象:
cookiejar = response.cookies
 
# 8. 将CookieJar转为字典：
cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
 
print cookiejar
 
print cookiedict
```

运行结果为：

```python
<RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
{'BDORZ': '27315'}
```



​	⑥ Session

​	在Request请求中，session对象代表着一次用户会话：从客户端浏览器连接服务器开始，直到客户端浏览器与服务器断开。

​		在同一个session实例中所发出的所有请求之间会保持着cookie参数。





​	实现古诗词网登录：（需要借助超级鹰进行验证码识别）

```python

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

    
    
    
ua=UserAgent(verify_ssl=False)#随机进行UA伪装

headers={
"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
# "accept-encoding": "gzip, deflate, br", # 删除该列
"accept-language": "zh,en;q=0.9,zh-CN;q=0.8",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
}


# headers={'User-Agent':ua.random,
#          "cookie": "login=flase; ASP.NET_SessionId=segmscmb33zmzjaasljhn2n0; codeyzgswso=c3bb48d484992650; Hm_lvt_9007fab6814e892d3020a64454da5a55=1637388280; Hm_lpvt_9007fab6814e892d3020a64454da5a55=1637388280",
#          }#随机进行UA伪装
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

#创建一个session对象，用来存放cookie
session=requests.Session()
#
#
#
# #保存登录界面的验证码
# url="https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"
# page_text=session.get(url=url,headers=headers).text.encode("utf-8")
#
# tree=etree.HTML(page_text)
# imgpath=tree.xpath("//*[@id='imgCode']/@src")[0]
# print(imgpath)
# code_img_src="https://so.gushiwen.cn"+imgpath
# img_data=session.get(url=code_img_src,headers=headers).content
# with open("./code.jpg","wb") as fp:
#     fp.write(img_data)



#登录后的页面处理
def log_download(log_url):
    data={
        "__VIEWSTATE": "vTuu3oq7dJpq6lpKDpW+yreKeYa1KRkkQSRrugGcODskYprNPLI6gV9fDpiSqakMpplO+PvyHl3MXjG87+ZZCdqVxXnb6ugutWclE6sErQVe7STDXs1Jfe0Bm94=",
        "__VIEWSTATEGENERATOR": "C93BE1AE",
        "from": "http://so.gushiwen.cn/user/collect.aspx",
        "email": "13226181132@163.com",
        "pwd": "wan@@cys1019",
        "code": result,
        "denglu":"登录"
    }
    #使用session进行post请求的发送
    log_page_text=session.post(url=log_url,headers=headers,proxies=proxy,data=data)
    print(log_page_text.status_code)

    personernal_page_link="https://so.gushiwen.cn/user/collect.aspx?type=s&id=2253759&sort=t"
    personernal_page=session.get(url=personernal_page_link,headers=headers).text

    with open("gushicidengluhaod1.html","w",encoding="utf-8") as fp:
        fp.write(personernal_page)



if __name__ == '__main__':
        url = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"
        page_text = session.get(url=url, headers=headers).text
        tree = etree.HTML(page_text)
        imgpath = tree.xpath("//*[@id='imgCode']/@src")[0]
        print(imgpath)
        code_img_src = "https://so.gushiwen.cn" + imgpath
        img_data = session.get(url=code_img_src, headers=headers).content
        with open("./code.jpg", "wb") as fp:
            fp.write(img_data)

        # 获得动态变化的请求值
        __VIEWSTATE=tree.xpath("//*[@id='__VIEWSTATE']/@value")[0]
        __VIEWSTATEGENERATOR=tree.xpath("//*[@id='__VIEWSTATEGENERATOR']/@value")[0]
        chaojiying = Chaojiying_Client('13226181132', '123456789..', '924695')	#用户中心>>软件ID 生成一个替换 96001
        im = open('code.jpg', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
        result = chaojiying.PostPic(im, 1902)["pic_str"]

        data = {
            "__VIEWSTATE": __VIEWSTATE,
            "__VIEWSTATEGENERATOR": __VIEWSTATEGENERATOR,
            "from": "http://so.gushiwen.cn/user/collect.aspx",
            "email": "13226181132@163.com",
            "pwd": "wan@@cys1019",
            "code": result,
            "denglu": "登录"
        }
        log_url = "https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx"
        # log_download(log_url)
        print(chaojiying.PostPic(im, 1902))											#1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
        print(result)
        log_page_text = session.post(url=log_url, headers=headers,  data=data)
        print(log_page_text.status_code)


        personernal_page_link = "https://so.gushiwen.cn/user/collect.aspx?type=s&id=2253759&sort=t"
        personernal_page = session.get(url=personernal_page_link, headers=headers).text
        with open("gushicidengluhaod1.html", "w", encoding="utf-8") as fp:
            fp.write(personernal_page)

    
```



​	⑦ 处理HTTPS请求种的SSL证书验证：使用**verify参数**(True/False)

```python
response = requests.get("https://www.baidu.com/", verify=True)
```



​	⑧ 超时：**timeout** 参数，设置最长响应时间

```python
requests.get("https://www.baidu.com/", timeout=10)
```

这里应该注意一点，timeout仅对连接过程有效，与响应体的下载无关。`timeout` 并不是整个下载响应的时间限制，而是如果服务器在 `timeout` 秒内没有应答，将会引发一个异常（更精确地说，是在 `timeout` 秒内没有从基础套接字上接收到任何字节的数据时）If no timeout is specified explicitly, requests do not time out.









## 四.状态码

```python
# 信息性状态码
100: ('continue',),
101: ('switching_protocols',),
102: ('processing',),
103: ('checkpoint',),
122: ('uri_too_long', 'request_uri_too_long'),

# 成功状态码
200: ('ok', 'okay', 'all_ok', 'all_okay', 'all_good', '\\o/', '✓'),
201: ('created',),
202: ('accepted',),
203: ('non_authoritative_info', 'non_authoritative_information'),
204: ('no_content',),
205: ('reset_content', 'reset'),
206: ('partial_content', 'partial'),
207: ('multi_status', 'multiple_status', 'multi_stati', 'multiple_stati'),
208: ('already_reported',),
226: ('im_used',),

# 重定向状态码
300: ('multiple_choices',),
301: ('moved_permanently', 'moved', '\\o-'),
302: ('found',),
303: ('see_other', 'other'),
304: ('not_modified',),
305: ('use_proxy',),
306: ('switch_proxy',),
307: ('temporary_redirect', 'temporary_moved', 'temporary'),
308: ('permanent_redirect',
      'resume_incomplete', 'resume',), # These 2 to be removed in 3.0

# 客户端错误状态码
400: ('bad_request', 'bad'),
401: ('unauthorized',),
402: ('payment_required', 'payment'),
403: ('forbidden',),
404: ('not_found', '-o-'),
405: ('method_not_allowed', 'not_allowed'),
406: ('not_acceptable',),
407: ('proxy_authentication_required', 'proxy_auth', 'proxy_authentication'),
408: ('request_timeout', 'timeout'),
409: ('conflict',),
410: ('gone',),
411: ('length_required',),
412: ('precondition_failed', 'precondition'),
413: ('request_entity_too_large',),
414: ('request_uri_too_large',),
415: ('unsupported_media_type', 'unsupported_media', 'media_type'),
416: ('requested_range_not_satisfiable', 'requested_range', 'range_not_satisfiable'),
417: ('expectation_failed',),
418: ('im_a_teapot', 'teapot', 'i_am_a_teapot'),
421: ('misdirected_request',),
422: ('unprocessable_entity', 'unprocessable'),
423: ('locked',),
424: ('failed_dependency', 'dependency'),
425: ('unordered_collection', 'unordered'),
426: ('upgrade_required', 'upgrade'),
428: ('precondition_required', 'precondition'),
429: ('too_many_requests', 'too_many'),
431: ('header_fields_too_large', 'fields_too_large'),
444: ('no_response', 'none'),
449: ('retry_with', 'retry'),
450: ('blocked_by_windows_parental_controls', 'parental_controls'),
451: ('unavailable_for_legal_reasons', 'legal_reasons'),
499: ('client_closed_request',),

# 服务端错误状态码
500: ('internal_server_error', 'server_error', '/o\\', '✗'),
501: ('not_implemented',),
502: ('bad_gateway',),
503: ('service_unavailable', 'unavailable'),
504: ('gateway_timeout',),
505: ('http_version_not_supported', 'http_version'),
506: ('variant_also_negotiates',),
507: ('insufficient_storage',),
509: ('bandwidth_limit_exceeded', 'bandwidth'),
510: ('not_extended',),
511: ('network_authentication_required', 'network_auth', 'network_authentication')
```



## 五.通过request进行文件上传

```python
import requests

files={"file":open("D:\\simpleMybatis\\src\\main\\webapp\\imgs\\1.jpg","rb")}
response=requests.post("http://httpbin.org/post",files=files)
print(response.text)

```

运行结果：

```
{
  "args": {}, 
  "data": "", 
  "files": {
    "file": "data:application/octet-stream;base64,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"
  }, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "26505", 
    "Content-Type": "multipart/form-data; boundary=54b9a66471949936beb4d169dee9aa9f", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.24.0", 
    "X-Amzn-Trace-Id": "Root=1-61b23027-0484ff1536a8c72574ae1eb7"
  }, 
  "json": null, 
  "origin": "18.163.124.254", 
  "url": "http://httpbin.org/post"
}

```

p.s:要么使用相对路径(相对于当前文件所在位置)，要么使用绝对路径(记得遇到**"\	"** 时需要转义，即**"\\"**)



