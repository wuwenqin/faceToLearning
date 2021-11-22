import scrapy
from urllib import parse
from papa.items import StockItme


class MySpider(scrapy.Spider):
    name = 'example'

    # 添加URL参数
    def __init__(self, category=None, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.start_urls=['https://repository.duke.edu/dc/gamble?f%5Bcommon_model_name_ssi%5D%5B%5D=Item&page=1&per_page=100']

    # 获取url并访问
    def parse(self, response):
        post_urls= response.xpath("//*[@id=\"documents\"]/div/div/a/@href").extract()
        print(len(post_urls))
        for post_url in post_urls:
            yield scrapy.Request(url=parse.urljoin(response.url, post_url),callback=self.parse_detail,dont_filter=True)

    # 打印
    def parse_detail(self, response):
        stock_item = StockItme()
        # 数据传递

        stock_item["Img"] = self.get_Img(response)
        stock_item["Title"] = self.get_tt(response)
        stock_item["Alter"] = self.get_alter(response)
        stock_item["Date"] = self.get_date(response)
        stock_item["Creator"] = self.get_creator(response)
        stock_item["Location"]= self.get_location(response)
        stock_item["Format"] = self.get_format(response)
        stock_item["Dig"] = self.get_dig(response)
        yield stock_item

    def get_Img(self, response):
        # 获取图片名称
        try:
            Img = response.xpath("//*[@id=\"download-menu\"]/li[7]/a/@data-item-id").extract()
            return '{}'.format(*Img)
        except IndexError:
            Imge = response.xpath("//*[@id=\"download-menu\"]/li[11]/a/@data-item-id").extract()
            return '{}'.format(*Imge)

    # 获取标题
    def get_tt(self,response):
        # title内容
        title_ = response.xpath("//*[@id=\"item-info\"]/dl/dt[1]/text()").extract()
        title_t = response.xpath("//*[@id=\"item-info\"]/dl/dd[1]/ul/li/text()").extract()
        return '{}{}'.format(*title_, *title_t)

    # 获取副标题
    def get_alter(self,response):
        # Alternative Title:
        atternative_ = response.xpath("//*[@id=\"item-info\"]/dl/dt[2]/text()").extract()
        atternative_t = response.xpath("//*[@id=\"item-info\"]/dl/dd[2]/ul/li/text()").extract()
        return '{}{}'.format(*atternative_, *atternative_t)

    # 获取日期
    def get_date(self, response):
        # date
        date_ = response.xpath("//*[@id=\"item-info\"]/dl/dt[3]/text()").extract()
        date_t = response.xpath("//*[@id=\"item-info\"]/dl/dd[3]/ul/li/text()").extract()
        return '{}{}'.format(*date_, *date_t)

    # 获取作者
    def get_creator(self, response):
        # creator
        creator_ = response.xpath("//*[@id=\"item-info\"]/dl/dt[4]/text()").extract()
        creator_t = response.xpath("//*[@id=\"item-info\"]/dl/dd[4]/ul/li/a/text()").extract()
        return '{}{}'.format(*creator_, *creator_t)

    # 获取地方
    def get_location(self, response):
        # location
        location_ = response.xpath("//*[@id=\"item-info\"]/dl/dt[5]/text()").extract()
        location_t = response.xpath("//*[@id=\"item-info\"]/dl/dd[5]/ul/li/a/text()").extract()
        return '{}{}'.format(location_,location_t)

    # 获取主题
    def get_format(self,response):
        # format
        format_ = response.xpath("//*[@id=\"item-info\"]/dl/dt[6]/text()").extract()
        format_t = response.xpath("//*[@id=\"item-info\"]/dl/dd[6]/ul/li/a/text()").extract()
        return '{}{}'.format(format_,format_t)

    # 获取传记
    def get_dig(self,response):
        # Digital Collection:
        dig_t = format_t = response.xpath("///*[@id=\"item-info\"]/dl/dd[7]/a/text()").extract()
        return '{}'.format(*dig_t)


#class ExampleSpider(scrapy.Spider):
    # name = 'example'
    # allowed_domains = ['example.com']
    # start_urls = ['http://example.com/']


